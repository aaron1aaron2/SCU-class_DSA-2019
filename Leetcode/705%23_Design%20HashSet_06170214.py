class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0  
        self.arr = [[] for i in range(10000)] 
        self.pointer = dict()
        
    def add(self, key: int) -> None:
        self.pointer[key] = self.size
        self.arr[self.size] = True
        self.size+=1
        
    def remove(self, key: int) -> None:
        if key in self.pointer.keys():
            self.arr[self.pointer[key]] = False
            self.pointer.pop(key)
        else:
            pass

        
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.pointer.keys():
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
