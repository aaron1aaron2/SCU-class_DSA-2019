from Crypto.Hash import MD5

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def encrypt(self, text):
        h = MD5.new()
        h.update(text.encode("utf-8"))
        num = int(h.hexdigest(),16)
        return num
    
    def search(self, text):
        num = self.encrypt(text)
        idx = num%self.capacity
        cur = self.data[idx]
        if cur is None:
            return False
        elif cur.val == num:
            return cur
        else:
            while cur.next is not None:
                if cur.val == num:
                    return num
                cur = cur.next
            return False
        
    def add(self, key):
        if self.search(key) is  False:
            num = self.encrypt(key)
            idx = num%self.capacity
            cur = self.data[idx]
            new = ListNode(num)
            if cur is None:
                self.data[idx] = ListNode(num)
            else:
                new.next = self.data[idx]
                self.data[idx].pre = new
                self.data[idx] = new           
        else:
            pass
        
    def remove(self, key):
        num = self.encrypt(key)
        idx = num%self.capacity
        target = self.search(key)
        if target is not False:
            parent = target.pre
            child = target.next
            if parent is None:
                self.data[idx] = child
                if child is not None : child.pre = None
            else:
                parent.next = child
                child.pre = parent
        else:
            pass
        
    def contains(self, key):
        target = self.search(key)
        if target is not False:
            return True
        else:
            return False