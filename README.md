# My algorithms & data-structures Learning Note 
> 歡迎來到 2019_三下_資料結構與演算法 的學習筆記

## Contents
- [不可不知道的事](#不可不知道的事)
- [About me](#About-me)
- [學習資源](#學習資源)
- [課堂筆記](#課堂筆記)
- [課堂作業](#課堂作業)
- [課外學習](#課外學習)
- [課程心得](#課程心得)

## 不可不知道的事
這些專有名詞很重要，在學習這堂課前可以先去查查看，還有提醒一下，請不要只查中文，英文的資源更豐富。
下面我租略介紹一下關於資料結構與演算法的基本觀念...

### 1. 資料結構 (data structure)
在電腦科學中，資料結構是電腦中儲存、組織資料的方式，資料的組織與架構會大大影響資料處理效能，這也是我們學習資料結構的重點所在。

- 常見的資料結構 
  - 堆疊（Stack）
  - 佇列（Queue）
  - 陣列（Array）
  - 連結串列（Linked List）
  - 樹（Tree） 
  - 圖（Graph） 
  - 堆積（Heap）
  - 雜湊表（Hash table）
  

### 2. 演算法 (algorithms)
我的想法是演算法起源於問題，因為有問題需要透過電腦去解決，所以人們就會定義一個步驟和邏輯達到目的，這就是演算法。許多演算法都是透過某個資料結構為基礎去產生的，針對不同問題會有不同的演算法，但是資料結構是相通的，所以資料結構很重要一好好學。針對同個問題也會有不同的演算法，一般來說新的演算法通常是最出色的，但是在同個問題不同情境下，各演算法的表現又會不一樣。這就要你們去慢慢理解了。

> 這邊有更詳細的解釋 >> [初學者學演算法｜談什麼是演算法和時間複雜度-medium](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E8%AB%87%E4%BB%80%E9%BA%BC%E6%98%AF%E6%BC%94%E7%AE%97%E6%B3%95%E5%92%8C%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6-b1f6908e4b80)

### 3. 時間複雜度 (Time complexity)
一個程式的時間複雜度是指完全地執行程式所需的計算機時間。時間複雜度是比較演算法好不好的一個標準，使用時間會隨著資料量變多而增加。這邊我簡單的說一下它的概念，時間複雜度 `O(n)` 表示，它是趨近於無限的狀況做比較。`O(n)` 代表說我花的時間與資料量是 1:1 的，而 `n^2` 代表花的時間是資料量的平方倍。
> - 各種常見演算法的時間複雜度可以看這個 >> [big-0 時間複雜度表](https://www.bigocheatsheet.com/)
> - 關於 `big-o` 可以看這裡 >> [the basics of big-o notation](https://medium.com/better-programming/the-basics-of-big-o-notation-e67228e549d2)。

### 4. 空間複雜度 (Space complexity)
空間複雜度的意思就是你的演算法在處理問題的整過程，最大需要儲存多少暫存。假如說我今天進來的是長度為 n 的 list，而我從頭到尾都只用這個 list 做處理，空間複雜度就是 n ，也稱作 [原地演算法-In-place algorithm](https://en.wikipedia.org/wiki/In-place_algorithm)。如果用了額外的 list (長度為n) 去存取，就是 2n。

---
## About me
> 我是一個天真、可愛、善良的大學生~

### **何彥南** 

<img src='https://i.imgur.com/pFlGRnJ.png' weight=300 height=200>

* 就讀於: Soochow University (東吳大學)
* 主修: 巨量資料管理學系
* 生日: 1998/11/26
* 星座: 射手座
* 興趣: 打羽球
* 綽號: 荷花、熊、187
* 擅長程式: python 

---
## 學習資源
- [*非關語言: 常見程式演算*](https://openhome.cc/Gossip/AlgorithmGossip/) >> 包含一些程式演算法的練習實作題目，對新手蠻友善的。
### 英文資源
#### 演算法教學
- [*Geeksforgeeks*](https://www.geeksforgeeks.org/) >> 最推薦，每個部份皆包含影片，整理完整，除了演算法和資料結構外還有許多其他 CS 學習資源。
- [*Hackerearth*](https://www.hackerearth.com/zh/practice/algorithms/searching/linear-search/tutorial/) 
- [*Studytonight*](https://www.studytonight.com/data-structures/introduction-to-data-structures) 
- [*Tutorialspoint*](https://www.tutorialspoint.com/data_structures_algorithms/) 
#### 演算法範例程式碼
- [*The Algorithms - Python*](https://github.com/TheAlgorithms/Python) >> 有許多演算法 python 的範例程式可以參考。
#### 課程資源
- [關於 computer science 的國外大學課程](https://github.com/prakhar1989/awesome-courses#algorithms) >> 給英文程度好，肯努力的人看

---
### 中文資源
#### 演算法教學
- [*完整的演算法筆記*](http://www.csie.ntnu.edu.tw/~u91029/) >> 某位認真的人整理的筆記，雖然有部分有寫錯，但是講的淺顯易懂且該有的都有。
- 相關課程資源(國內)

#### 課程資源
- **台灣大學/清華大學** - 資訊之芽
   - 演算法班

      - [*2019 課程講義*](https://www.csie.ntu.edu.tw/~sprout/algo2019/)
      - [*2018 課程講義*](https://www.csie.ntu.edu.tw/~sprout/algo2018/)
      - [*2017 課程講義*](https://www.csie.ntu.edu.tw/~sprout/algo2017/)
      - [*2016 課程講義*](https://www.csie.ntu.edu.tw/~sprout/algo2016/)

    - C/C++ 班

      - [*2019 課程講義*](https://tw-csie-sprout.github.io/c2019/#!slides.md)
      - [*2018 課程講義*](https://tw-csie-sprout.github.io/c2018/#!slides.md)
      - [*2017 課程講義*](https://tw-csie-sprout.github.io/c2017/#!slides.md)
      - [*2016 課程講義*](https://tw-csie-sprout.github.io/c2016/#!slides.md)
      - [*2015 課程講義*](http://tw-csie-sprout.github.io/programming15spring/#!slide.md)

    - Python 班

      - [*2019 課程講義*](https://tw-csie-sprout.github.io/py2019/#!slides.md)
      - [*2018 課程講義*](https://tw-csie-sprout.github.io/py2018/#!slides.md)
      - [*2017 課程講義*](https://tw-csie-sprout.github.io/py2017/#!slides.md)
      - [*2016 課程講義*](https://tw-csie-sprout.github.io/py2016/#!slides.md)

  - **交通大學** - PCCA 競技程式訓練
    - [*2019 冬令營課程講義*](https://sites.google.com/g2.nctu.edu.tw/pcca-winter-2019/%E8%AA%B2%E7%A8%8B%E8%B3%87%E8%A8%8A?authuser=0)
    - [*2018 夏令營課程講義*](https://sites.google.com/g2.nctu.edu.tw/pcca-summer-2018/%E8%AA%B2%E7%A8%8B%E8%B3%87%E8%A8%8A?authuser=0)
    - [*2018 冬令營課程講義*](https://sites.google.com/g2.nctu.edu.tw/pcca-winter-2018/%E8%AA%B2%E7%A8%8B%E8%B3%87%E8%A8%8A?authuser=0)
    - [*2017 冬令營課程講義*](https://sites.google.com/view/nctupcca/2017-%E4%BA%A4%E5%A4%A7%E7%AB%B6%E6%8A%80%E7%A8%8B%E5%BC%8F%E8%A8%93%E7%B7%B4%E5%86%AC%E4%BB%A4%E7%87%9F/%E8%AA%B2%E7%A8%8B%E8%B3%87%E8%A8%8A?authuser=0)
    - [*2016 夏令營課程講義*](https://sites.google.com/site/pccanctu/2016-summer-camp/sources)
    - [*2016 冬令營課程講義*](https://sites.google.com/site/pccanctu/2016-winter-camp/resources)

  - **交通大學** - PSPT 課程

    - [*2014 PSPT 課程講義*](https://drive.google.com/drive/u/0/folders/0BydVf1xpoCSQdzZUWGZzQWtEZnM?tid=0BydVf1xpoCSQM0lHMWU3cTZJaW8)

  - **成功大學** - ACM 課程

    - [*2019 Spring NCKU ACM Training Courses*](https://nckuacm.github.io/2019/)
    - [*2018 Spring NCKU ACM Training Courses*](https://nckuacm.github.io/2018/)

## 課堂筆記
### week 1
- [github](note/Github.md)

### week 2
- [linked List](note/Linked-list.md)

### week 3
- [Stack & Queue](note/Stack%20&%20Queue.md)

### week 4
- [set](note/set.md) 
- [Insertion Sort](note/Insertion%20Sort.md) 

### week 5
- [Quick Sort](note/Quick%20Sort.md)

### week 6
- [Heap Sort](note/Heap%20sort.md)

### week 7
- [Merge Sort](note/Merge%20Sort.md)

### week 8
- [Binary Tree](note/Tree.md)
 
### week 9
- [Binary Search Tree](note/Binary%20Search%20Tree.md)

### week 10
- [Red Black Tree](note/Red%20Black%20Tree.md)

### week 11 
- [Hash Table](note/hash%20table.md)

### week 12
- [Breadth-First Search](note/Breadth-First%20Search.md)

### week 13 
- [Depth-First Search](note/Depth-First%20Search.md)

### week 14
- [Minimum Spanning Tree - Kruskal](note/Kruskal.md)

### week 15
- [Shortest Path - Dijkstra](note/Dijkstra.md)

### week 16
- 課程回顧

### Week 17
- 區塊鏈實作分享
  - [簡大為作品 Demo >>> 不看會後悔，看了一秒變粉絲...](https://youtu.be/RqTTfm0vF4c)
  - [陳偉傑作品 Demo](https://youtu.be/Ri3o0ZqYBmQ)
  - [陳佳淳作品 Demo](https://youtu.be/DQT6R-27bDY)
  
## 課堂作業
- [HW1: Quick Sort](HW1/Quick%20Sort.ipynb)
- [HW2: merge sort](HW2/Merge%20Sort%20流程圖%26說明.ipynb)
- [HW2: heap sort](HW2/Heap%20Sort%20流程圖%26說明.ipynb)
- [HW3: Binary Search Tree](HW3/BST_學習歷程與說明.ipynb)
- [HW4: hash table](HW4/hash_table_學習歷程.ipynb)
- [HW5: DFS & BFS](HW5/DFS_學習歷程與說明.ipynb)
- [HW6: Dijkstra & ruskal](HW6/Dijkstra%20%26%20Kruskal_學習歷程與說明.ipynb)


## 課外學習
### leetcode 
#### >> [go to folder](Leetcode)

### CS50 
#### >> [go to folder](CS50)

## 課程心得
資料結構與演算法這堂課在我們巨量資料的領域是不可或缺的知識，剛開始的時候其實我也蠻排斥蔡老師的授課方式，尤其是作業方面，老實說蠻花時間的。但是慢慢的發現原來在這堂課下，我慢慢建立起了自己的自學模式，這對我來說是一個收穫。我也發現了其實網路上的學習資源很多，都是寶藏，差的就是你有沒有毅力去發掘去學習。還有一點就是如果你程式基礎不夠，我有以下幾點建議:
- 演算法這堂課主要是你的思考如何解決問題的過程，程式碼不是最重要的，畢竟答案都查的到，程式碼只是實現想法的工具。
- 程式碼寫不出來參考別人沒關係，但是在看別人的解法前，我都會嘗試的自己去思考去寫，就算你的解法不是最好的，但至少你有自已的想法。
- 參考別人的程式不是複製貼上，而是去了解它為何會這樣寫，還要加上參考資料，這是對原創者的尊重。

最後，謝謝`蔡芸琤老師`、`賴建郡助教`、`司福銘助教`陪我走完這學期，這學期我也學了蠻多的。也讓我更了解我現在正走的路是多麼艱辛且多變的。

### 希望大家也要更了解自己想要甚麼
* 基本功很重要，不要整天想飛。
* 試著去了解 DS、CS是在做甚麼。
* 知識永遠學不完，要懂得取捨。
* 學分不是修很多就厲害，知道你自己在在學甚麼才是最重要的。
* 中文的資料有限，找尋英文資料，不去排斥英文，你會有驚喜。
* 每天給自己固定的時間學習。
* **要記得你是最棒的~**
