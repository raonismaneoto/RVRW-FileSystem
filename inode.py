from Fs import Fs
import util

class Inode(Fs):

    def __init__(self, number=None, owner=None, group=None, f_type=None, permissions=None, last_modification=None, 
    last_f_modification=None, last_access=None, disk_addresses=None, size=None, status=None, logical_device=None, 
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
        self.start_offset = 2*1024*1024 + 1
        self.block_list = []
        self.file_name = ''

    def write(self, data):
    	block = util.get_block(self.block_list[0])
    	block.data.append(data)
    	util.save(block.bytefy(), block.get_offset(), 'disk')
    	util.save(self.bytefy(), self.get_offset(), 'disk')

    def get_offset(self):
    	return self.start_offset + (self.number * self.size) +1

