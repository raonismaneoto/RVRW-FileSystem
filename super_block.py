from Fs import Fs
import os
import constants

class SuperBlock(Fs):

  def __init__(self, size, f_blocks_list, ifree_list):
    self.size = size
    self.bsize = constants.BLOCKS_AMOUNT
    self.f_blocks_list = f_blocks_list
    self.isize = constants.INODES_AMOUNT
    self.ifree_list = ifree_list
    self.modified = False
    self.root_size = 0

  def get_inode_number(self):
    inode_number = self.ifree_list.pop(0)
    save(self.bytefy(), 0 ,'disk')
    return inode_number

  def get_block_number(self):
    block_number = self.f_blocks_list.pop(0)
    save(self.bytefy(), 0 ,'disk')
    return block_number

def save(bytearr, offset, filepath):
  with open(filepath, "rw+") as disk:
    disk.seek(offset, os.SEEK_SET)
    disk.write(bytearr)
    disk.close()
		