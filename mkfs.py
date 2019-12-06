from super_block import SuperBlock
import os
import pickle
import util
from memory_keeper import MemKeeper
from constants import *

def mkfs(disk_path):
	f_blocks_list = create_f_blocks_list()
	inodes_list = create_inodes_list()
	super_block = SuperBlock(SUPER_BLOCK_SIZE, f_blocks_list, inodes_list)
	util.save(super_block.bytefy(), 0, 'disk')

def create_f_blocks_list():
	l = []
	for i in xrange(BLOCKS_AMOUNT):
		current = util.Block(number=i)
		current.save()
		l.append(current.number)
	return l

def create_inodes_list():
	l = []
	for i in xrange(INODES_AMOUNT):
		current = util.Inode(number=i)
		current.save()
		l.append(current.number)
	return l