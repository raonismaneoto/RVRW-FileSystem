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

	create_root_dir()


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


def create_root_dir():
	sb = util.get_sb()
	inode = util.get_inode(sb.ifree_list[0])
	blocks = [sb.f_blocks_list[0]]
	sb.ifree_list.pop(0)
	sb.f_blocks_list.pop(0)
	util.create_empty_inode(100)
	util.create_empty_block(100)
	sb.ifree_list.append(100)
	sb.f_blocks_list.append(100)
	sb.bsize += 1
	sb.isize += 1
	set_root_inode_props(inode, blocks)
	save_root_dir(sb, inode)

def set_root_inode_props(inode, blocks):
	inode.owner = 'root'
	inode.group = 'root'
	inode.f_type = 'dir'
	inode.permissions = 111111111
	inode.links = 1
	inode.disk_addresses = 1
	inode.block_list = blocks
	inode.file_name = 'root'

def save_root_dir(sb, inode):
	sb.root_size = inode.get_size()
	util.save(sb.bytefy(), 0, 'disk')
	util.save(inode.bytefy(), inode.get_offset(), 'disk')