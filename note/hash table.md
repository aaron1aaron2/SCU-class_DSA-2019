# Hash table
###### tags: `演算法` `資料結構`
## Hash table
hash table 是一個資料結構，用來儲存一對 keys & value 。他使用 hash function 將 key 轉換成 array 對應的位置(index) 。而該位置就是用來儲存 value 的。
使用的 hash function 好壞是 hash table 關鍵。 在一般情況下，hash table 搜尋特定的物件的時間複雜度平均為 O(1).


![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/473px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)

將特定字串轉換得到特定編號，並存到對應位置的資料結構，hash table 由下列三者組成：

- keys
  - 作為獨立的索引，通常為字串，也就是應用端輸入的東西。
- hash function
  - 通過某些算式或是方法，將 keys 轉換成能對應特定的 index 的。
  - 他的設計理念是一個key會有對應的且獨立的 bucket，但是目前大多數的設計都會有碰撞問題，也就是不同的 keys 經過轉換後會對應到一樣的 bucket。
- bucket
  - 他是一個 array ，有多個位置可以儲存資料，在裡面可以是空的可以存一筆資料，甚至也可以放其它資料結構，例如：linked-list

## hashing
hashing 他是一種在一群體中，辨識特定物件的技術，再現實生活中:
1. 在學校裡，每位學生都有特定的編號，這編號可以用來查詢他的相關資料。
2. 在圖書館裡，每本書都有一個特別編號，紀錄與該書本相關的資訊，像是類別、借還書資料 之類的...

上述兩種情況都會需要有特別編碼(unique number)。簡單來講就是他是一個將 key 轉成 index 的工作。而要如何用程式去實現呢? 我們把輸入值(str)當作 key ，然後透過 MD5 的 hexdigest() 將字串轉換成 16 進位的格式，在透過 hash function 轉換成對應的 index 。

> 最簡單的方式就是直接取餘數作為 index
```python=
hash = hashfunc(key)
index = hash % array_size
```
## Hash function
hash function 可以把不規則的資料(像是字串)轉成特定index(在有限的 array_size 下) 然後會存入 hash table。從 hash function 出來的值稱作 hash values、hash codes、hash sums 或是 simply hashes。

一個好的 hashing 機制 ，需要一個好的 hash function ，他有以下幾個特點

- easy to computing (很好計算): 他不是一個複雜的演算法，必須能夠簡單快速的轉換。

- Uniform distribution (均勻分布): 他必須均勻分布，不要只偏向某格群體(index)，這樣會影響 hash table 的效率.

- Less collisions (少碰撞):碰撞就是有兩個 key 會對應到同個 hash value(index)，這是要避免的。

> Note: 幾乎所有 hash function 都會有碰撞(Collision)問題，所以在做 hash table 時要注意如果發生碰撞要如何處理。
## Collision Handling
![](https://he-s3.s3.amazonaws.com/media/uploads/2cabd32.jpg)


因為 array（容量） 不是無限的， 所以我們要在有限的空間裡，存取特定值。也就是 在我們的 hash table 裡會有 array_size(capacity)，用來限制 array 的大小，那如果不同的字串對應同個 index 依樣怎麼辦?? 也就是同個 key 在hashing 時有衝突(Collision) ，這時就可以使用 linked-List 也就是在hash table 裡面放 linked-List，只要 index 一樣我們就可以把 value 一直往後堆疊在透過在節點裡設置對應的另一個 key 作為辨識，但是當我們的 array_size 太小就會像是 linked-List 了。

![](https://he-s3.s3.amazonaws.com/media/uploads/0e2c706.png)

- Chaining: 將 hash table 的每個位置插入 linked-List ，但是他會使用更多而外的記憶體。
- Open Addressing: 所有物件都存在 hash table 中，也就是不管有幾個物件，每個都直接指派一個 空 index 去存取(key,value)。(類似 python 裡的 dict)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/HASHTB12.svg/543px-HASHTB12.svg.png)
## MD5 Hash
This hash function accepts sequence of bytes and returns 128 bit hash value, usually used to check data integrity but has security issues.

Functions associated :
* encode() : Converts the string into bytes to be acceptable by hash function.
* digest() : Returns the encoded data in byte format.
* hexdigest() : Returns the encoded data in hexadecimal format.

## Applications

- Associative arrays(關聯陣列): 
    - Hash tables are commonly used to implement many types of in-memory tables. They are used to implement associative arrays (arrays whose indices are arbitrary strings or other complicated objects).
        
- Database indexing(資料庫索引): 
    - Hash tables may also be used as disk-based data structures and database indices (such as in dbm).

- Caches(快取記憶體): 
    - Hash tables can be used to implement caches i.e. auxiliary data tables that are used to speed up the access to data, which is primarily stored in slower media.
    
- Object representation(實現物件導向): 
    - Several dynamic languages, such as Perl, Python, JavaScript, and Ruby use hash tables to implement objects.
    
- algorithms(演算法): Hash Functions are used in various algorithms to make their computing faster

### 關聯陣列
- 在電腦科學中，關聯陣列（英語：Associative Array），又稱對映（Map）、字典（Dictionary）是一個抽象的資料結構，它包含著類似於（鍵，值）的有序對。一個關聯陣列中的有序對可以重複也可以不重複。 這種資料結構包含以下幾種常見的操作：
    
    - 字典問題是設計一種能夠具備關聯陣列特性的資料結構。解決字典問題的常用方法，是利用散列表，但有些情況下，也可以直接使用二叉查詢樹或其他結構。
    - 許多程序設計語言內建基本的資料型別，提供對關聯陣列的支援。而Content-addressable memory則是硬體層面上實現對關聯陣列的支援。

### 資料庫索引
是資料庫管理系統中一個排序的資料結構，以協助快速查詢、更新資料庫表中資料。索引鍵值的邏輯順序與索引所服務的表中相應行的物理順序相同的索引，被稱為聚集索引，反之為非聚集索引，索引一般使用二叉樹排序索引鍵值的，聚集索引的索引值是直接指向資料表對應元組的，而非聚集索引的索引值仍會指向下一個索引資料塊，並不直接指向元組，因為還有一層索引進行重定向，所以非聚集索引可以擁有不同的鍵值排序而擁有多個不同的索引。而聚集索引因為與表的元組物理順序一一對應，所以只有一種排序，即一個數據表只有一個聚集索引。

## 參考網站
- [Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- [geeksforgeeks | md5-hash-python](https://www.geeksforgeeks.org/md5-hash-python/)
- [geeksforgeeks | hashing-set-1-introduction](https://www.geeksforgeeks.org/hashing-set-1-introduction/)
- [Python 計算 MD5 與 SHA 雜湊教學與範例](https://blog.gtwang.org/programming/python-md5-sha-hash-functions-tutorial-examples/)
- [hackerearth | Basics of Hash Tables](https://www.hackerearth.com/zh/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)
