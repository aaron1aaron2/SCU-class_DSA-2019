class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        self.head = None 
        self.len = 0    
        
    def get_list(self):
        '''測試用，可回傳list'''
        if self.len != 0:
            return [self.get(item) for item in range(self.len)]
        else :
            return -1
           
    def get(self, index):
        if index<0 or index>=self.len: 
            return -1
        else:
            value = self.head
            for _ in range(index):
                value = value.next
            return value.val
        
    def addAtHead(self, val):
        new_head = ListNode(val)
        if self.len==0:
            self.head = new_head
        else:
            new_head.next = self.head
            self.head = new_head
        self.len+=1

    def addAtTail(self, val):
        new_tail = ListNode(val)
        if self.len==0:
            self.head = new_tail
        else:
            value=self.head
            for _ in range(self.len):
                if value.next==None:
                    break
                else:
                    value=value.next
            value.next = new_tail
        self.len+=1

    def addAtIndex(self, index, val):
        new_insert = ListNode(val)
        if index > self.len:
            return -1
        elif index<=0 or self.len==0:
            self.addAtHead(val)
        else:
            value = self.head #0
            for i in range(self.len):
                if i==(index-1):
                    new_insert.next = value.next 
                    value.next = new_insert     
                else:
                    value = value.next 
            self.len+=1

    def deleteAtIndex(self, index):
        if index >= self.len or self.len==0 or index < 0:
            return -1
        elif self.len==1:
            self.head=None
            self.len=0
        elif index==0:
            value = self.head
            self.head = value.next
            self.len-=1
        else:
            value = self.head
            for i in range(index):
                if i==(index-1):
                    delete_item = value.next 
                    value.next = delete_item.next
                else:
                    value = value.next 
            self.len-=1
                
