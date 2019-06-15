from Fs import Fs

class SuperBlock(Fs):

	def __init__(self, size=2*1024*1024, f_blocks_counter=None, f_blocks_list=None, isize=None, ifree_list=None):
		self.size = size
		self.f_blocks_counter = f_blocks_counter
		self.f_blocks_list = f_blocks_list
		self.isize = isize
		self.ifree_list = ifree_list
		self.modified = False
		