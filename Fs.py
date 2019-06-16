import json

class Fs(object):

    def __init__(self):
        pass
    
    def bytefy(self):
      #TODO each object must implement this method to limit the bytearray size.
        jsonfied = json.dumps(self.__dict__) + '\x00'
        byte_arr = bytearray(jsonfied)
        return byte_arr
    
    def __getitem__(self, key):
        if key in dir(self):
            return self.__dict__[key]
        return None
    
    def get_size(self):
        return len(bytearray(json.dumps(self.__dict__)))
        