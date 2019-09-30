class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None
class MyQueue:

    def __init__(self):
        self.head = None #為頭 front
        self.len = 0 
        

    def push(self, x: int) -> None:
        new_item = Node(x)
        if self.len==0:
            self.head = new_item
        else:
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_item
        self.len+=1
        

    def pop(self) -> int:
        if self.len==0:
            pass
        else:
            del_item = self.head
            self.head = self.head.next
            self.len-=1
            return del_item.val
        
    def peek(self) -> int:
        if self.len==0:
            pass
        else:
            return self.head.val
        
    def empty(self) -> bool:
        if self.len==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
