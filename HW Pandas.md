

```python
!pwd
```

    /c/Users/isabe/Desktop/UCSD201801DATA5-Class-Repository-DATA/02-Homework/04-Numpy-Pandas/HeroesOfPymoli
    


```python
%cd ../

```

    C:\Users\isabe\Desktop\UCSD201801DATA5-Class-Repository-DATA\02-Homework\04-Numpy-Pandas
    


```python
!pwd
```

    /c/Users/isabe/Desktop/UCSD201801DATA5-Class-Repository-DATA/02-Homework/04-Numpy-Pandas
    


```python
%cd HeroesOfPymoli
```

    C:\Users\isabe\Desktop\UCSD201801DATA5-Class-Repository-DATA\02-Homework\04-Numpy-Pandas\HeroesOfPymoli
    


```python
!ls
```

    HeroesOfPymoli_Example.pdf
    HW Pandas.ipynb
    purchase_data.json
    


```python
import pandas as pd
import numpy as np
from pandas import DataFrame
```


```python
heroes=pd.read_json('purchase_data.json')
```


```python
heroes.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>



# Statistics for Heroes dataset


```python
heroes.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Item ID</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>780.000000</td>
      <td>780.000000</td>
      <td>780.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>22.729487</td>
      <td>91.293590</td>
      <td>2.931192</td>
    </tr>
    <tr>
      <th>std</th>
      <td>6.930604</td>
      <td>52.707537</td>
      <td>1.115780</td>
    </tr>
    <tr>
      <th>min</th>
      <td>7.000000</td>
      <td>0.000000</td>
      <td>1.030000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>19.000000</td>
      <td>44.000000</td>
      <td>1.960000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>22.000000</td>
      <td>91.000000</td>
      <td>2.880000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>25.000000</td>
      <td>135.000000</td>
      <td>3.910000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>45.000000</td>
      <td>183.000000</td>
      <td>4.950000</td>
    </tr>
  </tbody>
</table>
</div>



# Player Count


```python
playercount= len(heroes[heroes['SN']!=None]['SN'].unique())
print ("Player count = ",playercount)
```

    Player count =  573
    


```python
len(heroes[heroes['Gender']=='Male']['SN'].unique())
```




    465




```python
DataFrame(heroes[['Gender','Price']]).groupby('Gender')['Price'].mean()
```




    Gender
    Female                   2.815515
    Male                     2.950521
    Other / Non-Disclosed    3.249091
    Name: Price, dtype: float64




```python
DataFrame(heroes[['Gender','Price']]).groupby('Gender')['Price'].mean()
```




    Gender
    Female                   2.815515
    Male                     2.950521
    Other / Non-Disclosed    3.249091
    Name: Price, dtype: float64




```python
heroes['Age'].max()
```




    45




```python
agebins=[0,4,8,12,16,20,24,28,32,36,40,44,48]
agegroups=['0 - 4','5 - 8','9 - 12','13 - 16','17 - 20','21 - 24','25 - 28','29 - 32','33 - 36','37 - 40','41 - 44','45 -48']
```


```python
heroes['AgeBin']=pd.cut(heroes['Age'],bins=agebins,labels=agegroups)
```


