import config
import os

class Subtitle():
    def __init__(self, path):
        self.path = path

    def convert(self):
        for f in os.listdir(self.path):
            with open(self.path + f, 'w', encoding='utf8') as saving:
                saving.write('Nova legenda')
    
legenda = Subtitle(config.directory)
legenda.convert()
