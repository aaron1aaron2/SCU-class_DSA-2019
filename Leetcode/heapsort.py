class Solution(object):
    def get_child(self,parent):
            return {'left':2*parent+1,'right':2*parent+2}
    def max_heap(self,input_,size):
        for i in range(size-1,-1,-1):
            child = self.get_child(i)
            left = child['left']
            right = child['right']

            if (size<=left): 
                continue
            elif (size<=right): 
                if input_[left]>input_[i]:
                    input_[i],input_[left] = input_[left],input_[i]
            else:
                if (input_[i]>input_[left]) & (input_[i]>input_[right]): 
                    continue
                elif (input_[right]<input_[left])&(input_[left]>input_[i]):
                    input_[i],input_[left] = input_[left],input_[i]
                else:  
                    input_[i],input_[right] = input_[right],input_[i]  
    def sortArray(self,input_):
        size = len(input_)
        while size>1:
            self.max_heap(input_,size)
            input_[0],input_[size-1] = input_[size-1],input_[0]
            size-=1
        return input_
