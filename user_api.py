import util
import json

def create_file(args):
  sb, root_inode = get_main_obj()
  file_name = args[0]
  check_file_oneness(file_name)
  inode = util.get_inode(sb.get_inode_number())
  root_inode.write({file_name: inode.number})
  sb, root_inode = get_main_obj()
  inode.block_list.append(sb.get_block_number())
  inode.file_name = file_name
  util.create_empty_inode(sb.isize-1)
  util.create_empty_block(sb.bsize-1)
  util.save(inode.bytefy(), inode.get_offset(), 'disk')
  util.save(sb.bytefy(), 0, 'disk')
  print util.get_inode(inode.number).bytefy()

def read_file(args):
  sb, root_inode = get_main_obj()
  file_name = args[0]
  inode_number = -1
  blist = root_inode.block_list
  inode = {}
  for block_number in blist:
    print block_number
    block = util.get_block(block_number)
    for file_descriptor in block.data:
      if type(file_descriptor) == dict and file_name in file_descriptor.keys():
        inode_number = file_descriptor[file_name]
        break
  if inode_number != -1:
    inode = util.get_inode(inode_number)
  print_data(inode)
  return inode

def print_data(inode):
  if inode == {}:
    print inode
    return
  data = ''
  for block in inode.block_list:
    block = util.get_block(block)
    data += json.dumps(block.data)
  print data

def write_file(args):
  file_name = args[0]
  data = [arg for arg in args[1:]]
  inode = read_file([file_name])

  if inode == {}:
    raise Exception("The file %s does not exist" %file_name)

  inode.write(data)

def check_file_oneness(file_name):
  sb, root_inode = get_main_obj()
  blist = root_inode.block_list
  for block_number in blist:
    block = util.get_block(block_number)
    for file_descriptor in block.data:
      if type(file_descriptor) == dict and file_name in file_descriptor.keys():
        raise Exception("The file with name %s already exists" %file_name)

def get_main_obj():
  return [util.get_sb(), util.get_inode(0)]

menu_options = {
  'create': create_file,
  'read': read_file,
  'write': write_file
}

while True:
  user_input = raw_input().split(" ")
  operation = menu_options[user_input[0]]
  operation(user_input[1:])

