# Minimum Spanning Tree - Dijkstra
###### tags: `演算法` `資料結構`
## 簡介
Dijkstra 演算法他會先定義一個 `起始點` ，他的目的是在一個 graph 裡找到 `起始點` 到所有節點的最短路徑。

注意：不能他不會輸出路徑，只會輸出 `起始點` 到各個節點的最短路徑距離。（可參考：[prim’s implementation](https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/amp/)

### 步驟
1. 選擇起始點作為標準點
2. 此時標準點視為走過的點
3. 判斷標準點可以連到的節點，有以下兩種情況:
    - 已連過: 判斷這次連結 weight 是否會比先前的最短路徑短。
    - 未連過: 直接連接，作為該節點的最短路徑(暫時)。
4. 在可連結到的節點中選擇 weight 最小的，作為新的標準點。
5. 重複 3、4 直到所有節點皆已被拜訪
## 課堂
![](https://i.imgur.com/o7yfBFS.png)

![](https://i.imgur.com/IhJfge5.png)

## 練習
![](https://i.imgur.com/ZyUA9H0.png)

| group               | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (0)                 | 0   | 4   | -   | -   | -   | -   | -   | 8   | -   |
| (0,1)               | 0   | 4   | 12  | -   | -   | -   | -   | 8   | -   |
| (0,1,7)             | 0   | 4   | 12  | -   | -   | -   | 9   | 8   | 15  |
| (0,1,7,6)           | 0   | 4   | 12  | -   | -   | 11  | 9   | 8   | 15  |
| (0,1,7,6,5)         | 0   | 4   | 12  | 25  | 21  | 11  | 9   | 8   | 15  |
| (0,1,7,6,5,2)       | 0   | 4   | 12  | 19  | 21  | 11  | 9   | 8   | 14  |
| (0,1,7,6,5,2,8)     | 0   | 4   | 12  | 19  | 21  | 11  | 9   | 8   | 14  |
| (0,1,7,6,5,2,8,3)   | 0   | 4   | 12  | 19  | 21  | 11  | 9   | 8   | 14  |
| (0,1,7,6,5,2,8,3,4) | 0   | 4   | 12  | 19  | 21  | 11  | 9   | 8   | 14  |

> ans: 0+4+12+19+21+11+9+8+14 = 98 

- [Dijkstra's algorithm in 3 minutes — Review and example](https://www.youtube.com/watch?v=_lHSawdgXpI&feature=emb_rel_pause)
- [youtube | Dijkstra's Algorithm: Another example](https://www.youtube.com/watch?v=5GT5hYzjNoo)
- [hackerearth | Shortest Path Algorithms](https://www.hackerearth.com/zh/practice/algorithms/graphs/shortest-path-algorithms/tutorial/)
- [geeksforgeeks | Dijkstra’s shortest path algorithm | Greedy Algo-7](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
