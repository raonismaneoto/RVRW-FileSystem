from super_block import SuperBlock
from inode import Inode
from block import Block
import os
import pickle
import util
from memory_keeper import MemKeeper

SIZE = 20*1024

def mkfs(disk_path):

	f_blocks_list = create_f_blocks_list()

	inodes_list = create_inodes_list()

	super_block = SuperBlock(SIZE, 100, f_blocks_list, 15, inodes_list)

	util.save(super_block.bytefy(), 0, 'disk')

	create_root_dir()


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


def create_root_dir():
	sb = util.get_sb()
	inode = util.get_inode(sb.ifree_list[0])
	blocks = [sb.f_blocks_list[0]]
	inode.blocks_list = blocks
	set_root_inode_props(inode)
	save_root_dir(sb, inode, blocks)

def set_root_inode_props(inode):
	pass

def save_root_dir(sb, inode, blocks):
	pass