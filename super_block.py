from Fs import Fs

class SuperBlock(Fs):

	def __init__(self, size=2*1024*1024, bsize=None, f_blocks_list=None, isize=None, ifree_list=None):
		self.size = size
		self.bsize = bsize
		self.f_blocks_list = f_blocks_list
		self.isize = isize
		self.ifree_list = ifree_list
		self.modified = False
		self.root_size = 0

	def get_inode_number(self):
		inode_number = self.ifree_list[0]
		self.ifree_list.pop(0)
		self.ifree_list.append(self.isize)
		self.isize += 1
		return inode_number

	def get_block_number(self):
		block_number = self.f_blocks_list[0]
		self.f_blocks_list.pop(0)
		self.f_blocks_list.append(self.bsize)
		self.bsize += 1
		return block_number
		