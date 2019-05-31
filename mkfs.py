import SuperBlock

SIZE = 20*1024

def mfks(disk_path):

	f_blocks_list = create_f_blocks_list()

	inodes_list = create_inodes_list()

	super_block = SuperBlock(SIZE, len(f_blocks_list), f_blocks_list, len(inodes_list), inodes_list)

	save(super_block, disk_path)


def create_f_blocks_list():
	pass

def create_inodes_list():
	pass

def save(sb, disk_path):
	pass