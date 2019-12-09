from Fs import Fs
import util
import json
import constants

class Inode(Fs):

    def __init__(self, number=None, owner=None, group=None, f_type=None, permissions=None, last_modification=None, 
    last_f_modification=None, last_access=None, disk_addresses=None, size=constants.INODE_SIZE, status=None, logical_device=None, 
    reference_count=None, links=None):
        ### These are the fields of the inode on disk
        self.owner = owner
        self.group = group
        self.f_type = f_type
        self.permissions = permissions
        #last modification of this inode
        self.last_modification = last_modification
        #last modification of the inode's file
        self.last_f_modification = last_f_modification
        self.last_access = last_access
        #Number of links to the file
        self.links = links
        self.disk_addresses = disk_addresses
        ### The next fields are available to the incore inode
        # pag. 63
        self.status = status
        self.logical_device = logical_device
        # The position of this inode on the disk 
        self.number = number
        self.reference_count = reference_count
        self.start_offset =  constants.SUPER_BLOCK_SIZE
        self.block_list = []
        self.file_name = ''
        self.size = size

    def write(self, data):
    	blocks_quantity = self.calculate_blocks_quantity(data)
    	blocks_list = self._get_available_blocks(blocks_quantity)
    	data = bytearray(json.dumps(data))
    	for block in blocks_list:
    		block.write(util.load(data[:(constants.BLOCK_SIZE-1)]))
      self.save()

    def save(self):
      util.save(self.bytefy(), self.get_offset(), 'disk')

    def get_offset(self):
    	return self.start_offset + self.number * self.size

    def calculate_blocks_quantity(self, data):
    	data_size = len(bytearray(json.dumps(data)))
    	blocks_quantity = data_size/constants.BLOCK_SIZE
    	if data_size%constants.BLOCK_SIZE != 0:
    		blocks_quantity += 1
    	return blocks_quantity

    def _get_available_blocks(self, blocks_quantity):
      available_blocks = []
      for block in self.block_list:
        block_instance = util.get_block(block)
        if not block_instance.is_full():
          available_blocks.append(block_instance)
      missing_blocks = blocks_quantity - len(available_blocks)
      has_enough_blocks = missing_blocks <= 0
      sb = util.get_sb()
      if not has_enough_blocks:
        for i in xrange(missing_blocks):
          b_number = sb.get_block_number()
          self.block_list.append(b_number)
          util.create_empty_block(b_number)
          available_blocks.append(util.get_block(b_number))
      return available_blocks

