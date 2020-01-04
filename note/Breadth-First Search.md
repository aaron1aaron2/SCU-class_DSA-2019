# Breadth-First Search
###### tags: `演算法` `資料結構`
## 簡介
Breadth-First Search(BFS，廣度優先搜尋)，是廣義的Level-Order Traversal，同樣的原理使用在 Graph，就叫做 BFS 。他是已同層次(level)的節點優先，由低層次到高層次。

- 對 Graph 來說某個節點(Node)的層次(level)，相當於起始點到該節點的距離
- 而 Tree 就是的層次(level)就更淺顯易懂了，如下圖:

![](https://i.imgur.com/BMd1yaz.png)

## 課堂
### 1. 概念 & 步驟
![](https://i.imgur.com/1xkkRtI.png)

### 2. pseudocode
![](https://i.imgur.com/YIgCH6L.png)
 
### 3. 有方向性的 graph
![](https://i.imgur.com/DnHnx7U.png)

### 4. 練習: 請寫出下圖的 state 1 & state 2
![](https://i.imgur.com/LfoUsWK.png)


* state 1: ~~B C  F  A G H I D~~
* state 2: E B C F A G H I D


## 參考資料
- [Graph: Breadth-First Search(BFS，廣度優先搜尋)](https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)
- [geeksforgeeks |　Breadth First Search or BFS for a Graph
](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
- [youtube | Depth First & Breadth First Graph Search - DFS & BFS Graph Searching Algorithms](https://www.youtube.com/watch?v=TIbUeeksXcI)
- [hackerearth | Breadth First Search](https://www.hackerearth.com/zh/practice/algorithms/graphs/breadth-first-search/tutorial/)
- [tutorialspoint | Data Structure - Breadth First Traversal](https://www.tutorialspoint.com/data_structures_algorithms/breadth_first_traversal.htm)
