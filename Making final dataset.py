#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


Dataset = pd.read_csv('D:\codes\Tea project\Tea_chloro_color_feature.csv')


# In[3]:


Dataset.describe()


# In[4]:


Dataset.head(10)


# In[5]:


#Calculating H,S,V 
#converting RGB to HSV 

def RGB_to_CSV(r,g,b):
    r,g,b=r/255,g/255,b/255
    
    mx = max(r,g,b)
    mn = min(r,g,b)
    df = mx-mn
    if mx == mn:
        h=0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
        
    v = mx*100
    
    return h,s,v


# In[47]:


row_len = len(Dataset)


# In[46]:


for i in range(row_len):
    
    


# In[19]:


#combination
#R-B/R+B
one = []
#R+G+B
two = []
#(G+B)/R
three = []
#G/R
four = []
df = Dataset
Final_Dataset = Dataset.iloc[:,:-1]


# In[20]:


#making all the combination

for ind in df.index: 
     o = ((df['mean_r'][ind]-df['mean_b'][ind])/(df['mean_r'][ind]+df['mean_b'][ind]))
     one.append(o)
        
    
Final_Dataset['(R-B/R+B)'] = one  


# In[21]:


for ind in df.index:
     t = df['mean_r'][ind] + df['mean_g'][ind] + df['mean_b'][ind]
     two.append(t)
print(two)
Final_Dataset['(R+G+B)'] = two


# In[26]:


for ind in df.index:
     th = (df['mean_g'][ind] + df['mean_b'][ind])/df['mean_r'][ind]
     three.append(th)
print(three)
Final_Dataset['(G+B)/R'] = three


# In[27]:


for ind in df.index:
     f = df['mean_g'][ind] / df['mean_r'][ind]
     four.append(f)
print(four)
Final_Dataset['(G/R)'] = four


# In[28]:


Final_Dataset.head(10)


# In[31]:


Final_Dataset.drop(['Chlorophyll value'],axis=1)


# In[32]:


Final_Dataset.to_csv('Final_Dataset.csv')


# In[ ]:




