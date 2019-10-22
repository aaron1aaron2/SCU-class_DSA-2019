class Solution:
    def isUnivalTree(self, root) 
        '''這方法不是我寫的，但是我覺得很聰明，他針對題目要求去精簡化，畢竟題目只要確認是否有不一樣的數字而已。'''
        
        # 當 heap 不存在時返回 True
        if root == None:
            return True
         
        # 當左邊子節點存在且與父節點不一樣，回傳 false 。
        if root.left!=None and root.val != root.left.val:
            return False
            
        # 當右邊子節點存在且與父節點不一樣，回傳 false 。
        if root.right!=None and root.val != root.right.val:
            return False
        
        # 充分利用 and 的特性去偵測有無某個節點不一樣。
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
