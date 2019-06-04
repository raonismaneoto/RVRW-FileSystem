from os.path import exists 
from mkfs import mkfs

FILE_NAME = 'disk'
SUPER_BLOCK_SIZE = 2 * 1024 * 1024
INODE_SIZE = 4 * 1024 * 1024
BLOCK_SIZE = 16 * 1024 * 1024
FILE_SIZE = 20 * 1024 * 1024

def create_disk_file():
  f = open(FILE_NAME, 'wb')
  f.write('$' * SUPER_BLOCK_SIZE)
  f.write('!' * INODE_SIZE)
  f.write('@' * BLOCK_SIZE)
  f.close()

def disk_file_exists():
  return exists(FILE_NAME)

def setup():
  if not disk_file_exists(): create_disk_file()
  mkfs(FILE_NAME)

setup()
