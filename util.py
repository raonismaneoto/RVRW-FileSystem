import json
from Fs import Fs
import os

def load(bytearr):
    stringfied = str(bytearr)
    print stringfied
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
