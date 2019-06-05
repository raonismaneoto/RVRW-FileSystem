import SuperBlock

SIZE = 20*1024

def mfks(disk_path):

	f_blocks_list = create_f_blocks_list()

	inodes_list = create_inodes_list()

	super_block = SuperBlock(SIZE, 100, f_blocks_list, 15, inodes_list)

	save(super_block, disk_path)


def create_f_blocks_list():
	head = Block()
	current = head
	for i in xrange(100):
		current.next = Block()
		current = current.next
	return head

def create_inodes_list():
	head = Inode()
	current = head
	for i in xrange(15):
		current.next = Inode()
		current = current.next
	return head

def save(sb, disk_path):
	pass