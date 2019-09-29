# House Prices: Advanced Regression Techniques
> dataset : https://www.kaggle.com/c/house-prices-advanced-regression-techniques
## Dataset & problem
### 問題背景
要求購房者描述他們的夢想中的房子，他們可能不會優先想到 `地下室天花板的高度` 或 `與鐵路很近` 。
但是，這場比賽的數據集證明，上述兩個變數對價格的影響比`房間數量`或 `有白色柵欄`的影響更大。

這邊有 **79個特徵** 描述愛荷華州埃姆斯市住宅。包含各種面向，本次競賽要求您 **預測每個房屋的最終價格**。

### 目標
#### >>> 預測每間房子的售價 `SalePrice`

### 欄位描述
|column name|description|描述|
|-|-|-|
|SalePrice|the property's sale price in dollars. This is the target variable that you're trying to predict.|房屋售價(預測目標)
|MSSubClass| The building class|房屋類別(樓層數、格局、新舊)
|MSZoning| The general zoning classification|區域分類(農業區、工業區、高低密度住宅區)
|LotFrontage|Linear feet of street connected to property|直線尺(街道與土地連接的長度)
|LotArea| Lot size in square feet|坪數
|Street|Type of road access
|Alley| Type of alley access
|LotShape| General shape of property
|LandContour| Flatness of the property
|Utilities| Type of utilities available
|LotConfig| Lot configuration
|LandSlope| Slope of property
|Neighborhood| Physical locations within Ames city limits
|Condition1| Proximity to main road or railroad
|Condition2| Proximity to main road or railroad (if a second is present)
|BldgType| Type of dwelling
|HouseStyle| Style of dwelling
|OverallQual| Overall material and finish quality
|OverallCond| Overall condition rating
|YearBuilt| Original construction date
|YearRemodAdd| Remodel date
|RoofStyle| Type of roof
|RoofMatl| Roof material
|Exterior1st| Exterior covering on house
|Exterior2nd| Exterior covering on house (if more than one material)
|MasVnrType| Masonry veneer type
|MasVnrArea| Masonry veneer area in square feet
|ExterQual| Exterior material quality
|ExterCond| Present condition of the material on the exterior
|Foundation| Type of foundation
|BsmtQual| Height of the basement
|BsmtCond| General condition of the basement
|BsmtExposure| Walkout or garden level basement walls
|BsmtFinType1| Quality of basement finished area
|BsmtFinSF1| Type 1 finished square feet
|BsmtFinType2| Quality of second finished area (if present)
|BsmtFinSF2| Type 2 finished square feet
|BsmtUnfSF| Unfinished square feet of basement area
|TotalBsmtSF| Total square feet of basement area
|Heating| Type of heating
|HeatingQC| Heating quality and condition
|CentralAir| Central air conditioning
|Electrical| Electrical system
|1stFlrSF| First Floor square feet
|2ndFlrSF| Second floor square feet
|LowQualFinSF| Low quality finished square feet (all floors)
|GrLivArea| Above grade (ground) living area square feet
|BsmtFullBath| Basement full bathrooms
|BsmtHalfBath| Basement half bathrooms
|FullBath| Full bathrooms above grade
|HalfBath| Half baths above grade
|Bedroom| Number of bedrooms above basement level
|Kitchen| Number of kitchens
|KitchenQual| Kitchen quality
|TotRmsAbvGrd| Total rooms above grade (does not include bathrooms)
|Functional| Home functionality rating
|Fireplaces| Number of fireplaces
|FireplaceQu| Fireplace quality
|GarageType| Garage location
|GarageYrBlt| Year garage was built
|GarageFinish| Interior finish of the garage
|GarageCars| Size of garage in car capacity
|GarageArea| Size of garage in square feet
|GarageQual| Garage quality
|GarageCond| Garage condition
|PavedDrive| Paved driveway
|WoodDeckSF| Wood deck area in square feet
|OpenPorchSF| Open porch area in square feet
|EnclosedPorch| Enclosed porch area in square feet
|3SsnPorch| Three season porch area in square feet
|ScreenPorch| Screen porch area in square feet
|PoolArea| Pool area in square feet
|PoolQC| Pool quality
|Fence| Fence quality
|MiscFeature| Miscellaneous feature not covered in other categories
|MiscVal| $Value of miscellaneous feature
|MoSold| Month Sold
|YrSold| Year Sold
|SaleType| Type of sale
|SaleCondition| Condition of sale

# kc_house_data
> dataset : https://www.kaggle.com/shivachandel/kc-house-data
