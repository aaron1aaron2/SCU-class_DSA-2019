# use linked list
class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None
        
class MinStack:

    def __init__(self):
        self.head = None #為 stack 得底
        self.len = 0 #last index 為len-1

        
    def get_tail(self, list_len, back_num=1):
        use_index=list_len-back_num
        value = self.head
        if use_index==-1:
            return value
        else:
            for _ in range(use_index):
                value = value.next
        return value
            
    def push(self, x: int) -> None:
        add_item = Node(x)
        if self.len==0:
            self.head = add_item
        else:
            last_item = self.get_tail(self.len)
            last_item.next = add_item
        self.len+=1
        
    def pop(self) -> None:
        if self.len==0:
            pass
        elif self.len==1:
            self.head = None
            self.len = 0
        else:
            SecondLast_item = self.get_tail(self.len,back_num=2)
            SecondLast_item.next = None
            self.len-=1

    def top(self) -> int:
        if self.len==0:
            pass
        else:
            return self.get_tail(self.len).val
            
            
    def getMin(self) -> int:
        if self.len==0:
            pass
        else:
            value = self.head
            Min = value.val
            for _ in range(self.len):         
                if value.val < Min:
                    Min = value.val
                elif value.next==None:
                    break        
                value = value.next
            return Min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
