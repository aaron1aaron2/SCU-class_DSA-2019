class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        index = 0
        for i in nums:
            x = target-i
            if str(x) in dict:
                return [dict[str(x)], index]
            else:
                dict[str(i)] = index
            index+=1
