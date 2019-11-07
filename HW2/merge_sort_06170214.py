class Solution(object):
    def compare(self,subarray_left,subarray_right):
        # 變數
        l_idx,r_idx = 0,len(subarray_left) 
        output_array = subarray_left+subarray_right
        border =len(output_array)

        # 比較與排序
        while border>0:
            if l_idx==r_idx or r_idx==border:
                remain = output_array[:border]
                output_array = output_array[border:]
                output_array.extend(remain)
                border=0
            elif output_array[l_idx]<=output_array[r_idx]:
                smaller = output_array[l_idx]
                output_array = output_array[:l_idx]+output_array[l_idx+1:]
                output_array.append(smaller)
                border-=1
                r_idx-=1               
            else:
                smaller = output_array[r_idx]
                output_array = output_array[:r_idx]+output_array[r_idx+1:]
                output_array.append(smaller)
                border-=1
        return output_array

    def merge_sort(self,input_):
        # 折返限制
        size = len(input_)
        if size > 1:
            # 切分
            div = len(input_)//2
            subarray_left = input_[:div]
            subarray_right = input_[div:]
            
            # 準備左邊的 array
            subarray_left = self.merge_sort(subarray_left)
            
            # 準備右邊的 array
            subarray_right = self.merge_sort(subarray_right)
            
            # 兩個array 都準備好則開始比較
            return self.compare(subarray_left,subarray_right)
        elif size ==1:
            return input_