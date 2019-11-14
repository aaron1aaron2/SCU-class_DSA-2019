# Stack & Queue
###### tags: `演算法` `資料結構`

# 課堂
<img src="https://i.imgur.com/ArHZkOR.png" width="600" height="250">

> 擷取至: [老師的PPT](https://docs.google.com/presentation/d/e/2PACX-1vQ1hb79im0vqpApCttGnXAFRT8SqH9HQP0b_oyVRCV8SVyiHLkHJjidYGAfxkvq468QMumFIDdTeiB-/pub?start=false&loop=false&delayms=3000&slide=id.g5ff860a9a8_0_5)
## 為什麼要有 Stack?
* 編譯器(word、sublime)的 undo 。
* 網頁瀏覽器中回到上一頁功能。
* 任何遞迴(recursion)形式的演算法都可以用 Stack 改寫，例如 Depth-First Search(DFS,深度優先搜尋)

## Stack 必須有的功能
* **Push(Data)**: 把資料放到最上面(最新)。
* **Pop**: 把資料從最上面(最新)移除。
* **Top**: 回傳最上面(最新)的資料。
* **IsEmpty**: 確認stack 裡面是否有資料。
* **getSize**: 回傳stack 裡的資料個數。

## 為什麼要有 Queue
* **應用在其他演算法**: 
    * Bread-First Search | 廣度優先搜尋
    * Tree 的 Level-Order Traversal | 二元樹走訪
* 作業係統被多個程式共享資源時(例如CPU、應表機、網站伺服器)，一次只能執行一個需求，所以需要用 Queue 來安排執行順序。

## Queue 必須有的功能
* **Push(Data)**: 把資料放到 Queue 的後面，並更新成新的 back。
* **Pop(dequeue)**: 把 front 所指向的資料從 Queue 中移除，並更新front。
* **getFront**: 回傳 front 所指向的資資料。
* **getBack**: 回傳 Back 所指向的資資料。
* **IsEmpty**: 確認 Queue 裡是否有資料。
* **getSize**: 確認 Queue 裡的資料個數。

# 外部資料

## Queue 
<img src="https://i.imgur.com/RYR0bLH.png" width="350" height="250">

簡單來講就是 `先插入的先刪除`(First in first out | FIFO), 可用來實現 **廣度優先搜尋**(Breadth-first search | BFS).
- **Additions** (又稱: Enqueues) always add to the back of the line
- **Removals** (又稱: Dequeues) always remove from the front of the line
> 用 list 實現基本的 queue 功能

```python=
q = []
q.insert(0,v) #在頭的位置插入 
q.pop() #刪除最後一個(先插入的)element
```
## Stack: 
`後(新)插入的先刪除` (Last in first out | LIFO)，可用在 **深度優先搜尋**(DFS | Depth-First Search)
> 用 list 實現基本的 stack 功能
```python=
stack = []
stack.append(v) #在最後面插入
stack.pop() #刪除最後一個(新插入的)element
```
# 參考
* [老師的PPT](https://docs.google.com/presentation/d/e/2PACX-1vQ1hb79im0vqpApCttGnXAFRT8SqH9HQP0b_oyVRCV8SVyiHLkHJjidYGAfxkvq468QMumFIDdTeiB-/pub?start=false&loop=false&delayms=3000&slide=id.g5ff860a9a8_0_5)
* [GeeksforGeeks | difference-between-stack-and-queue-data-structures](https://www.geeksforgeeks.org/difference-between-stack-and-queue-data-structures/)
* [Medium | Data Structures: Introductions and Implementation with Python](https://medium.com/algorithms-and-leetcode/data-structures-introductions-and-implementation-with-python-1c9088f19420)
* [Medium | A Gentle Introduction to Data Structures: How Queues Work](https://medium.com/free-code-camp/a-gentle-introduction-to-data-structures-how-queues-work-f8b871938e64)
# 練習
## Min Stack
> 題目: [Leetcode | Min Stack](https://leetcode.com/problems/min-stack/)
### key point
* 高清楚頭尾，要怎麼對應 linked-List 的head 和方向。
* 主要的是 getMin()的實現，需要想一下。

## Implement Queue using Stacks
> 題目: [Leetcode | Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
### key point
* 搞清楚題目要那些功能。
