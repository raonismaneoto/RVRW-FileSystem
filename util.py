import json
from Fs import Fs

def load(bytearr):
    stringfied = str(bytearr)
    print stringfied
    return json.loads(stringfied)

def instance_from_obj(class_constructor, obj):
    instance = class_constructor()
    for key in obj:
        setattr(instance, key, obj[key])
    return instance