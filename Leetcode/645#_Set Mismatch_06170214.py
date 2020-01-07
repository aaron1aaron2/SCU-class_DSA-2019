class Solution:
    def findErrorNums(self, nums):
        sub = sum(set(nums))
        repeat = sum(nums) - sub #(全部加總) - (set 後加總)
        miss = sum(range(len(nums)+1))-sub # 正確 - 
        return [repeat,miss]
