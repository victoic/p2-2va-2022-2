from abc import ABC, abstractmethod
import os

dir = os.path.dirname(__file__)

class File(ABC):
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
    
    @abstractmethod
    def operate(self):
        pass

class FileReader(File):
    _instances = {}

    def __new__(cls, path, filename):
        shared = os.path.join(path, filename)
        if shared not in cls._instances:
            cls._instances[shared] = super(FileReader, cls).__new__(cls)
        return cls._instances[shared]

    def __init__(self, path, filename):
        super().__init__(path, filename)
    
    def operate(self):
        try:
            with open(os.path.join(self.path, self.filename), 'r') as f:
                return f.read()
        except:
            print('File does not exist')

class FileWriter(File):
    _instances = {}

    def __new__(cls, path, filename):
        shared = os.path.join(path, filename)
        if shared not in cls._instances:
            cls._instances[shared] = super(FileWriter, cls).__new__(cls)
        return cls._instances[shared]

    
    def __init__(self, path, filename):
        super().__init__(path, filename)
    
    def operate(self, command, mode = 'a'):
        try:
            with open(os.path.join(self.path, self.filename), mode) as f:
                f.write(f"{command}\n")
                return True
        except:
            return False

if __name__ == '__main__':
    # Testing gitthe operations
    file = FileReader(os.path.join(dir, '../log'), 'test.txt')
    print(file.operate())

    file = FileWriter(os.path.join(dir, '../log'), 'test.txt')
    print(file.operate('Opaaaaa!'))

    file = FileReader(os.path.join(dir, '../log'), 'test.txt')
    print(file.operate())

    # Testing if the creation of Files with tha same path and filename is avoided
    print('Testing Design Pattern')
    file = FileReader(os.path.join(dir, '../log'), 'test.txt')
    file2 = FileReader(os.path.join(dir, '../log'), 'test.txt')
    print(file is file2)