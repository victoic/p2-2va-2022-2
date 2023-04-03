from abc import ABC, abstractmethod
import os

class File(ABC):
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
    
    @abstractmethod
    def operate(self):
        pass

class FileReader(File):
    def __init__(self, path, filename):
        super().__init__(path, filename)
    
    def operate(self):
        try:
            with open(os.path.join(self.path, self.filename), 'r') as f:
                return f.read()
        except:
            print('file doesnt exist')

class FileWriter(File):
    def __init__(self, path, filename):
        super().__init__(path, filename)
    
    def operate(self):
        try:
            with open(os.path.join(self.path, self.filename), 'w') as f:
                f.write()
                return True
        except:
            return False