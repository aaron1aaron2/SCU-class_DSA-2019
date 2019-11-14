# Set
###### tags: `演算法` `資料結構`
## 維基百科定義
在數學定義上，它是集合論的研究物件，指具有某種特定性質的事物的母體，「一堆東西」集合裡的事物東西叫作元素。數字 2、4和 6 在單獨考慮時是不同的對象，但是當將它們放一起時，會形成的大小為3的單個集合- {2,4,6}。

## 特性
* Set集合裡沒有重複元素
* Set集合是無序集合

## 基本操作
* 插入
* 刪除
* Set 是否為空
* Set 是否包含某個元素
* Set 元素個數
## 在 python 裡的基本操作
```python=
a = {1,2,3}
b = {2,5,6}

a&b # 交集:{2}

a|b # 聯集:{1, 2, 3, 5, 6}

a-b # 差集:{1, 3}

2 in a # True
2 not in a # False
```
## 其他符號
|python 符號|意思|
|:-:|:-|
|---|差集|
|&|交集|
|I|聯集|
|!=|不等於|
|==|等於|
|in|屬於|
|not in|不屬於|

## 資料來源
* [wiki](https://en.wikipedia.org/wiki/Set_(mathematics))
* http://www2.csie.ntnu.edu.tw/~u91029/Set.html
* https://codertw.com/%e7%a8%8b%e5%bc%8f%e8%aa%9e%e8%a8%80/425189/

# 練習
## Set Mismatch
> 題目: [Leetcode | Set Mismatch](https://leetcode.com/problems/set-mismatch/)

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

### Example
* Input: nums = [1,2,2,4] 
* Output: [2,3]

### key point

* 正常的 set: [1,2,3,4]
* 異常的 set: [1,2,2,4]
* 讓上面兩者比對，輸出 [2,3] --> [重複值,缺失值]