```python
DataFrame(heroes[['AgeBin','Price']].groupby(['AgeBin'])['Price'].count())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>AgeBin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0 - 4</th>
      <td>0</td>
    </tr>
    <tr>
      <th>5 - 8</th>
      <td>22</td>
    </tr>
    <tr>
      <th>9 - 12</th>
      <td>24</td>
    </tr>
    <tr>
      <th>13 - 16</th>
      <td>87</td>
    </tr>
    <tr>
      <th>17 - 20</th>
      <td>161</td>
    </tr>
    <tr>
      <th>21 - 24</th>
      <td>238</td>
    </tr>
    <tr>
      <th>25 - 28</th>
      <td>104</td>
    </tr>
    <tr>
      <th>29 - 32</th>
      <td>66</td>
    </tr>
    <tr>
      <th>33 - 36</th>
      <td>38</td>
    </tr>
    <tr>
      <th>37 - 40</th>
      <td>37</td>
    </tr>
    <tr>
      <th>41 - 44</th>
      <td>2</td>
    </tr>
    <tr>
      <th>45 -48</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
DataFrame(heroes[['AgeBin','Price']].groupby(['AgeBin'])['Price'].mean())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>AgeBin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0 - 4</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5 - 8</th>
      <td>2.788182</td>
    </tr>
    <tr>
      <th>9 - 12</th>
      <td>3.385417</td>
    </tr>
    <tr>
      <th>13 - 16</th>
      <td>2.745862</td>
    </tr>
    <tr>
      <th>17 - 20</th>
      <td>2.907019</td>
    </tr>
    <tr>
      <th>21 - 24</th>
      <td>2.924748</td>
    </tr>
    <tr>
      <th>25 - 28</th>
      <td>2.974712</td>
    </tr>
    <tr>
      <th>29 - 32</th>
      <td>3.061970</td>
    </tr>
    <tr>
      <th>33 - 36</th>
      <td>2.981053</td>
    </tr>
    <tr>
      <th>37 - 40</th>
      <td>2.901351</td>
    </tr>
    <tr>
      <th>41 - 44</th>
      <td>2.960000</td>
    </tr>
    <tr>
      <th>45 -48</th>
      <td>2.720000</td>
    </tr>
  </tbody>
</table>
</div>




```python
DataFrame(heroes[['AgeBin','Price']].groupby(['AgeBin'])['Price'].sum())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>AgeBin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0 - 4</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>5 - 8</th>
      <td>61.34</td>
    </tr>
    <tr>
      <th>9 - 12</th>
      <td>81.25</td>
    </tr>
    <tr>
      <th>13 - 16</th>
      <td>238.89</td>
    </tr>
    <tr>
      <th>17 - 20</th>
      <td>468.03</td>
    </tr>
    <tr>
      <th>21 - 24</th>
      <td>696.09</td>
    </tr>
    <tr>
      <th>25 - 28</th>
      <td>309.37</td>
    </tr>
    <tr>
      <th>29 - 32</th>
      <td>202.09</td>
    </tr>
    <tr>
      <th>33 - 36</th>
      <td>113.28</td>
    </tr>
    <tr>
      <th>37 - 40</th>
      <td>107.35</td>
    </tr>
    <tr>
      <th>41 - 44</th>
      <td>5.92</td>
    </tr>
    <tr>
      <th>45 -48</th>
      <td>2.72</td>
    </tr>
  </tbody>
</table>
</div>




```python
DataFrame(heroes[['AgeBin','Price']].groupby(['AgeBin'])['Price'].count())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>AgeBin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0 - 4</th>
      <td>0</td>
    </tr>
    <tr>
      <th>5 - 8</th>
      <td>22</td>
    </tr>
    <tr>
      <th>9 - 12</th>
      <td>24</td>
    </tr>
    <tr>
      <th>13 - 16</th>
      <td>87</td>
    </tr>
    <tr>
      <th>17 - 20</th>
      <td>161</td>
    </tr>
    <tr>
      <th>21 - 24</th>
      <td>238</td>
    </tr>
    <tr>
      <th>25 - 28</th>
      <td>104</td>
    </tr>
    <tr>
      <th>29 - 32</th>
      <td>66</td>
    </tr>
    <tr>
      <th>33 - 36</th>
      <td>38</td>
    </tr>
    <tr>
      <th>37 - 40</th>
      <td>37</td>
    </tr>
    <tr>
      <th>41 - 44</th>
      <td>2</td>
    </tr>
    <tr>
      <th>45 -48</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
len(heroes[heroes['SN']!=None]['SN'].unique())
```




    573



# Price Analysis by Gender



```python
TotalPurchaseAmountByGender = DataFrame(heroes[['Gender','Price']].groupby(['Gender'])['Price'].sum())
TotalPurchaseAmountByGender
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
TotalPurchaseCountByGender = DataFrame(heroes[['Gender','Price']].groupby(['Gender'])['Price'].count())
TotalPurchaseCountByGender
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
AvgPurchaseAmounttByGender = DataFrame(heroes[['Gender','Price']].groupby(['Gender'])['Price'].mean())
AvgPurchaseAmounttByGender
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>2.815515</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>2.950521</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>3.249091</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5spenders_Total=DataFrame(heroes[['SN','Price']].groupby(['SN'])['Price'].sum()).reset_index().sort_values('Price',ascending=False).head(5)
```


