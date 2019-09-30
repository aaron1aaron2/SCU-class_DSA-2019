class Solution(object):
	def twoSum(self, List, target):
		complement = dict() # key: list 中每個數字跟目標的差， value: 對應差的index
		for i in range(0, len(List)):
			cmp = target - List[i] 
			# 只要list 裡的數字有在 complement 的 key 裡，則組成配對返回對應的index。
			if List[i] in complement:
				return [complement[List[i]], i]
			complement[cmp] = i
		return None
