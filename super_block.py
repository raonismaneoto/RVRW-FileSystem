class SuperBlock():

	def __init__(self, size, f_blocks_counter, f_blocks_list, isize, ifree_list):
		self.size = size
		self.f_blocks_counter = f_blocks_counter
		self.f_blocks_list = f_blocks_list
		self.isize = isize
		self.ifree_list = ifree_list
		self.modified = False
		