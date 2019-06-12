from super_block import SuperBlock
from inode import Inode
from block import Block
import os
import pickle

SIZE = 20*1024

def mkfs(disk_path):

	f_blocks_list = create_f_blocks_list()

	inodes_list = create_inodes_list()

	super_block = SuperBlock(SIZE, 100, f_blocks_list, 15, inodes_list)

	save_from(super_block, '$', disk_path)


def create_f_blocks_list():
	head = Block()
	current = head
	for i in xrange(100):
		current.next = Block()
		current = current.next
		save_from(current, '@', 'disk')
	return head

def create_inodes_list():
	head = Inode()
	current = head
	for i in xrange(15):
		current.next = Inode()
		current = current.next
		save_from(current, '!', 'disk')
	return head

def save(sb, disk_path):
	import pickle
	with open(disk_path, "wb") as disk:
		disk.seek(0, os.SEEK_SET)
		pickle.dump(sb, disk)
		disk.close()

def save_from(object, mark_char, disk_path):
	with open(disk_path, "rw+") as disk:
		byte = 0
		for line in disk:
			for char in line:
				if char == mark_char:
					byte = disk.tell()
					disk.seek(byte, os.SEEK_SET)
					pickle.dump(object, disk)
					disk.close()
					return
