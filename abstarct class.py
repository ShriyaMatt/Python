#import neccesary modules
from abc import ABC, abstractmethod
#create bass class
class ABsclass(ABC):
    def print(self,x):
        print("Passed Value:",x)

    @abstractmethod
    def task(self):
        print("We are inside ABsclass.")

class test_class(ABsclass):
    def task(self):
        print("We are inside test_class task.")

test_obj=test_class()
test_obj.task()
test_obj.print(100)