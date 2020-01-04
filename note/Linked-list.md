# linked list
###### tags: `演算法` `資料結構`

# 課堂
<img src="https://i.imgur.com/1Qc4uHD.png"  width="600" height="180">

> 圖片擷取至: [老師PPT](https://docs.google.com/presentation/d/e/2PACX-1vTB218-EdUZ5jpNz6Uv4TOZQc37Y281v128_aRcWC6EhkTQs5bS8fh7yysmcuzb9R2QPN6_PDshFWL_/pub?start=false&loop=false&delayms=3000&slide=id.g5ff860a9a8_0_5)

## 為什麼要有 linked list?
* 可不連續的儲存在記憶體位置。
* 依使用多寡分配空間，不會有浪費的空間。
* 適合需要頻繁新增、刪除的資料
* 走訪功能
* Block Chain 應用

# 外部資料
## What is a linked list ?
<img src="https://i.imgur.com/YkJUBP7.png"  width="600" height="300">

> 圖片擷取至: [Linked List: Intro(簡介) | by Chiu CC](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)

**Linked list** (連結串列) 是一種常見的資料結構，其使用Node(節點)來記錄、表示、儲存資料(Data)，並利用每個 Node 中的 Pointer 指向下一個 Node，藉此將多個 Node 串連起來，形成 **Linked list**，並以 NULL 來代表 **Linked list** 的終點。

在這邊 Address 代表儲存位置，每個 Node 都有一個 Address，且會 Pointer 下個 Node 的 Address。所以在建構 **Linked list** 的時候，Node 的前後關系很重要。
### 線性的資料結構 (Linear data structures)

<img src="https://miro.medium.com/max/2090/1*Xokk6XOjWyIGCBujkJsCzQ.jpeg"  width="600" height="300">

> 圖片擷取至: [What’s a Linked List, Anyway? Part 1 | by Vaidehi Joshi
](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)

**linked-List 它是屬於線性的資料結構**，如上圖所示，線性的資料結構就是透過有順序的 **節點** or **元素** 所構成，可以將其比如成跳房子遊戲，我麼需要按照一定的順序去遍歷所有的節點。相反的非線性結構就不需要按照順序去遍歷。

像是 **Trees** 和 **graphs** 就是非線性資料結構，這個之後上課會教就不多講了。這時候大可能會發現 **Array** 和 **linked-List** 其實蠻像的，因為他們都屬於線性的資料結構，接著我們就來比較一下兩者的差別。

### 記憶體管理 (Memory management)
<img src="https://miro.medium.com/max/2159/1*G43FVT5xJ1n1QDKVNZUxXQ.jpeg"  width="600" height="300">

> 圖片擷取至: [What’s a Linked List, Anyway? Part 1 | by Vaidehi Joshi](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)

Ruby、JavaScript 和 Python屬於動態語言，所以我們不用花太多時間去思考，內存(記憶體)的配置。但是 **linked-List** 和 **Array** 最大的差別就是在記憶體上儲存的方式。 

#### >> **Array**
創建 Array 時，它需要一定數量的內存。如果我們需要在一個 Array 中存儲 7bytes 的東西，只能放在一個連續的塊中。因此，電腦必須在一個地方找到 7bytes 的空閒內存，也就是說有小於7 的空間不會被使用，所以就會造成浪費。
#### >> **linked-List**
另一方面，當 linked-List 誕生時，它不需要在同一個地方全部佔用 7bytes 的內存。每一個字節可以放在不同位置，需要的時候再呼叫它，也就是他們使用的內存空間可以分散在記憶體各處。

## Linked-list VS. Array 
* **Array**(陣列)
    * 優點:
        * 可以隨機訪問(random access)：也就是可以直接透過 index 對Array的資料做存取。
        * 較節省記憶體空間：因為 Linked list 需要多一個 pointer 來記錄下一個 node 的記憶體位置。
    * 缺點：
        * 新增/刪除資料很麻煩：若要在第一個位置新增資料，就需要O(N)時間把矩陣中所有元素往後移動。
        * 若資料數量時常在改變，要時常調整矩陣的大小，會花費較多時間在搬運資料。
        * 無法有效運用空間: 建立 array 時必須給他固定的範圍。
    * 適用時機:
        * 希望能夠快速存取資料。
        * 已知欲處理的資料數量，便能確認矩陣的大小。
        * 要求記憶體空間的使用越少越好。
* **Linked-list**
    * 優點：
        * 新增/刪除資料較簡單: 只要對前一個 note 調整 pointer 即可，不需要像 Array搬動其餘元素。
            * 若是在Linked list的「開頭」新增node，只要O(1)。
            * 若要刪除特定node，或者在特定位置新增node，有可能需要先執行O(N)的「搜尋」。
        * 可以有效運用空間: Linked list的資料數量可以是動態的，不像Array會有resize的問題。
    * 缺點：
        * 搜尋較費時: 因為Linked list沒有index，若要找到特定node，需要從頭開始找起，搜尋的時間複雜度為O(N)。
        * 占較多記憶體: 需要額外的記憶體空間來儲存 pointer。
    * 適用時機：
        * 無法預期資料數量時，使用Linked list就沒有resize的問題。
        * 需要頻繁地新增/刪除資料時。
        * 不需要快速查詢資料。
### 補充 
* 時間複雜度 [wiki](https://en.wikipedia.org/wiki/Time_complexity)
    * Constant time| O(1): 固定的時間，不受到資料量影響。
    * Linear time| O(N): 時間受資料量影響，呈線性增長。
    * O(log N) 時間受資料量影響，1:log(N)。

## 參考
>主要:  [Linked List: Intro(簡介) | by Chiu CC](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)
* medium:
    * [Data structures in Python, Series 1: Linked Lists | by Kojin](https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d)
    * [用python實作linked-list | by Tobby Kuo](https://medium.com/@tobby168/用python實作linked-list-524441133d4d)
    * [What’s a Linked List, Anyway? [Part 1] | by Vaidehi Joshi](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)
* video: 
    * [Introduction to Linked Lists (Data Structures & Algorithms) | byCS Dojo](https://www.youtube.com/watch?v=WwfhLC16bis)
    * [Sample Code - Introduction to Linked Lists | byCS Dojo](https://www.csdojo.io/linked) 
* problem
    * [ArrayList vs LinkedList from memory allocation perspective
](https://stackoverflow.com/questions/11564352/arraylist-vs-linkedlist-from-memory-allocation-perspective)
    * [what does O(N) mean [duplicate]](https://stackoverflow.com/questions/1909307/what-does-on-mean)

