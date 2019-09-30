class Solution(object):
	def twoSum(self, l, target):
		complement = dict()
		for i in range(0, len(l)):
			cmp = target - l[i]
			if l[i] in complement:
				return [complement[l[i]], i]
			complement[cmp] = i
		return None
