from Fs import Fs

class Block(Fs):

	def __init__(self, size=4096, number=None):
		self.start_offset = (2*1024*1024 + 1) + (4096*200*12) + 1
		self.size = size
		self.number = number
		self.data = []

	def get_offset(self):
		return self.start_offset + (self.number * self.size)