# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
     def insertionSortList(self, head):
        # 直接指定已排序的頭為第一個，它是假的，可以節省下面比較的部分
        newHead = ListNode(0)
        newHead.next = head 
        # 確認還有下一個代處理的值
        while head and head.next:
            # 已經排序好的跳過
            if head.val > head.next.val:
                nodeToInsert = head.next
                # 比較
                cur = newHead
                while cur.next and cur.next.val<nodeToInsert.val:
                    cur = cur.next
                # 先將基準值指定到下一個要找的值
                head.next = nodeToInsert.next
                # 插入到比自己大的值之前
                nodeToInsert.next = cur.next
                cur.next = nodeToInsert
            else:
                head = head.next
            
        return newHead.next
