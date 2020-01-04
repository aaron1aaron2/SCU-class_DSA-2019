class Solution:
    def partition(self,array,low,high): 
        '''基準點比較,排序'''
        border = (low-1) # 起始index (最左邊)，就是一個邊界的概念，在邊界的左邊是以排序過的值(比基準小的值)，右邊是帶排序的值。
        pivot = array[high] # 以最後一個為基準

        for cur in range(low , high): 

            # 當現在的位置比基準點小時，邊界值(i)與當前值(cur)做交換做交換，把較小的值往左移的同時移動邊界(i++)，較大的直不動。
            if   array[cur] < pivot: 
                border += 1 # i++
                array[border],array[cur] = array[cur],array[border] # 交換

        array[border+1],array[high] = array[high],array[border+1] 
        return ( border+1 ) 

    def quickSort(self,array,low,high): 
        '''當 low == high 代表 array只剩一個element，就可以停了。'''
        if low < high: 
            pi = self.partition(arr,low,high) # 返回排序完後的基準點位置

            self.quickSort(arr, low, pi-1) # 把小於基準的index 再丟回 quickSort 跑。
            self.quickSort(arr, pi+1, high) # 把大於基準的index 再丟回 quickSort 跑。
            
    def sortArray(self, nums):
        n = len(nums) 
        self.quickSort(nums,0,n-1) # 頭到尾的 index
        
        return nums
