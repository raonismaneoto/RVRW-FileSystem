import util
import json

working_inode_number = 0

def create_file(args):
  sb, root_inode = get_main_obj()
  file_name = args[0]
  check_file_oneness(file_name)
  inode = util.get_inode(sb.get_inode_number())
  root_inode.write({file_name: inode.number})
  sb, root_inode = get_main_obj()
  inode.block_list.append(sb.get_block_number())
  inode.file_name = file_name
  inode.f_type = util.FileType.file.value
  util.create_empty_inode(sb.isize-1)
  util.create_empty_block(sb.bsize-1)
  util.save(inode.bytefy(), inode.get_offset(), 'disk')
  util.save(sb.bytefy(), 0, 'disk')

def read_file(args):
  sb, root_inode = get_main_obj()
  file_name = args[0]
  inode_number = -1
  blist = root_inode.block_list
  inode = {}
  for block_number in blist:
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
    print 'There is no file attached to this name'
    return
  data = ''
  for block in inode.block_list:
    block = util.get_block(block)
    data += json.dumps(block.data) + '\n'
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

def isMounted():
  sb, root_dir = get_main_obj()
  return root_dir.file_name == 'root'

def mount(args):
  create_root_dir()

def create_root_dir():
  sb = util.get_sb()
  inode = util.get_inode(sb.get_inode_number())
  blocks = [sb.get_block_number()]
  util.create_empty_inode(100)
  util.create_empty_block(100)
  set_root_inode_props(inode, blocks)
  save_root_dir(sb, inode)

def set_root_inode_props(inode, blocks):
  inode.owner = 'root'
  inode.group = 'root'
  inode.f_type = util.FileType.dir.value
  inode.permissions = 111111111
  inode.links = 1
  inode.disk_addresses = 1
  inode.block_list = blocks
  inode.file_name = 'root'

def save_root_dir(sb, inode):
  sb.root_size = inode.get_size()
  util.save(sb.bytefy(), 0, 'disk')
  util.save(inode.bytefy(), inode.get_offset(), 'disk')

def get_inodes_from_inode(inode_number):
  inode = util.get_inode(inode_number)
  inodes = []
  for block_number in inode.block_list:
    block = util.get_block(block_number)
    for file_descriptor in block.data:
      if type(file_descriptor) == dict:
        name, _inode_number = file_descriptor.items()[0]
        _inode = util.get_inode(_inode_number)
        inodes.append(_inode)
  return inodes

def create_dir(args):
  file_name = args[0]
  sb = util.get_sb()
  inode = util.get_inode(working_inode_number)
  # TODO update this method to parse inode number by param
  check_file_oneness(file_name)
  _inode = util.get_inode(sb.get_inode_number())
  inode.write({file_name: _inode.number})
  sb, root_inode = get_main_obj()
  inode.f_type = util.FileType.dir.value
  inode.block_list.append(sb.get_block_number())
  inode.file_name = file_name
  util.create_empty_inode(sb.isize-1)
  util.create_empty_block(sb.bsize-1)
  util.save(inode.bytefy(), inode.get_offset(), 'disk')
  util.save(sb.bytefy(), 0, 'disk')

def ls(args):
  result = []
  inodes = get_inodes_from_inode(working_inode_number)
  for inode in inodes:
    result.append(inode.file_name)
  print(result)
  return result

def cd(args):
  global working_inode_number
  dir_name = args[0]
  inodes = get_inodes_from_inode(working_inode_number)
  matches = [i for i in inodes if i.file_name == dir_name]
  if len(matches) > 1:
    print("Fatal Error: Found two inodes with same name")
  elif len(matches) == 1:
    match = matches[0]
    if match.f_type == util.FileType.dir.value:
      working_inode_number = match.number
      print("Changed current directory to " + match.file_name)
    else:
      print(dir_name + " is not an directory!")
  else:
    print("Not found directory with name " + dir_name)

menu_options = {
  'create': create_file,
  'read': read_file,
  'write': write_file,
  'mount': mount,
  'mkdir': create_dir,
  'ls': ls,
  'cd': cd
}

while True:
  user_input = raw_input().split(" ")
  if user_input[0] != 'mount' and not isMounted():
    print "Please, you need to mount the FS first"
    continue
  if user_input[0] == 'exit':
    break
  operation = menu_options[user_input[0]]
  operation(user_input[1:])

