from super_block import SuperBlock
from inode import Inode
from block import Block
import os
import pickle
import util

SIZE = 20*1024

def mkfs(disk_path):

	f_blocks_list = create_f_blocks_list()

	inodes_list = create_inodes_list()

	super_block = SuperBlock(SIZE, 100, f_blocks_list, 15, inodes_list)

	util.save(super_block.bytefy(), 0, 'disk')


def create_f_blocks_list():
	head = Block()
	current = head
	l = []
	for i in xrange(100):
		file_position = current.start_offset +(4096*i)
		util.save(current.bytefy(), file_position, 'disk')
		current.next = Block()
		current = current.next
		l.append(file_position)
	return l

def create_inodes_list():
	head = Inode()
	current = head
	l = []
	for i in xrange(15):
		file_position = current.start_offset +(4096*i)
		util.save(current.bytefy(), file_position, 'disk')
		current.next = Inode()
		current = current.next
		l.append(file_position)
	return l