```python
DataFrame(heroes[['SN','Price']].groupby(['SN'])['Price'].sum()).reset_index().sort_values('Price',ascending=False).head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>538</th>
      <td>Undirrala66</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Saedue76</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>354</th>
      <td>Mindimnya67</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>181</th>
      <td>Haellysu29</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Eoda93</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5spender_dict={}
for cust in top5spenders_Total['SN']:
    avg = heroes[heroes['SN']==cust]['Price'].mean()
    count = heroes[heroes['SN']==cust]['Price'].count()
    total = heroes[heroes['SN']==cust]['Price'].sum()
    
    top5spender_dict[cust]=(total,count,avg)

top5Spendors_Report = DataFrame(DataFrame(top5spender_dict).T)
```


```python
top5Spendors_Report.columns=['Total Purchase Amt','Total Count of Items','Average Purcahse Amount']
```


```python
top5Spendors_Report.sort_values('Total Purchase Amt',ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Amt</th>
      <th>Total Count of Items</th>
      <th>Average Purcahse Amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>17.06</td>
      <td>5.0</td>
      <td>3.412000</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>13.56</td>
      <td>4.0</td>
      <td>3.390000</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>12.74</td>
      <td>4.0</td>
      <td>3.185000</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>12.73</td>
      <td>3.0</td>
      <td>4.243333</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>11.58</td>
      <td>3.0</td>
      <td>3.860000</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5spender_dict
```




    {'Eoda93': (11.58, 3, 3.86),
     'Haellysu29': (12.73, 3, 4.243333333333333),
     'Mindimnya67': (12.739999999999998, 4, 3.1849999999999996),
     'Saedue76': (13.56, 4, 3.39),
     'Undirrala66': (17.06, 5, 3.412)}




```python
top5spenders = df__.sort_values('Price',ascending=False).head(5)
```


```python
top5spenders['SN']
```




    538    Undirrala66
    428       Saedue76
    354    Mindimnya67
    181     Haellysu29
    120         Eoda93
    Name: SN, dtype: object




```python
heroes.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>AgeBin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>37 - 40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>21 - 24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>33 - 36</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>21 - 24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>21 - 24</td>
    </tr>
  </tbody>
</table>
</div>



## Identify	the	5	most	popular	items	by	purchase	count,	then	list	(in a	table): Item	ID Item	Name Purchase	Count Item	Price Total	Purchase	Value



#### Total Purchase Value is assumed to be the product of Price and Count of Purchases


```python
MostPopItem = DataFrame(heroes[['Item ID','SN', 'Item Name', 'Price']].groupby(['Item ID', 'Item Name', 'Price'])['SN'].count()).reset_index().sort_values('SN', ascending = False).head(5)
MostPopItem.columns = ['Item ID', 'Item Name', 'Price', 'Total Items']
MostPopItem['Total Purcahse Value']=MostPopItem['Price']*MostPopItem['Total Items']
MostPopItem
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>Total Items</th>
      <th>Total Purcahse Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
      <td>11</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>11</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <td>31</td>
      <td>Trickster</td>
      <td>2.07</td>
      <td>9</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>174</th>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>9</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>Serenity</td>
      <td>1.49</td>
      <td>9</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
