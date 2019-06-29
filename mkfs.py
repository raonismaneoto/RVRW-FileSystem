from super_block import SuperBlock
import os
import pickle
import util
from memory_keeper import MemKeeper

SIZE = 20*1024

def mkfs(disk_path):

	f_blocks_list = create_f_blocks_list()

	inodes_list = create_inodes_list()

	super_block = SuperBlock(SIZE, 100, f_blocks_list, 100, inodes_list)

	util.save(super_block.bytefy(), 0, 'disk')


def create_f_blocks_list():
	head = util.Block()
	current = head
	l = []
	for i in xrange(100):
		current.number = i
		current.size = 4096
		file_position = current.get_offset()
		util.save(current.bytefy(), file_position, 'disk')
		l.append(current.number)
		current.next = util.Block()
		current = current.next
	return l

def create_inodes_list():
	head = util.Inode()
	current = head
	l = []
	for i in xrange(100):
		current.number = i
		current.size = 4096*12
		file_position = current.get_offset()
		util.save(current.bytefy(), file_position, 'disk')
		l.append(current.number)
		current.next = util.Inode()
		current = current.next
	return l