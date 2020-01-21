import random as r
class heap(object):
    def __init__(self):
         self._list = []
    def __str__(self):
        return self._list.__str__()

    def __Heapify__(self, index):
        index += 1 # +1 array start in 0 not 1
        root = (index//2) - 1 # -1 to get true value
        right = ((index * 2) // 1) - 1 # //1 to Round number to int
        left = ((index * 2 + 1) // 1 ) -1 
        index -= 1  #return to true value
        lenght = len(self._list)
        
        #fix sons
        if right  < lenght:
            self.__Heapify__(right)
        if left < lenght:
            self.__Heapify__(left)

        #fix root
        if  root >=0 and self._list[root] < self._list[index]:
            temp = self._list[root]
            self._list[root] = self._list[index]
            self._list[index] = temp
            self.__Heapify__(root)
        
       

    def push(self, value):
        self._list.append(value)
        self.__Heapify__(len(self._list)-1)
    
    def popMax(self):
        result = self._list[0]
        last = self._list.pop() 
        if len(self._list)>0:
            self._list[0] = last
            self.__Heapify__(0)
        return result
        
