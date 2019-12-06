from Fs import Fs
import util
import constants

class Block(Fs):

	def __init__(self, size=constants.BLOCK_SIZE, number=None):
		self.start_offset = constants.SUPER_BLOCK_SIZE + (constants.INODES_AMOUNT + 1) * constants.INODE_SIZE
		self.size = size
		self.number = number
		self.data = []

	def is_full(self):
		return size < len(self.bytefy())

	def write(self, data, offset=self.get_offset()):
		self.data.append(data)
		util.save(self.bytefy(), offset, 'disk')
	
	def save(self):
		util.save(self.bytefy(), self.get_offset(), 'disk')

	def get_offset(self):
		return self.start_offset + self.number * self.size