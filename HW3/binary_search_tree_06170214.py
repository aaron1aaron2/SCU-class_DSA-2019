class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution(object):
    def insert(self, root, val):
        new_node = TreeNode(val)
        cur = root
        
        while cur.right!=None or cur.left!=None:
            if val <= cur.val  and cur.left!=None:
                cur.left.parent = cur
                cur = cur.left
            elif val > cur.val and cur.right!=None:
                cur.right.parent = cur
                cur = cur.right
            else:
                break

        if val <= cur.val:
            new_node.parent = cur
            cur.left = new_node
        else:
            new_node.parent = cur
            cur.right = new_node
        return new_node
            
    def search(self, root, target):
        if root==None or target==None:
            return None
        if root.val == target:
            return root
        cur = root
        while cur.right!=None or cur.left!=None:
            if target < cur.val and cur.left!=None:
                cur.left.parent = cur
                cur = cur.left
                if cur.val == target:
                    return cur
            elif target > cur.val and cur.right!=None:
                cur.right.parent = cur
                cur = cur.right
                if cur.val == target:
                    return cur
            else:
                return None

    def delete(self, root, target):
        root = self.delete_node(root,target)
        cur = self.search(root, target)
        if cur!=None:
            root = self.delete(cur,target)
        return root
        
    def delete_node(self, root, target):
        cur = self.search(root, target)
        if cur == None:
            return root
            pass
        else:
            if cur.left==None and cur.right==None:
                if root==target:
                    return None
                if cur.parent.val >= cur.val:
                    cur.parent.left =None
                else:
                    cur.parent.right =None
                cur.parent = None
                
                return root
            
            elif  cur.left == None and cur.right!=None:
                if root.val == target:
                    root.right.parent =None
                    return root.right
                if cur.parent.val >= cur.val:
                    cur.parent.left = cur.right
                    cur.right.parent = cur.parent
                    cur.parent = None
                else:
                    cur.parent.right = cur.right
                    cur.right.parent = cur.parent
                    cur.parent = None
                
                return root
            
            elif cur.left != None and cur.right==None:
                if root.val == target:
                    root.left.parent==None
                    return root.left
                if cur.parent.val >= cur.val:
                    cur.parent.left = cur.left
                    cur.left.parent = cur.parent
                    cur.parent = None
                else:
                    cur.parent.right = cur.left
                    cur.left.parent = cur.parent
                    cur.parent = None
                    
                return root
                
            elif cur.left!=None and  cur.right!=None:
                if root.val == target:
                    cur = root.left
                    if cur.right !=None:
                        while cur.right !=None:
                            cur = cur.right
                    else:  
                        root.left.right = root.right
                        root.left.right.parent = None
                        return root.left
                    
                    cur.parent.right =None
                    cur.parent = None

                    root.right.parent = cur
                    root.left.parent = cur
                    if cur.left != None:
                        global node_insert
                        node_insert = cur.left
                        cur.right = root.right
                        cur.left = root.left
                        new = self.insert(cur,node_insert.val)
                        new.right = node_insert.right
                        new.left = node_insert.left
                        return cur
                    cur.right = root.right
                    cur.left = root.left

                    return cur

                if cur.parent.val >= cur.val:
                    cur.parent.left = cur.left
                    cur.parent.left.parent = cur.parent
                    cur.parent.left.right = cur.right
                    cur.right.parent = cur.parent.left
                else:
                    cur.parent.right = cur.left
                    cur.parent.right.parent = cur.parent
                    cur.parent.right.right = cur.right
                    cur.right.parent = cur.parent.right
                    
                return root
 
    def modify(self, root, target, new_val):
        while self.search(root, target)!=None:
            root = self.delete_node(root,target)
            self.insert(root, new_val)
        return root