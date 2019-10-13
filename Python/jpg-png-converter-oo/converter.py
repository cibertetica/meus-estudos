import config
import os

class Archive():
    def __init__(self, path):
        self.path = path
    
    def convert(self):
        for f in os.listdir(self.path):
            if f[-4:] == '.jpg':
                new_f = f.replace('.jpg', '.png')
                os.replace(self.path + f, self.path + new_f)
        
outros = Archive(config.path)
outros.convert()