# Having fun in leetcode
## 目錄
- [1. Design Linked List <Medium>](#1-design-linked-list) | [code](Design%20Linked%20List.py) | [problem](https://leetcode.com/problems/design-linked-list/)
- [2. Set Mismatch <Easy>](#2-set-mismatch) | [code]() | [problem](https://leetcode.com/problems/set-mismatch/) 
- [3. Min Stack <Easy>](#3-min-stack) | [code](Min%20Stack.py) | [problem](https://leetcode.com/problems/min-stack/) 
- [4. Implement Queue using Stacks <Easy>](#4-implement-queue-using-stacks) | [code](Implement%20Queue%20using%20Stacks.py) | [problem](https://leetcode.com/problems/implement-queue-using-stacks/) 
- [5. Insertion Sort List <Medium>](#5-insertion-sort-list) | [code](Insertion%20Sort%20List.py) | [problem](https://leetcode.com/problems/insertion-sort-list) 

   
## 1. Design Linked List  
> 題目: [Leetcode | Design Linked List](https://leetcode.com/problems/design-linked-list/)
設計一個屬於你的 linked-List。其中包含 `singly linked-List` & `doubly linked-List` 這邊我們先以 `singly linked-List` 做練習。 它包含兩個屬性: 
* `val` : 當前 node 的值。
* `next` : 指向下一個 node 的 pointer。

### 需要建立的 function
1. `get(index)` : 輸入 ***index*** 可以取得在 linked-List 裡對應的 ***val***。
1. `addAtHead(val)` : 將輸入的 ***val*** 新增在 linked-List 的第一個位置。
1. `addAtTail(val)` : 將輸入的 ***val*** 新增在 linked-List 的最後一個位置。
1. `addAtIndex(index, val)` : 在 linked-List 中，指定 ***index*** 的位置插入 ***val***。
    * 其他條件
        * 當 ***index*** 等於 linked-List 的長度，將 ***val*** 插在最後一個位置。
        * 當 ***index*** 大於 linked-List 的長度，則 ***val*** 不會插入 linked-List。
        * 當 ***index*** 為負數，將 ***val*** 插在第一個位置。
5. `deleteAtIndex(index)` : 如果 ***index*** 在 linked-List 裡是有效的，刪除對應的 ***val***。

### 我的想法
> 要建立`兩個 class` 
* 第一個: 當做節點(Node)，也就是每次呼叫他的時候，就相當於創立一個新的節點在 memory 裡面。可以看到每個 Node 包含 `self.val` (紀錄資料) 和 `self.next` (紀錄下一個Node)。
```python=
class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None
```

* 第二個: 作為所有功能的集合，所有超做都透過這個 Class 去操作。在 linked-List 的定義下，我們需要知道開頭的 Node 是誰，並記錄下這就是 `self.head` 的功能。`self.len` 是我而外加的(*感覺可以省略* )我覺得這樣比較清楚，他記錄著當前 linked-List 的長度，在實現下面功能時，我們可以透過 `self.len` 去控制這個 Class 下的所有操作。
```python=
class MyLinkedList(object):
    def __init__(self):
        self.head = None 
        self.len = 0
```
> 其他要注意的地方
* 當每次呼叫第一個 Class ListNode( ) 時，就是建立 Node
* Node 之間的連接關係都是透過 `.next` 建立的
* 是否第一次建立 linked-List 
* linked-List 已存在時，`index 是否有效`
* `value.next==None` 時，代表value 是最後一個 Node

為了方便 debug，我在第二個 class MyLinkedList( ) 下寫了一個 function 當呼叫他時會已 list 回傳現在的 linked-List ，大家也可以試試看。
```python=
def get_list(self):
    '''測試用，可回傳list'''
    if self.len != 0:
        return [self.get(item) for item in range(self.len)]
    else :
        return -1
```
其他功能的建構就不講了，大多數是邏輯問題，但是我的程式在 leetcode 上 速度只贏6%的人，還有許多加強的空間。

[回目錄](#目錄)

## 2. Set Mismatch
> 題目: [Leetcode | Set Mismatch](https://leetcode.com/problems/set-mismatch/)

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

### Example
* Input: nums = [1,2,2,4] 
* Output: [2,3]

### key point

* 正常的 set: [1,2,3,4]
* 異常的 set: [1,2,2,4]
* 讓上面兩者比對，輸出 [2,3] --> [重複值,缺失值]

[回目錄](#目錄)

## 3. Min Stack
> 題目: [Leetcode | Min Stack](https://leetcode.com/problems/min-stack/)
### key point
* 高清楚頭尾，要怎麼對應 linked-List 的head 和方向。
* 主要的是 getMin()的實現，需要想一下。

[回目錄](#目錄)

## 4. Implement Queue using Stacks
> 題目: [Leetcode | Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
### key point
* 搞清楚題目要那些功能。

[回目錄](#目錄)

## 5. Insertion Sort List
> 題目: [ Leetcode | Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)

Sort a linked list using insertion sort.

<img src='https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif' weigh='500' height='200'>

> A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list

Algorithm of Insertion Sort:

- Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
- At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
- It repeats until no input elements remain.

Example :
- Input: 4->2->1->3
- Output: 1->2->3->4

[回目錄](#目錄)
