# Depth-First Search 
###### tags: `演算法` `資料結構`
{%hackmd @rpyapp/theme %}
## 介紹
>DFS 它屬於 recursive(遞迴) 的演算法。他主要的的想法就是先往某個方向走到底也就是 Depth-First 的意思，然後折返再去看他的分支，就像是 BST 的走訪。
他會 backtracking(回朔)，也就是走到底再往回找未被標記的節點，在走到底，這概念跟 BST 很像

![](https://i.imgur.com/Z6SIeJv.png)

###  Depth First Traversal of a tree
> 其實 tree 的 走訪規則也是 DFS 的其中一種應用，看下圖就知道他們其實邏輯是一樣的，也是可以把 tree 當作 graph，只是下列特點:
 - 有方向
 - edge 關係嚴格: 被一個節點指向，指向兩個節點
 - 沒有迴圈關係: 不會有一條路，可以繞一圈回到原點

![](https://i.imgur.com/dbGlhXc.png)

## 課程
### DFS VS. BFS 
![](https://i.imgur.com/gPqpwpO.png)

從兩者的步驟可以看到兩者概念很像，DFS就是很直接挑一邊的走道底再回頭找，使用 stack 的結構。而 BFS 則是先以最接近的那一層開始，也就是他一走到某個節點時他就會把該點附近沒走過的節點都進入Qeuee。
- DFS: 以一邊優先
- BFS: 以階層關係優先

![](https://i.imgur.com/KDLXUCc.png)

### 課堂練習
![](https://i.imgur.com/jZSCB6o.png)

route: G->E->F->A->D->B->C
## Applications of Depth First Search
Depth-first search (DFS) is an algorithm (or technique) for traversing a graph.
Following are the problems that use DFS as a building block.

1) For an unweighted graph, DFS traversal of the graph produces the minimum spanning tree and all pair shortest path tree.

2) Detecting cycle in a graph
A graph has cycle if and only if we see a back edge during DFS. So we can run DFS for the graph and check for back edges. (See this for details)

3) Path Finding
We can specialize the DFS algorithm to find a path between two given vertices u and z.
i) Call DFS(G, u) with u as the start vertex.
ii) Use a stack S to keep track of the path between the start vertex and the current vertex.
iii) As soon as destination vertex z is encountered, return the path as the
contents of the stack

See this for details.

4) Topological Sorting
Topological Sorting is mainly used for scheduling jobs from the given dependencies among jobs. In computer science, applications of this type arise in instruction scheduling, ordering of formula cell evaluation when recomputing formula values in spreadsheets, logic synthesis, determining the order of compilation tasks to perform in makefiles, data serialization, and resolving symbol dependencies in linkers [2].

5) To test if a graph is bipartite
We can augment either BFS or DFS when we first discover a new vertex, color it opposited its parents, and for each other edge, check it doesn’t link two vertices of the same color. The first vertex in any connected component can be red or black! See this for details.

6) Finding Strongly Connected Components of a graph A directed graph is called strongly connected if there is a path from each vertex in the graph to every other vertex. (See this for DFS based algo for finding Strongly Connected Components)

7) Solving puzzles with only one solution, such as mazes. (DFS can be adapted to find all solutions to a maze by only including nodes on the current path in the visited set.)
## 參考資料
- [Graph: Depth-First Search(DFS，深度優先搜尋)
Posted by Chiu CC on 2 11, 2016](http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)
- [youtube | Graph DFS Pseudo Code with Animation](https://www.youtube.com/watch?v=GFlthbUd7LQ&feature=youtu.be)
- [youtube | Depth First Traversal for a Graph | GeeksforGeeks](https://youtu.be/Y40bRyPQQr0)
- [youtube | Applications of Depth First Search | GeeksforGeeks](https://youtu.be/dE3wBxYobrU)
