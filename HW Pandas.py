
# coding: utf-8

# In[1]:


get_ipython().system('pwd')


# In[2]:


get_ipython().run_line_magic('cd', '../')


# In[3]:


get_ipython().system('pwd')


# In[6]:


get_ipython().run_line_magic('cd', 'HeroesOfPymoli')


# In[100]:


get_ipython().system('ls')


# In[1]:


import pandas as pd
import numpy as np
from pandas import DataFrame


# In[2]:


heroes=pd.read_json('purchase_data.json')


# In[3]:


heroes.head()


# # Statistics for Heroes dataset

# In[4]:


heroes.describe()


# # Player Count

# In[5]:


playercount= len(heroes[heroes['SN']!=None]['SN'].unique())
print ("Player count = ",playercount)


# In[6]:


len(heroes[heroes['Gender']=='Male']['SN'].unique())


# In[7]:


DataFrame(heroes[['Gender','Price']]).groupby('Gender')['Price'].mean()


# In[8]:


DataFrame(heroes[['Gender','Price']]).groupby('Gender')['Price'].mean()


# In[9]:


heroes['Age'].max()


# In[10]:


agebins=[0,4,8,12,16,20,24,28,32,36,40,44,48]
agegroups=['0 - 4','5 - 8','9 - 12','13 - 16','17 - 20','21 - 24','25 - 28','29 - 32','33 - 36','37 - 40','41 - 44','45 -48']


# In[11]:


heroes['AgeBin']=pd.cut(heroes['Age'],bins=agebins,labels=agegroups)


# In[12]:


DataFrame(heroes[['AgeBin','Price']].groupby(['AgeBin'])['Price'].count())


# In[13]:


DataFrame(heroes[['AgeBin','Price']].groupby(['AgeBin'])['Price'].mean())


# In[14]:


DataFrame(heroes[['AgeBin','Price']].groupby(['AgeBin'])['Price'].sum())


# In[15]:


DataFrame(heroes[['AgeBin','Price']].groupby(['AgeBin'])['Price'].count())


# In[16]:


len(heroes[heroes['SN']!=None]['SN'].unique())


# # Price Analysis by Gender
# 

# In[23]:


TotalPurchaseAmountByGender = DataFrame(heroes[['Gender','Price']].groupby(['Gender'])['Price'].sum())
TotalPurchaseAmountByGender


# In[24]:


TotalPurchaseCountByGender = DataFrame(heroes[['Gender','Price']].groupby(['Gender'])['Price'].count())
TotalPurchaseCountByGender


# In[25]:


AvgPurchaseAmounttByGender = DataFrame(heroes[['Gender','Price']].groupby(['Gender'])['Price'].mean())
AvgPurchaseAmounttByGender


# In[56]:


top5spenders_Total=DataFrame(heroes[['SN','Price']].groupby(['SN'])['Price'].sum()).reset_index().sort_values('Price',ascending=False).head(5)


# In[81]:


DataFrame(heroes[['SN','Price']].groupby(['SN'])['Price'].sum()).reset_index().sort_values('Price',ascending=False).head(5)


# In[72]:


top5spender_dict={}
for cust in top5spenders_Total['SN']:
    avg = heroes[heroes['SN']==cust]['Price'].mean()
    count = heroes[heroes['SN']==cust]['Price'].count()
    total = heroes[heroes['SN']==cust]['Price'].sum()
    
    top5spender_dict[cust]=(total,count,avg)

top5Spendors_Report = DataFrame(DataFrame(top5spender_dict).T)


# In[74]:


top5Spendors_Report.columns=['Total Purchase Amt','Total Count of Items','Average Purcahse Amount']


# In[77]:


top5Spendors_Report.sort_values('Total Purchase Amt',ascending=False)


# In[82]:


top5spender_dict


# In[49]:


top5spenders = df__.sort_values('Price',ascending=False).head(5)


# In[51]:


top5spenders['SN']


# In[26]:


heroes.head()


# ## Identify	the	5	most	popular	items	by	purchase	count,	then	list	(in a	table): Item	ID Item	Name Purchase	Count Item	Price Total	Purchase	Value
# 
# 

# #### Total Purchase Value is assumed to be the product of Price and Count of Purchases

# In[93]:


MostPopItem = DataFrame(heroes[['Item ID','SN', 'Item Name', 'Price']].groupby(['Item ID', 'Item Name', 'Price'])['SN'].count()).reset_index().sort_values('SN', ascending = False).head(5)
MostPopItem.columns = ['Item ID', 'Item Name', 'Price', 'Total Items']
MostPopItem['Total Purcahse Value']=MostPopItem['Price']*MostPopItem['Total Items']
MostPopItem


# In[105]:


MostProfItem = DataFrame(heroes[['Item ID','SN', 'Item Name', 'Price']].groupby(['Item ID', 'Item Name', 'Price'])['SN'].count()).reset_index().sort_values('SN', ascending = False)
MostProfItem.columns = ['Item ID', 'Item Name', 'Price', 'Total Items']
MostProfItem['Total Purchase Value'] = MostProfItem['Price']*MostProfItem['Total Items']
MostProfItem


# In[109]:


MostProfitable5 = MostProfItem.sort_values('Total Purchase Value', ascending = False).head(5)
MostProfitable5

