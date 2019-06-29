from Fs import Fs
import util

class Block(Fs):

	def __init__(self, size=4096, number=None):
		self.start_offset = (2*1024*1024 + 1) + (4096*200*12) + 1
		self.size = size
		self.number = number
		self.data = []

	def is_full(self):
		return len(self.data) != 0

	def write(self, data):
		self.data.append(data)
		util.save(self.bytefy(), self.get_offset(), 'disk')

	def get_offset(self):
		return self.start_offset + (self.number * self.size) + 1