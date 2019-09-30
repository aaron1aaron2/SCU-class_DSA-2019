# kc house data
###### tags: `kaggle` `data science` `linear regression` `multiple regression`
> kaggle: https://www.kaggle.com/shivachandel/kc-house-data

---
## 關於這個資料集
kchouse 是一家在線房地產公司，使用機器學習技術對房屋進行估價。本篇報告旨在使用多元線性回歸（MLR）預測美國 [華盛頓州金縣] 的房屋銷售額。

* 該數據集由2014年5月至2015年5月之間售出的房屋的歷史數據組成。
* 該數據集包含美國**華盛頓州金縣**的房價，該數據還涵蓋西雅圖。
* 該數據集由 **21個變量** 和 **21613個觀測值** 所組成。

## 欄位說明
|column name|中文解釋|description|
|-|-|-|
|date |日期|Date house was sold(String)
|price|價格| Price of the sold house
|bedrooms|臥房數| Numer of Bedrooms
|bathrooms|浴室數| Numer of bathrooms
|sqft_living|客廳大小| Square footage of the living room
|sqrt_log|計程儀平方英尺| Square footage of the log
|floors|樓層數| Total floors in the house
|waterfront|是否為濱水區(0、1)| Whether the house has a view a waterfront(1: yes, 0: not)
|view|-|unknown
|condtion|屋況|Condition of the house
|grade|評分(無依據)|unknown
|sqft_above|房屋面積(不包括地下室)|Square footage of house apart from basement
|sqft_basement|地下室的面積|Square footage of the basement
|yr_built|建造年份(西元)|Built year
|yr_renovated|整修年份(西元)| Year when the house was renovated
|zipcode|郵遞區號|zipcode of the house
|lat|緯度|Latitude coordinate
|long|經度|Longitude coordinate
|sqft_living15|2015年客廳面積(含部分整修)|Living room area in 2015(implies some renovations)
|sqrt_lot15|2015 土地面積(水平面積)|Lot area in 2015(implies some renovations)
