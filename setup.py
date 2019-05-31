from os.path import exists 
from mkfs import mkfs

FILE_NAME = 'disk'
FILE_SIZE = 20 * 1024 * 1024

def create_disk_file():
  f = open(FILE_NAME, 'wb')
  f.write("\0" * FILE_SIZE)

def disk_file_exists():
  return exists(FILE_NAME)

def setup():
  if not disk_file_exists(): create_disk_file()
  mkfs(FILE_NAME)

setup()
