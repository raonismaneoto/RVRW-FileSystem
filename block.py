from Fs import Fs

class Block(Fs):

	def __init__(self):
		self.start_offset = (2*1024*1024 + 1) + (4096*200) + 1
		self.data = []