MostProfItem = DataFrame(heroes[['Item ID','SN', 'Item Name', 'Price']].groupby(['Item ID', 'Item Name', 'Price'])['SN'].count()).reset_index().sort_values('SN', ascending = False)
MostProfItem.columns = ['Item ID', 'Item Name', 'Price', 'Total Items']
MostProfItem['Total Purchase Value'] = MostProfItem['Price']*MostProfItem['Total Items']
MostProfItem

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>Total Items</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
      <td>11</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>11</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <td>31</td>
      <td>Trickster</td>
      <td>2.07</td>
      <td>9</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>174</th>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>9</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>Serenity</td>
      <td>1.49</td>
      <td>9</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>34</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>65</th>
      <td>65</td>
      <td>Conqueror Adamantite Mace</td>
      <td>1.96</td>
      <td>8</td>
      <td>15.68</td>
    </tr>
    <tr>
      <th>151</th>
      <td>152</td>
      <td>Darkheart</td>
      <td>3.15</td>
      <td>8</td>
      <td>25.20</td>
    </tr>
    <tr>
      <th>44</th>
      <td>44</td>
      <td>Bonecarvin Battle Axe</td>
      <td>2.46</td>
      <td>8</td>
      <td>19.68</td>
    </tr>
    <tr>
      <th>107</th>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>3.61</td>
      <td>8</td>
      <td>28.88</td>
    </tr>
    <tr>
      <th>106</th>
      <td>106</td>
      <td>Crying Steel Sickle</td>
      <td>2.29</td>
      <td>8</td>
      <td>18.32</td>
    </tr>
    <tr>
      <th>92</th>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>8</td>
      <td>10.88</td>
    </tr>
    <tr>
      <th>157</th>
      <td>158</td>
      <td>Darkheart, Butcher of the Champion</td>
      <td>3.56</td>
      <td>7</td>
      <td>24.92</td>
    </tr>
    <tr>
      <th>115</th>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>4.25</td>
      <td>7</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>108</th>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>3.39</td>
      <td>7</td>
      <td>23.73</td>
    </tr>
    <tr>
      <th>66</th>
      <td>66</td>
      <td>Victor Iron Spikes</td>
      <td>3.55</td>
      <td>7</td>
      <td>24.85</td>
    </tr>
    <tr>
      <th>79</th>
      <td>79</td>
      <td>Alpha, Oath of Zeal</td>
      <td>2.88</td>
      <td>7</td>
      <td>20.16</td>
    </tr>
    <tr>
      <th>153</th>
      <td>154</td>
      <td>Feral Katana</td>
      <td>2.19</td>
      <td>7</td>
      <td>15.33</td>
    </tr>
    <tr>
      <th>130</th>
      <td>130</td>
      <td>Alpha</td>
      <td>1.56</td>
      <td>7</td>
      <td>10.92</td>
    </tr>
    <tr>
      <th>171</th>
      <td>172</td>
      <td>Blade of the Grave</td>
      <td>1.69</td>
      <td>7</td>
      <td>11.83</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>Torchlight, Bond of Storms</td>
      <td>1.77</td>
      <td>7</td>
      <td>12.39</td>
    </tr>
    <tr>
      <th>178</th>
      <td>179</td>
      <td>Wolf, Promise of the Moonwalker</td>
      <td>1.88</td>
      <td>7</td>
      <td>13.16</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>Brimstone</td>
      <td>2.52</td>
      <td>7</td>
      <td>17.64</td>
    </tr>
    <tr>
      <th>91</th>
      <td>91</td>
      <td>Celeste</td>
      <td>3.71</td>
      <td>6</td>
      <td>22.26</td>
    </tr>
    <tr>
      <th>103</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>4.87</td>
      <td>6</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>47</th>
      <td>47</td>
      <td>Alpha, Reach of Ending Hope</td>
      <td>1.55</td>
      <td>6</td>
      <td>9.30</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Thorn, Satchel of Dark Souls</td>
      <td>4.51</td>
      <td>6</td>
      <td>27.06</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Purgatory, Gem of Regret</td>
      <td>3.91</td>
      <td>6</td>
      <td>23.46</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>6</td>
      <td>10.38</td>
    </tr>
    <tr>
      <th>85</th>
      <td>85</td>
      <td>Malificent Bag</td>
      <td>2.17</td>
      <td>6</td>
      <td>13.02</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>116</th>
      <td>116</td>
      <td>Renewed Skeletal Katana</td>
      <td>2.37</td>
      <td>2</td>
      <td>4.74</td>
    </tr>
    <tr>
      <th>96</th>
      <td>96</td>
      <td>Blood-Forged Skeletal Spine</td>
      <td>4.77</td>
      <td>2</td>
      <td>9.54</td>
    </tr>
    <tr>
      <th>177</th>
      <td>178</td>
      <td>Oathbreaker, Last Hope of the Breaking Storm</td>
      <td>2.41</td>
      <td>2</td>
      <td>4.82</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19</td>
      <td>Pursuit, Cudgel of Necromancy</td>
      <td>3.98</td>
      <td>2</td>
      <td>7.96</td>
    </tr>
    <tr>
      <th>62</th>
      <td>62</td>
      <td>Piece Maker</td>
      <td>4.36</td>
      <td>2</td>
      <td>8.72</td>
    </tr>
    <tr>
      <th>55</th>
      <td>55</td>
      <td>Vindictive Glass Edge</td>
      <td>4.26</td>
      <td>2</td>
      <td>8.52</td>
    </tr>
    <tr>
      <th>24</th>
      <td>24</td>
      <td>Warped Fetish</td>
      <td>2.41</td>
      <td>2</td>
      <td>4.82</td>
    </tr>
    <tr>
      <th>80</th>
      <td>80</td>
      <td>Dreamsong</td>
      <td>3.81</td>
      <td>2</td>
      <td>7.62</td>
    </tr>
    <tr>
      <th>149</th>
      <td>150</td>
      <td>Deathraze</td>
      <td>4.54</td>
      <td>2</td>
      <td>9.08</td>
    </tr>
    <tr>
      <th>148</th>
      <td>149</td>
      <td>Tranquility, Razor of Black Magic</td>
      <td>2.47</td>
      <td>2</td>
      <td>4.94</td>
    </tr>
    <tr>
      <th>58</th>
      <td>58</td>
      <td>Freak's Bite, Favor of Holy Might</td>
      <td>3.03</td>
      <td>2</td>
      <td>6.06</td>
    </tr>
    <tr>
      <th>145</th>
      <td>146</td>
      <td>Warped Iron Scimitar</td>
      <td>4.08</td>
      <td>2</td>
      <td>8.16</td>
    </tr>
    <tr>
      <th>64</th>
      <td>64</td>
      <td>Fusion Pummel</td>
      <td>3.58</td>
      <td>2</td>
      <td>7.16</td>
    </tr>
    <tr>
      <th>132</th>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>2</td>
      <td>7.80</td>
    </tr>
    <tr>
      <th>56</th>
      <td>56</td>
      <td>Foul Titanium Battle Axe</td>
      <td>4.33</td>
      <td>2</td>
      <td>8.66</td>
    </tr>
    <tr>
      <th>89</th>
      <td>89</td>
      <td>Blazefury, Protector of Delusions</td>
      <td>1.50</td>
      <td>2</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>155</th>
      <td>156</td>
      <td>Soul-Forged Steel Shortsword</td>
      <td>1.16</td>
      <td>1</td>
      <td>1.16</td>
    </tr>
    <tr>
      <th>109</th>
      <td>109</td>
      <td>Downfall, Scalpel Of The Emperor</td>
      <td>3.20</td>
      <td>1</td>
      <td>3.20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Verdict</td>
      <td>3.40</td>
      <td>1</td>
      <td>3.40</td>
    </tr>
    <tr>
      <th>136</th>
      <td>136</td>
      <td>Ghastly Adamantite Protector</td>
      <td>3.30</td>
      <td>1</td>
      <td>3.30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>1</td>
      <td>1.79</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bloodlord's Fetish</td>
      <td>2.28</td>
      <td>1</td>
      <td>2.28</td>
    </tr>
    <tr>
      <th>126</th>
      <td>126</td>
      <td>Exiled Mithril Longsword</td>
      <td>3.25</td>
      <td>1</td>
      <td>3.25</td>
    </tr>
    <tr>
      <th>43</th>
      <td>43</td>
      <td>Foul Edge</td>
      <td>2.38</td>
      <td>1</td>
      <td>2.38</td>
    </tr>
    <tr>
      <th>28</th>
      <td>28</td>
      <td>Flux, Destroyer of Due Diligence</td>
      <td>3.04</td>
      <td>1</td>
      <td>3.04</td>
    </tr>
    <tr>
      <th>146</th>
      <td>147</td>
      <td>Hellreaver, Heirloom of Inception</td>
      <td>3.59</td>
      <td>1</td>
      <td>3.59</td>
    </tr>
    <tr>
      <th>167</th>
      <td>168</td>
      <td>Sun Strike, Jaws of Twisted Visions</td>
      <td>2.64</td>
      <td>1</td>
      <td>2.64</td>
    </tr>
    <tr>
      <th>163</th>
      <td>164</td>
      <td>Exiled Doomblade</td>
      <td>1.92</td>
      <td>1</td>
      <td>1.92</td>
    </tr>
    <tr>
      <th>59</th>
      <td>59</td>
      <td>Lightning, Etcher of the King</td>
      <td>1.65</td>
      <td>1</td>
      <td>1.65</td>
    </tr>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Splinter</td>
      <td>1.82</td>
      <td>1</td>
      <td>1.82</td>
    </tr>
  </tbody>
</table>
<p>183 rows × 5 columns</p>
</div>




```python
MostProfitable5 = MostProfItem.sort_values('Total Purchase Value', ascending = False).head(5)
MostProfitable5

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>Total Items</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>4.25</td>
      <td>7</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
      <td>6</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>4.87</td>
      <td>6</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>3.61</td>
      <td>8</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>


