#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv ('/Users/tiago/Desktop/python/search.csv') #ind the saved .csv in the python folder, 
                                        #hold down option key while right-clicking on flie to get the full path name
print (df)
df.describe()
list(df.columns)


# In[10]:


import matplotlib.pyplot as plt
annotations = df['Planet_Name']
plt.plot(df['Transit_Duration'])
#for i, label in enumerate(annotations):
   
   # plt.annotate (label, (i,df['Transit_Duration'][i]))


# #info for the columns above:
# SNR_Emission_15_micron',
#  'SNR_Emission_5_micron',
#  'SNR_Transmission_K_mag',
#  'Rp', - planet radius
#  'Mp',- planet mass
#  'Tday', - dayside temp
#  'Teq', - planet equilibrium temp
#  'log10g_p',- planet gravity
#  'Period', - rotation time (d)
#  'Transit_Duration', duration of being infront of host star
#  'K_mag', k band mag
#  'Distance', distance to host star
#  'Teff', - stellar temp
#  'log10g_s',- stellar gravity
#  'Transit_Flag', idk
#  'Catalog_Name']

# In[22]:



x = df['Mp']
y = df['Rp']
plt.scatter(x,y)
plt.xlabel('mass relative to jupiter')
plt.ylabel('radius relative to jupiter')


# In[ ]:




