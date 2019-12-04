from super_block import SuperBlock
import os
import pickle
import util
from memory_keeper import MemKeeper
from constants import SUPER_BLOCK_SIZE

DEFAULT_BLOCKS_AMOUNT = 100

def mkfs(disk_path):

	f_blocks_list = create_f_blocks_list()
	inodes_list = create_inodes_list()
	super_block = SuperBlock(SUPER_BLOCK_SIZE, DEFAULT_BLOCKS_AMOUNT, f_blocks_list, DEFAULT_BLOCKS_AMOUNT, inodes_list)
	util.save(super_block.bytefy(), 0, 'disk')


def create_f_blocks_list():
	l = []
	for i in xrange(DEFAULT_BLOCKS_AMOUNT):
		current = util.Block(number=i)
		file_position = current.get_offset()
		util.save(current.bytefy(), file_position, 'disk')
		l.append(current.number)
	return l

def create_inodes_list():
	l = []
	for i in xrange(DEFAULT_BLOCKS_AMOUNT):
		current = util.Inode(number=i)
		file_position = current.get_offset()
		util.save(current.bytefy(), file_position, 'disk')
		l.append(current.number)
	return l