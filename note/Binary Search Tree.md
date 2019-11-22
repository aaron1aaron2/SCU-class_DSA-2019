# Binary Search Tree (BST)
###### tags: `演算法` `資料結構`

## 定義
 Binary Search Tree（BST）是一個以 tree 為基礎的資料結構。這種數據結構是為了更有效率的儲存與搜尋。下面我們以隨機一個節點做 key，root 也算是一個 key，只是它包含所有子節點。
 

* key 會有三種情況，一他是葉節點，二它一邊有子樹（節點），三它兩邊皆有子樹（節點）。
* key 的左子樹中包含的子節點 皆小於 key 值。
* key 的右子樹中包含的子節點皆大於 key 值。
* key 的左子樹與右子樹皆為二元樹（binary tree)。
* 沒有重複的節點。（這次作業有）

## 基本功能
要建立一棵 BST 需要先具備，
其它就最基本的功能有：

### 1. Traversals 走訪
走訪不是一個 function 他是一個用來實習整個 BST 的邏輯，所有功能都需要走訪，他可以拜訪所有的節點，分兩大類：

- depth-first traversal
- breadth-first traversal

在 depth-first traversal 裡面包含遊走子樹的選擇包含三種邏輯。
#### 1. InOrder traversal - 中序走訪
先拜訪左子點在拜訪右子點，最後才是父節點。
![](https://i.imgur.com/1NAZTSl.png)
#### 2. PreOrder traversal - 前序走訪
先拜訪父節點，在拜訪左子點和右子點。
![](https://i.imgur.com/ujHDA5d.png)
#### 3. PostOrder traversal - 後續走訪
先拜訪右子點再來左子點，最後父節點。
![](https://i.imgur.com/DdsmdGZ.png)

>[Refer to](https://hackersir.gitbooks.io/c/content/Ch13/Intro.html)
### 1.Searching
在 BST 的 Search 中，有兩走遊走方式。
- 不使用 recursive(我的方法): 
我們會從 root 開始遊走。我的方法是值機用 while 迴圈去判斷當前有走的值是大於或小於目標值`(cur.val >or< target)`。當知道他應該往哪走的話就看那個方向有沒有路可以走`(not None)`
- 使用 recursive (PreOrder traversal):
由上到下左至右去走訪每個節點。一開始會一直往左去走值到左邊到最底'，但是當你觸底(遇到None)，也就是開始 return 東西時。就會折返，當左子點已走訪完就會開始去確定右邊的其他節點。
簡單來說在 preorder的情況下，每一節點有父節點、左子樹、右子樹，走訪時會先通過 `父節點` 在往 `左子樹` ，當 `左子樹` 已全部走訪時就會開始走訪 `右子樹` 。當這些動作都完成時就會回到 `父節點` 的 `父節點`。

#### 時間複雜度
在BST中搜索時復雜度為O（h），其中h是樹的高度，也就是一般 BST 的效率會受到深度影響。
- 最好狀況: 左右平衡 -> O（log n）
- 最差狀況: 退化成 linked-List -> O（n)

### 2.Insertion
insert 與 search 的過程很像，從 root 開始遞迴的方式往下搜尋，找到對應的位置插入新的節點（需符合BST的定義）。 如果該值本身以存於 BST 裡則不做任何事，因為基本的 BST 裡不會存在重複值。但是此次作業沒有不能重複值限制，所以我設計的 BST 可存在重複值。


### 3.Deletion
刪除超級無敵難。因為我沒使用 recursive ，所以有好幾種情況需要考慮。
1. 目標值是否為 root -> 找尋替補值(兩種方式)
    * 先左在右: 從 root 的左節點往右找最後面的值，切斷其與父節點的連結當作新的節點，將 root 的子樹賦予給新的節點。 (假如說新的節點最後面還有左節點，保留到最後 insert 回tree)
    * 先右在左: 從 root 的右節點往左找最後面的值，切斷其與父節點的連結當作新的節點，將 root 的子樹賦予給新的節點。 (假如說新的節點最後面還有右節點，保留到最後 insert 回tree)
3. 目標值是否存在 
    - if 存在 : 執行3
    - else : 甚麼都不做。
5. 當目標值存在時，遇到的目標節點有下列三種情況:
    * 為葉節點: 直接切斷其與父節點的聯繫，回傳 root。
    * 存在一個子節點: 直接將子節點往上(父節點)連接。
    * 存在兩個子節點: 我取左邊的節點補上原節點。

### 4.modify
一次的 modify 就是一次的 insert 和 delete。那如果要修改多個值呢? 我這邊是用while ， search 先去確定 tree 裡面還有 target 存在再決定要不要在做一次 modify 的動作。所以基本上 insert 和 delete 沒問題就好了。至於 tree 的深度，那是紅黑樹的問題，我就不管了...

## Why would we use BST?
What are some real-world examples of BST’s? Trees are often used in search, game logic, autocomplete tasks, and graphics.

Speed. As mentioned earlier, the BST is an ordered data structure. Upon insertion, the nodes are placed in an orderly fashion. This inherent order makes searching fast. Similar to binary search (with an array that is sorted), we cut the amount of data to sort through by half on each pass. For example, suppose we are looking for a small node value. On each pass, we keep moving along the leftmost node. This eliminates half the greater values automatically!

Also, unlike an array, the data is stored by reference. As we add to the data structure, we create a new chunk in memory and link to it. This is faster than creating a new array with more space and then inserting the data from the smaller array to the new, larger one.

In short, inserting, deleting and searching are the all-stars for a BST

Now that we understand the principles, the benefits, and the basic components of a BST, let’s implement one in javascript.

The API for a BST consists of the following: Insert, Contains, Get Min, Get Max, Remove Node, Check if Full, Is Balanced, and the types of Search — Depth First (preOrder, inOrder, postOrder), Breadth First Search, and lastly Get Height. That’s a big API, just take it one section at a time.
# 參考資料
- [geeksforgeeks | Binary Search Tree](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)
- [freecodecamp](https://hackmd.io/@Zq6oiEB9Ty-KvUdV9n7vOw/SyRJk_cjr)
- [techopedia](https://www.techopedia.com/definition/6282/binary-search-tree-bst)
- video
    - [Binary Tree and Binary Search Tree in Data Structure](https://www.youtube.com/watch?time_continue=424&v=7vw2iIdqHlM)
    - [Binary Search Tree | Set 1 (Search and Insertion) | GeeksforGeeks](https://www.youtube.com/watch?v=qYo8BVxtoH4)
    - [Binary Search Tree | Set 2 (Delete) | GeeksforGeeks](https://www.youtube.com/watch?v=puyl7MBqPIg)
