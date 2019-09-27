# use linked list
class MinStack:

    def __init__(self):
        self.mylist=[]
        self.len=0
              
    def push(self, x: int) -> None:
        self.mylist.append(x)
        self.len+=1
        
    def pop(self) -> None:
        if self.len==0:
            pass
        else:
            self.mylist.pop(self.len-1)
            self.len-=1

    def top(self) -> int:
        return self.mylist[self.len-1]
    
    def getMin(self) -> int:
        return min(self.mylist)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
