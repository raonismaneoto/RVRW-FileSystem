import json
from Fs import Fs
import os

def load(bytearr):
    stringfied = str(bytearr)
    return json.loads(stringfied)

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
    sb_instance = instance_from_obj(SuperBlock, sb_json)
    return sb_instance

def get_inode():
    pass
    
def get_block():
    pass
