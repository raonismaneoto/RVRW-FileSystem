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
		return self.size < len(self.bytefy())

	def write(self, data, replace=False):
		self.data.append(data)
		self.save()
	
	def write_dir(self, entry, inode_number):
		if len(self.data) == 0:
			self.data = {}
		self.data[entry] = inode_number
		self.save()
	
	def save(self):
		util.save(self.bytefy(), self.get_offset(), 'disk')

	def get_offset(self):
		return self.start_offset + self.number * self.size