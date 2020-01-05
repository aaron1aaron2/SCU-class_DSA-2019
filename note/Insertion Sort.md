# Insertion Sort
###### tags: `演算法` `資料結構` `排序`

# 課堂
![](https://i.imgur.com/1JrragX.png)

> [老師 ppt](https://docs.google.com/presentation/d/e/2PACX-1vQOTMDM-5-OUaGfnLUOFVgefFwSVRplSwnbicp0CXOQrB5H8RM_1Aq8o_4JxHlncEmhjvqk3tzcoB7s/pub?start=false&loop=false&delayms=3000&slide=id.g619c41add7_0_24)

### 作法
分成已排序 (小 -> 大) 和未排序兩部分。依序由未排序中的第一筆為基準值(正處理的值)，插入到已排序中的適當位置。在比較時...
* 直到遇到 `第一個 < 基準值` 的值，停止並插入在該值右邊。
* 遇到 `> or = 基準值` 的值，將該值往右移動，基準值繼續往前比較。

### 時間複雜度 (Time Complexity)
* **Best Case：Ο(1)**
    * 當資料的順序恰好為由小到大時，每回合只需比較1次
* **Worst Case：Ο(n2)**
    * 當資料的順序恰好為由大到小時，第i回合需比i次
* **Average Case：Ο(n2)**
    * 第n筆資料，平均比較n/2次
### 空間複雜度(Space Complexity)：θ(1)
### 穩定性(Stable/Unstable)：穩定(Stable)

# 外部資料
<img src="https://miro.medium.com/max/1023/1*_NOe6jL9veyR4yAyf85dzA.png" width="600" height="300">

### 步驟
1. 第一個(最左邊)的數字直接做為已排序的頭。
1. 將下一個值(右邊)作為基準值。
1. 與所有已排序中的數字比對(右->左)。
1. 移動所有比基準值大的數字。
1. 插入基準值。
1. 回到第2個步驟。
### 特點
* 處理較小的資料時，它是有效的。但對於較大的資料，它的效率非常低。

* Insertion Sort 是有適應性。也就是說如果有部分排序的列表，它可以藉由減少步驟，進而提高效率。

* 它的空間複雜度較小，排序時只需要單個額外的存儲空間。

* 插入排序的總時間複雜度為O（n2）。



## 參考
* [An Introduction to Insertion Sort | by Karuna Sehgal
](https://medium.com/karuna-sehgal/an-introduction-to-insertion-sort-16b97619697)
* [Inching Towards Insertion Sort | by Vaidehi Joshi
](https://medium.com/basecs/inching-towards-insertion-sort-9799274430da)
