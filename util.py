import json
from Fs import Fs
import os
from inode import Inode
from block import Block
from super_block import SuperBlock

def load(bytearr):
    stringfied = str(bytearr)
    return aval(json.loads(json.dumps(stringfied)))

def save(bytearr, offset, filepath):
  with open(filepath, "rw+") as disk:
    disk.seek(offset, os.SEEK_SET)
    disk.write(bytearr)
    disk.close()

def read(filepath, offset, size):
  with open(filepath, "rw+") as disk:
    disk.seek(offset, os.SEEK_SET)
    result = disk.read(size)
    disk.close()
    return result

def instance_from_obj(class_constructor, obj):
    instance = class_constructor()
    for key in obj:
        setattr(instance, key, obj[key])
    return instance

def get_sb():
    sb_bytearr = read('disk', 0, 2*1024*1024)
    sb_json = load(sb_bytearr)
    print sb_json
    print type(sb_json)
    sb_instance = instance_from_obj(SuperBlock, sb_json)
    return sb_instance

def get_inode(number):
    inode_bytearr = read('disk', (2*1024*1024 + 1) + 4096*12*number, 4096*12)
    inode_json = load(inode_bytearr)
    inode_instance = instance_from_obj(Inode, inode_json)
    return inode_instance
    
def get_block(number):
    block_bytearr = read('disk', ((2*1024*1024 + 1) + (4096*200*12) + 1) + 4096*number, 4096)
    block_json = load(block_bytearr)
    block_instance = instance_from_obj(Block, block_json)
    return block_instance