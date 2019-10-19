# Quick Sort
###### tags: `演算法` `資料結構`

# 課堂作業
> [老師的範例_array](https://github.com/pecu/DSA/blob/master/05_QuickSort/QuickSort_Array_Recursive.ipynb)

> [老師的範例_linked-List](https://github.com/pecu/DSA/blob/master/05_QuickSort/QuickSort_LinkedList.py)


# 課外資料
## 簡介
![](https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/01/QuickSort2.png)

Quick Sort 他是以 [divide-and-conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm) 演算法為基礎。他的概念其實很簡單，就是從 array 中抽取一個數字為 pivot（基準點），將整個 array 依基準點分成兩個小的 array, 比基準點大的放在右邊的array，比基準點小的放在左邊的array，之後左右兩邊的小array 繼續重複同樣到動作（找基準->分兩邊）直到該小array剩下一個為未排序（未當過基準點）。

> 他有四種方式

- 總是以第一個 element 為基準點
- 總是以最後一個 element 為基準點
- 以中位數為基準點
- 隨機基準點(下圖)

<img src="https://he-s3.s3.amazonaws.com/media/uploads/1ea505b.jpg" height='600' weight='500'>

## 特點
- 他有回歸性 (recursive)
- 屬於分治法 ([divide-and-conquer](https://zh.wikipedia.org/zh-tw/%E5%88%86%E6%B2%BB%E6%B3%95))
- 有效率的處理大的資料

## 複雜度分析
- 時間複雜度
    - 最差: [ Big-O ]: O(n2)

    - 理想: [Big-omega]: O(n*log n)

    - 平均: [Big-theta]: O(n*log n)

- 空間複雜度: O(n*log n)

### Difference between Big O and Big Ω
The difference between Big O notation and Big Ω notation is that Big O is used to describe the worst case running time for an algorithm. But, Big Ω notation, on the other hand, is used to describe the best case running time for a given algorithm.
## Is QuickSort stable?
其實由上面的時間複雜度就可以知道 QuickSort 是一個不穩定的排序方式。它的表現跟基準點的選擇有關，當你排序後所有element 都在基準點的同一側，也就是說你選擇的基準點在 array 裡是最大或最小的值，

## Is QuickSort In-place?
>In-place: [原地演算法](https://zh.wikipedia.org/zh-tw/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)

廣義來看 QuickSort 也算是原地演算法，一個原地演算法（in-place algorithm）基本上不需要額外輔助的資料結構,但允許少量額外的輔助變數來轉換資料的演算法。


## 參考網站
- https://www.hackerearth.com/zh/practice/algorithms/sorting/quick--sort/tutorial/
- https://www.geeksforgeeks.org/quick-sort/
- https://www.studytonight.com/data-structures/quick-sort
- https://www.youtube.com/watch?v=CB_NCoxzQnk

# Quick-Sort by linked-List
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Sort-Linked-List-768x384.png)
#### 有興趣可以參考這邊>>> https://www.geeksforgeeks.org/quicksort-on-singly-linked-list/


