import util

menu_options = {
	'create': create_file
}

sb = util.get_sb()
root_inode = util.get_inode(1)

while True:
	user_input = raw_input().split()
	operation = menu_options[user_input[0]]
	operation(user_input[1:])

def create_file(file_name):
	inode = util.get_inode(sb.ifree_list[0])
	inode.block_list.append(util.get_block(sb.f_blocks_list[0]))
	root_inode.write({file_name: inode.number})
	sb.ifree_list.pop(0)
	sb.f_blocks_list.pop(0)
	util.save(inode.bytefy(), inode.get_offset(), 'disk')
	util.save(sb.bytefy(), 0, 'disk')
	util.save(block.bytefy(), block.get_offset(), 'disk')
	print "file %s created" %file_name
