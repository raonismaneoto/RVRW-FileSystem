from Fs import Fs
import util
import constants

entries = "entries"
contents = "contents"

class Block(Fs):

	def __init__(self, size=constants.BLOCK_SIZE, number=None):
		self.start_offset = constants.SUPER_BLOCK_SIZE + (constants.INODES_AMOUNT + 1) * constants.INODE_SIZE
		self.size = size
		self.number = number
		self.data = {}
		self.data[entries] = {}
		self.data[contents] = []

	def is_full(self):
		return self.size < len(self.bytefy())

	def write(self, data, replace=False):
		if type(data) == tuple:
			entry, inode_number = data
			self.data[entries][entry] = inode_number
		else:
			for d in data:
				self.data[contents].append(d)
		self.save()
	
	def save(self):
		util.save(self.bytefy(), self.get_offset(), 'disk')

	def get_offset(self):
		return self.start_offset + self.number * self.size