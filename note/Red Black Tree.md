# Red Black Tree
###### tags: `演算法` `資料結構`

## 簡介
紅黑樹(Red Black Tree)，它是一個以樹的資料結構為基礎延伸的，它是為了解決一般二元樹的不平衡問題，樹的出現是希望可以加快搜尋資料， 平均來說它搜尋資料的時間複雜度為 O(logn)，但是當你插入(insert)的資料越是接近整理過的資料時 (例如:[1,2,3,4]) 樹會退化成 linked list ，時間複雜度 O(n) 它會失去原本tree的優勢。而紅黑樹可以透過調整的動作去平衡。

![](https://yotsuba1022.gitbooks.io/data-structure-note/content/assets/rbtree-1.png)

## 特徵
![](https://yotsuba1022.gitbooks.io/data-structure-note/content/assets/rbtree-2.png)
- 紅黑樹的特徵:
    * 節點都有顏色(紅/黑)
    * 在插入和刪除的過程中, 要遵循保持這些顏色的不同排列的規則
- 紅黑樹的規則(紅黑規則):
    * 每個節點不是紅就是黑的(廢話)
    * 根總是黑色的
    * 若節點是紅色的, 則其子節點必為黑色, 反之不必為真(亦即若節點是黑色, 則其子節點可為紅也可為黑), 這條規則其實也是在說明就垂直方向來看, 紅色節點不可以相連
    * 每個空子節點都是黑色的: 所謂的空子節點指的是, 對非葉節點而言, 本可能有, 但實際沒有的那個子節點. 譬如一個節點只有右子節點, 那麼其空缺的左子節點就是空子節點
    * 從根節點到葉節點或空子節點的每條路徑(簡單路徑), 必須包含相同數目的黑色節點(這些黑色節點的數目也稱為黑色高度)
## 紅黑樹是如何維持平衡關係？
這個部分也可以說是分而治之，他將每個子樹都平衡，整棵樹也就會跟著平衡，下面舉個例子：
- 上面三張圖皆為不平衡的狀態，圖1、3 的顏色也不符合規定，你可以看到它呈現`三代的結構`，
- 下則是包含三個子樹的正常狀態

![](https://i.imgur.com/LWmbtsc.png)

## Rotation
![](https://miro.medium.com/max/1960/1*RccOz-HQviItgvKG26oHyg.jpeg)
## Comparison with AVL Tree
The AVL trees are more balanced compared to Red-Black Trees, but they may cause more rotations during insertion and deletion. So if your application involves many frequent insertions and deletions, then Red Black trees should be preferred. And if the insertions and deletions are less frequent and search is a more frequent operation, then AVL tree should be preferred over Red-Black Tree.
## 參考資料
- [Red Black Tree demo](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)
- [geeksforgeeks | Red-Black Tree | Set 1 (Introduction)](https://www.geeksforgeeks.org/red-black-tree-set-1-introduction-2/)
- [Painting Nodes Black With Red-Black Trees](https://medium.com/basecs/painting-nodes-black-with-red-black-trees-60eacb2be9a5)
- [Red-Black Tree (紅黑樹)](https://yotsuba1022.gitbooks.io/data-structure-note/content/1.4.3-red-black-tree.html)
