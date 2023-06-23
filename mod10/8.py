# Создайте класс LookUpKeyDict, родителем которого будет класс UserDict. 
# Сделайте функцию lookup_key методом класса LookUpKeyDict.

from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        return [key for key, val in self.data.items() if val == value]
        
            
                