import json

class Fs():

    def __init__(self):
        pass
    
    def bytefy(self):
      #TODO each object must implement this method to limit the bytearray size.
        jsonfied = json.dumps(self.__dict__)
        return bytearray(jsonfied)
    
    def __getitem__(self, key):
        if key in dir(self):
            return self.__dict__[key]
        super(Fs, self).__getitem__(key)
    
        