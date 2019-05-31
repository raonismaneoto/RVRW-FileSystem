import os
from mkfs import mkfs

FILE_NAME = 'disk'
FILE_SIZE = 20 * 1024 * 1024

def create_disk_file():
    with open(FILE_NAME, 'wb') as f:
        f.write(os.urandom(FILE_SIZE))

def disk_file_exists():
    return os.path.exists(FILE_NAME)

def setup():
    if not disk_file_exists(): create_disk_file()
    mkfs(FILE_NAME)

setup()
