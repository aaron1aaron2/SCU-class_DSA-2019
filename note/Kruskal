# Minimum Spanning Tree - Kruskal
###### tags: `演算法` `資料結構`

## 課堂
可以看到 MST 他也是一種 graph 的衍伸，他注重在點與點之間的一個量值(cost、weight、spend time)。所以他是以 **邊(edge)** 為主體的資料結構去紀錄。每個節點只要有一條連結連到 tree 裡面就可以了。

![](https://i.imgur.com/V2FHxJF.png)

### 應用環境
最小生成樹可以應用在很多地方，主要的目的就是以最小的 cost 去將樹狀網路串耶起來。舉個例子，一個國家要牽光纖網路，只要大家都有一條線接到整個網路就好，這時我們就可以使用 MST，想像每個節點都是一個城市，城市與城市之間有不同的牽線成本，要如何規劃整個網路要麼去布局，才能以最低的成本達到目的。

### 步驟
![](https://i.imgur.com/szk1jSN.png)

1. 生成紀錄 edge 和 weight 的表
2. 依造 weight 去 sorted 整個表
3. 生成一個為 -1 的 array 紀錄每個點連結到的tree 的 root 
    - [(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),(6,-1),(7,-1),(8,-1)]
5. 由小到大去加入 edge，當 edge 加入 時造成 cycle 的情況，則跳過該 edge，值到所有 node 都連結到。
    - 連結(7,6) 
        - 7 & 6 沒對外連接也不是 root ，加入 (7,6)
        - status: [(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),(6,7),(7,-1),(8,-1)]
        - out: [(6,7)]
    - 連結(8,2)
        - status: [(0,-1),(1,-1),(2,8),(3,-1),(4,-1),(5,-1),(6,7),(7,-1),(8,-1)]
        - out: [(6,7),(2,8)]
    - 連結(6,5)
        - status: [(0,-1),(1,-1),(2,8),(3,-1),(4,-1),(5,7),(6,7),(7,-1),(8,-1)]
        - out: [(6,7),(2,8),(6,5)]
    - 連結(0,1)
        - status: [(0,1),(1,-1),(2,8),(3,-1),(4,-1),(5,7),(6,7),(7,-1),(8,-1)]
        - out: [(6,7),(2,8),(6,5),(0,1)]
    - 連結(2,5)
        - 2 & 5 的 root 不同，可以連接，則一為 root
        - status: [(0,1),root(1,-1),(2,7),(3,-1),(4,-1),(5,7),(6,7),root(7,-1),(8,7)]
        - out: [(6,7),(2,8),(6,5),(0,1),(2,5)]
    - 連結(8,6)
        - 8 & 6 的 root 一樣，pass
    - 連接(2,3)
        - 3 沒對外連接也不是 root ，加入 (2,3)
        - status: [(0,1),root(1,-1),(2,7),(3,7),(4,-1),(5,7),(6,7),root(7,-1),(8,7)]
        - out: [(6,7),(2,8),(6,5),(0,1),(2,5),(2,3)]
    - 以此類推....

### procedure code
![](https://i.imgur.com/JTesz8p.png)


## 我的理解
每個節點一開始都中立，只要兩個節點接在一起就會形成一個子樹。一開始這些中立的節點中會挑最近（cost小）的節點們會連結形成一個子樹，隨機取一個節點為該子樹的root，如果在原本的 graph cost 的大小分佈比較散，那一開始就會有很多子樹同時存在。如果分佈集中，那基本上就是一個子樹獨大。但是最終會只剩下最小生成樹。

要如何判斷要不要讓節點間產生新的連結 ，會遇到四種狀況：

1. 子樹與節點，中立國直接加入聯盟因為他沒有老大
2. 節點與節點，兩者結盟形成新的子樹，隨機選擇老大。
3. 子樹與子樹，兩邊打架，最終一定會一邊勝利，所以會結成一個聯盟。而新的 root 為原本兩個二選一。
4. 聯盟內鬥或是節點間私通(cycle)，自己人打自己人，這時老大會制止，因為他是中央集權，不希望看到內鬥發生或是聯盟內的國家間私通，所以會直接把他們的關係斷掉。

以上就是四種狀況，只有在第四種情況時不會新增 edge

## 參考資料
- [youtube | Kruskal's algorithm in 2 minutes — Review and example](https://youtu.be/71UQH7Pr9kU)
- [youtube | Kruskal’s Algorithm for Minimum Spanning Tree | GeeksforGeeks](https://www.youtube.com/watch?v=3rrNH_AizMA)
- [youtube | Union Find Kruskal's Algorithm](https://www.youtube.com/watch?v=JZBQLXgSGfs)
- [geeksforgeeks | Kruskal’s Minimum Spanning Tree Algorithm | Greedy Algo-2](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
- [hackerearth | Minimum Spanning Tree](https://www.hackerearth.com/zh/practice/algorithms/graphs/minimum-spanning-tree/tutorial/)

