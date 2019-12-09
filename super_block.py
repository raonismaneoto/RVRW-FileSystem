from Fs import Fs
import os
import constants

class SuperBlock(Fs):

  def __init__(self, size=constants.SUPER_BLOCK_SIZE, f_blocks_list=None, ifree_list=None):
    self.size = size
    self.f_blocks_list = f_blocks_list
    self.ifree_list = ifree_list

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
		