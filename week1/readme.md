# 第一次接觸 github 
> 這邊主要介紹github 的基本使技巧，git 的部分不會深入，對 git 有興趣的人可以[去這裡](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)

## 什麼是 github ?
您可能聽說過GitHub是代碼共享和發布服務，或者它是工程師的社交網站。
兩種說法都是正確的，但是GitHub 真正厲害的是...


> GitHub 的核心 Git 

這是一個由 Linux 創造者 Linus Torvalds 啟動的開源項目。 Git與其他版本控制系統一樣，管理和存儲項目的修訂。 
儘管它主要用途是管理程式代碼，但Git可用於管理任何其他類型的文件，所以可以將其視為所有文檔的歸檔系統。

## 個人頁面
![](https://i.imgur.com/1TUxAJF.png)

- 黃色的部分: 可以編輯個人檔案

- 藍色的部分: 顯示紅色部分對應的頁面

- 紅色的部分: 有七個按鈕
  - **Overview**: 你最受歡迎的 repository(包含fork的)、活躍度、近期的動作
  
  - **Repository**: 這邊可以看到所有你的 Repository，還有一年內的活躍度。也可以創建新的 Repository >>> <img src='https://i.imgur.com/H1zpxTS.png' weight='50' height='20'>
  
  - **Projects**: 每個 Repository 都可以建立自己的 Project，Project 可以規劃專案、排序任務、追蹤任務狀態、分享狀態等等，採用看板的方式顯示，和 trello 的相似度頗高，除了本身的功能以外，Project 的卡片和 Github Issue 的功能之間也有很高的密切度，細節功能十分完善，接下來我們就一一來介紹。
詳細操作>>> [點這邊](https://ithelp.ithome.com.tw/articles/10205003?sc=iThelpR)

  - **Package**: GitHub Package Registry是一個軟件包託管服務，類似於 npmjs.org，rubygems.org或hub.docker.com，可讓您將軟件包和代碼託管在一個地方。
您可以私下或公開託管軟件包，並將其用作為項目中的依賴項。 使用方式>>> [點這邊](https://help.github.com/en/articles/about-github-package-registry)

  - **Star**: 當你覺得別人的 Repository 做的很棒，你可以給他星星。這邊會顯示你給過星星的 Repository。>>> 給自己也沒問題喔~
  
  - **Followers**: 你的粉絲...
  
  - **Following**: 你的偶像...

## 建立你自己的 Repository
### Step 1: New Repository
> 點擊 Repository -> New

![](https://i.imgur.com/w2rIny7.png) 
> 填寫 `Repository name` ，作為之後的網址和 Repository 的名稱。下面 `README` 要勾。最後點擊 `Create repository.`

![](https://i.imgur.com/quzPcWp.png)

### Step 2: 建立 Readme.md
> Readme.md 是一個 markdown 的格式。在 Repository 下每個頁面(資料夾) ，github會直接將 readme.md的檔 顯示在檔案的底下，也就是說它是一個說明檔，說明你當前的頁面在做甚麼?
* 主要由 markdown 構成
* 可使用部分 html 語法
### 簡單的  markdown 語法
#### >>> 標頭
> 語法
```  
# H1
## H2
### H3
#### H4
```
> 結果

# H1
## H2
### H3
#### H4

---

#### >>> 列點
> 語法
```  
* abc
  * abc
  * abc
- abc
  - abc
  - abc
```
> 結果

* abc
  * abc
  * abc
- abc
  - abc
  - abc
  
---

#### >>> 超連結
> 語法
```  
[我的github](https://github.com/aaron1aaron2/my-learning-note/)
```
> 結果

[我的github](https://github.com/aaron1aaron2/my-learning-note/)

---

#### >>> 圖片
> 語法1
```  
![](https://github.com/aaron1aaron2/my-learning-note/blob/master/image/bear.jpg)
```
> 結果

![](https://github.com/aaron1aaron2/my-learning-note/blob/master/image/bear.jpg)

> 語法2 -html，可調整大小。 (注意: 在 markdown 穿插使用html語法最好後面空一行，不然會跑版)
```  
<img src='https://github.com/aaron1aaron2/my-learning-note/blob/master/image/bear.jpg' height=200 weight =200>
```
> 結果 

<img src='https://github.com/aaron1aaron2/my-learning-note/blob/master/image/bear.jpg' height=200 weight =200>


---

#### >>> 斜體字
> 語法
```  
*abc*
```
> 結果

*abc*

---

#### >>> 粗體字
> 語法
```  
**abc**
```
> 結果

**abc**

---

#### >>> 引用
> 語法
```  
> abc
>> abc
```
> 結果

> abc
>> abc

#### >>> 程式碼
> 語法1
```
`abc`
```
> 結果

`abc`
> 語法2

![](https://i.imgur.com/Dc5KPOR.png)

> 結果

```
abc
```

### Step 3: 建立資料夾

### Step 4: 上傳檔案

## 參考網站
* https:/'guides.github.com/activities/hello-world/
* https://techcrunch.com/2012/07/14/what-exactly-is-github-anyway/
* https://ithelp.ithome.com.tw/articles/10205003?sc=iThelpR
* https://help.github.com/en/articles/about-github-package-registry
