from abc import ABC, abstractmethod

class File(ABC):
    def __init__(self, path, filename):
        self.path = path
        self,filename = filename
    
    @abstractmethod
    def operate(self):
        pass

class FileReader(File):
    def __init__(self, path, filename):
        super().__init__(path, filename)
    
    def operate(self):
        pass

class FileWriter(File):
    def __init__(self, path, filename):
        super().__init__(path, filename)
    
    def operate(self):
        pass