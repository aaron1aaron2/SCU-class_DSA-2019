# Merge sort VS. Heap sort 
###### tags: `演算法`
## 我的想法
- heap sort: 簡單來說，他從頭到尾都是在原本的 array 上做動作，也就是 in-place 。這就是為什麼大家會覺得它比較複雜，雖然看起來都是在 heap 上面做比較和交換，但是它實際上是在原本的 array 上做動作，heap 只是是否交換的依據而已。所以我覺得 heap sort 在概念上是比較複雜的。但是在了解它的做法和原裡後，實做起來就很簡單，基本上就是重複 max(min) heap 和換 root 這兩個步驟，過程中 heap 會持續邊小，值到剩下一個元素。 
- merge sort: 它的概念很簡單，就是一直切到只剩下一個時，兩個唯一組開始比較合併，也就是它是先把小的 array 整理好後再去跟其他 array 整理。到下一層時，因為兩個 array 都整理過了，所以在做比較排序時就會比較容易(只需比較頭)。在實作上我就不太順利了，因為想起來很簡單但是做起來不容易。我覺得主要是遞迴的部分卡的蠻久的，尤其是它由左至右，和等待的部分，反正就是整個程式運作的順序問題。


## 從速度上來看
在所有 sort 裡面時間複雜度，同樣是 O(log n) 有 merge sort 、Heap sort 和 quick sort，也就是目前 O(log n) 已經是最快的排序方式了，雖然他們的時間複雜度都一樣，但是他們實際上的速度在不同條件下還是有差:
- **Quick sort**: 他狀況好的時候最快，但是他很不穩定，因為他會隨著 pivot 定的位置有關，如果 pivot 接近極值時就會很差，但是在大多情況下他是最快的。
- **merge sort**: 他在處理大的 array 時，在速度上會比 heap sort 好。
- **Heap sort**: 速度是三這中最差的。

## 從空間上來看
- **merge sort**: 需要多一個 array 的空間，來處理資料。
- **Heap sort**: 屬於 in-place ，不需要而外的空間。

## 從做法上
- **Heap sort**:
此方法會根據數據的特性去隨機遍歷，局部性較差。當你在重複製造 max heap 和 min heap 的同時會多次移動和交換，造成許多不必要的動作，但是也是因為這樣才不用用到而外的空間。

- **merge sort:**
因為它每次的遍歷都是依造順序，所以是有局部性的。也就是它會先將一部分的 array 排好，在依序跟其它 array 排序，這樣的話當你原本的為排序 array 沒有到很亂的話，它可以省下許多動作。而且它不需要使用交換，因為交換會用到兩次的讀取和兩次的寫入，而在 maerge sort 裡，在比較排序 element 的階段，只需要一次的讀取與寫入。

## 總結

在排序上，merge sort 較適合已經預排序的數據，而 Heap sort 和 Quick sort 較適合對未排序的數據。

## 參考網站
- https://stackoverflow.com/questions/53269004/heap-sort-vs-merge-sort-in-speed
- http://www-cs-students.stanford.edu/~rashmi/projects/Sorting.pdf
- https://www.quora.com/What-are-the-differences-among-quick-heap-and-merge-sort-and-which-one-is-best-Why
- https://medium.com/cracking-the-data-science-interview/heap-sort-merge-sort-and-convex-hull-4cd108ae3ed4