# Tree
###### tags: `演算法` `資料結構`


## 定義
A binary tree 是一種樹數據結構，其中每個節點最多具有兩個子節點，從而創建樹的分支。
這兩個子節點通常稱為左右節點。父節點是具有子節點的節點，而子節點可能包括對其父節點指引。

![](https://i.imgur.com/SzKdh74.png)


* **Path** − Path refers to the sequence of nodes along the edges of a tree.
* **Root** − The node at the top of the tree is called root. There is only one root per tree and one path from the root node to any node.
* **Parent** − Any node except the root node has one edge upward to a node called parent.
* **Child** − The node below a given node connected by its edge downward is called its child node.
* **Leaf** − The node which does not have any child node is called the leaf node.
* **Subtree** − Subtree represents the descendants of a node.
* **Visiting** − Visiting refers to checking the value of a node when control is on the node.
* **Traversing** − Traversing means passing through nodes in a specific order.
* **Levels** − Level of a node represents the generation of a node. If the root node is at level 0, then its next child node is at level 1, its grandchild is at level 2, and so on.
* **keys** − Key represents a value of a node based on which a search operation is to be carried out for a node.


> [refer to]( https://www.tutorialspoint.com/data_structures_algorithms/tree_data_structure.htm)

## 優點
* Trees 可以用來存儲有層次結構的信息。例如，電腦上的文件系統。
* 像是 Linked Lists ,由於節點是使用 pointer 鏈接的，因此樹的節點數量沒有上限。(array 有上限)
* Trees 可以直接反映出資料的結構。
* Trees 的結構適合 insertion 和 searching。
* Trees 的結構彈性大，移動部分的 sub-Trees 對整體的影響小。

## 應用
* 處理有分層的數據
* 資料庫(查詢資料)
* heap sort
* 視覺特效
* 路由演算法
* 多類別決策

## Full Binary Tree 
![](https://i.imgur.com/sF0uNXX.png)

除了葉子以外的所有節點都有子節點。

## Complete Binary Tree
![](https://i.imgur.com/2LZWBI1.png)

tree 中的所有層級都被完全填充。
 
## Perfect Binary Tree 
![](https://i.imgur.com/AAvUq8n.png)

是 Full Binary Tree 的進階版。其中所有內部節點都有兩個子節點，所有葉子都處於同一級別。


## Balanced Binary Tree
A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes. For Example, AVL tree maintains O(Log n) height by making sure that the difference between heights of left and right subtrees is atmost 1. 
**Red-Black trees** maintain O(Log n) height by making sure that the number of Black nodes on every root to leaf paths are same and there are no adjacent red nodes. Balanced Binary Search trees are performance wise good as they provide O(log n) time for search, insert and delete.
## A degenerate (or pathological) tree 
![](https://i.imgur.com/ObzQRRb.png)

大家都只有一個子節點，近似於 linled-List。


## 參考資料
- [geeksforgeeks | Binary Tree Data Structure](https://www.geeksforgeeks.org/binary-tree-data-structure/)
    - [Binary Tree | Set 1 (Introduction)](https://www.geeksforgeeks.org/binary-tree-set-1-introduction/)
    - [Binary Tree | Set 2 (Properties)](https://www.geeksforgeeks.org/binary-tree-set-2-properties/)
    - [Binary Tree | Set 3 (Types of Binary Tree)](https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/)
- [Carnegie Mellon University | Binary Trees](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html)
- [tutorialspoint | Data Structure and Algorithms - Tree](https://www.tutorialspoint.com/data_structures_algorithms/tree_data_structure.htm)

