# Heap Sort 
###### tags: `演算法` `資料結構`
>[老師ppt](https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.p)

## What is Heap?
Heap(Binary Heap) 是以 tree(樹) 為基礎的資料結構, 他有以下特點:

* Shape Property: Heap 的資料結構永遠都是 `完全二元樹  Complete Binary Tree`, 也就是在每個 level(層級) ，由左至右都有 Node(節點)，但是如果是同層級的左至右少一個結點，就不是完全二元樹了。(如下圖)

![](https://www.studytonight.com/data-structures/images/heap-binary-tree-example.png)

* Heap Property: 所有節點再初始狀態下沒有大小排序. 但是當所有 parent nodes(父節點)> 所有的 child nodes(子節點), 就會稱作 `Max-Heap`。反之當所有 parent nodes(父節點)< 所有的 child nodes(子節點) `Min-Heap`。(如下圖)

<img src='https://i.imgur.com/u6OeFbC.png' height=400 weight=673>


- 它是 linked 的進化版，一般在 linked-List 裡的 Node 裡面，只會包含 value 和 pointer(往前或往後)。但是它把在 heap 裡面，它限制只能往一個方向

## Why array based representation for Binary Heap?
由於 Binary Heap 是 `完全二元樹  Complete Binary Tree`，因此可以輕易的傳換成 array 的形式，而且使用 array 也可以節省使用的空間。

假設index 從0開始，父節點在 index=a 的位置則:
- 左子節點 = 2 x a + 1 
- 右子節點 = 2 x a + 2

## Heap Sort Algorithm for sorting in increasing order:

1. 將 array 轉換成 max heap 的形式。
2. 此時 root 的值為 max 。將 root 值與最後一個 index 的值互換，然後將heap 的大小 -1 ，也就是把排序過最大的值丟到 array後面，使其index不再之後處理的範圍內。
3. 重複以上動作，直到 heap 的大小 =1(剩下一個 element)。

## Applications of HeapSort
1. 用來排序 nearly sorted (or [K sorted](https://www.youtube.com/watch?v=yQ84lk-EXTQ) ) array
2. 獲取 array 中 k 個最大(或最小)的元素

>heap sort 在使用上有限，因為 Quicksort 和 Mergesort 在實際應用上表現更好。
儘管如此，heap 的資料結構已被大量使用。


## Complexity Analysis of Heap Sort
* 時間複雜度 : O(n*log n)

* 空間複雜度 : O(1)

## 特性
- 不穩定
- 需要連續的空間
- 速度快，被廣泛運用
- 是一個 in-place 演算法




##  Heap Sort  step-by-step
### Initial Elements (初始元素)

<img src='https://i.imgur.com/eBDrKvL.png' height=200 weight=750>

### Max Heap

<img src='https://i.imgur.com/gx0FGCY.png' height=200 weight=750>

### Step 0
> 將其轉換為 max heap

<img src='https://i.imgur.com/BOy1IvU.png' height=330 weight=720>

### Step 1

> 8 與 5 交換。>>  8 與 heap 切斷連結，此時 8 已經為排序過的 element。

<img src='https://i.imgur.com/Xy2r7Cu.png' height=330 weight=720>

### Step 2
> 建立 Max-heap >> 7 與 3 交換 >> 7 與 heap 切斷連結。

<img src='https://i.imgur.com/LlgrgNf.png' height=330 weight=720>

### Step 3
> 建立 Max heap  >> 5 與 1 交換 >> 5 與 heap 切斷連結。

<img src='https://i.imgur.com/ccgbPsl.png' height=330 weight=720>

### Step 4
> 建立 Max heap >> 4 與 3 交換 >> 4 與 heap 切斷連結。

<img src='https://i.imgur.com/gDYAi3D.png' height=330 weight=720>

### Step 5
> 建立 Max heap >> 3 與 1 交換 >> 3 與 heap 切斷連結。

<img src='https://i.imgur.com/N7IFaUW.png' height=330 weight=720>

### Result

![](https://i.imgur.com/sJeGPoz.png)
> [原文](https://www.hackerearth.com/zh/practice/algorithms/sorting/heap-sort/tutorial/) | Contributed by: Akash Sharma
## 參考網站
* https://en.wikipedia.org/wiki/Heapsort
* https://www.geeksforgeeks.org/heap-sort/
* https://www.hackerearth.com/zh/practice/algorithms/sorting/heap-sort/tutorial/
* https://www.studytonight.com/data-structures/heap-sort
* https://www.youtube.com/watch?v=MtQL_ll5KhQ
# 可用套件
### 1. heapq
> https://docs.python.org/zh-tw/3/library/heapq.html

# 練習
## Univalued Binary Tree
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.
> 前往 >> [題目](https://leetcode.com/problems/univalued-binary-tree/)
