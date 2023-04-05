from abc import ABC, abstractmethod

class Window(ABC):
    def __init__(self, file_reader, file_writer):
        self.history = ''
        self.file_reader = file_reader
        self.file_writer = file_writer
        
    def checkAction(self):
        file_content = self.file_reader.operate()

        if file_content != self.history:
            self.history = file_content
            return True
        
        return False
    #Feito por Tiago
