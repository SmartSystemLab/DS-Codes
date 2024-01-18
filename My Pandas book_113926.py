#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import pandas as pd 


# In[4]:


from numpy.random import randn


# In[5]:


np.random.seed(101)


# In[6]:


indexes = ['F','G','H','J','K']
coolumns = ['T','U','W']


# In[7]:


df = pd.DataFrame(randn(5,3), indexes, coolumns)


# In[8]:


df


# In[9]:


df['New'] = df['W']+df['U']


# In[10]:


df['New']


# In[11]:


df


# In[12]:


df.drop('W', axis =1)


# In[13]:


df


# In[14]:


df.shape


# In[15]:


df


# In[16]:


df.loc['H':'J']['W']


# In[20]:


df.iloc[1:4][2:]


# In[118]:


df


# In[140]:


df[df['W']>0]


# In[150]:


df[df['W']>0][['T','U']]


# In[151]:


df[df['W']>0]


# In[153]:


df[df['U']>1]


# In[163]:


df[(df['W']>0) | (df['U']>1)]


# In[162]:


df[df['W'] < 0]


# In[164]:


df['States'] = 'CA WY NY OR CO'.split()


# In[166]:


df


# In[49]:


outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[50]:


hier_index


# In[64]:


df = pd.DataFrame(np.random.randn(6,2),hier_index,['A','B'])


# In[65]:


df


# In[69]:


df.loc['G1'].iloc[2]


# In[71]:


df.index.names = ['Groups', 'Num']


# In[72]:


df


# In[84]:



df.loc['G2', 2]['A']


# In[83]:


df.xs(1, level = 'Num')


# In[91]:


outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[103]:


df = pd.DataFrame((['z', 'i'], ['a', 'j'], ['b', 'v'], ['y', 'u'], ['x', 's'], ['w', 't']), index = hier_index, columns = ['X', 'Y'])


# In[110]:


df


# In[114]:


df.index.names = ['Groups', 'Numbers']


# In[115]:


df


# In[116]:


df.xs(1, level = 'Numbers')


# In[117]:


df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C':[3,4,6]})


# In[127]:


df


# In[122]:


df.dropna(axis = 1)


# In[126]:


df['A'].fillna(value = df['A'].mean(), inplace = True,)


# In[128]:


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[129]:


df = pd.DataFrame(data)


# In[147]:


df.groupby('Company').describe().transpose()


# In[149]:


df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])


# In[150]:


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])


# In[164]:


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 


# In[165]:


df1


# In[166]:



df2


# In[167]:


df3 


# In[168]:


pd.concat([df1, df2, df3])


# In[172]:


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})    


# In[173]:


pd.merge(left, right, how = 'inner', on = 'key')


# In[177]:


left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})


# In[179]:


left


# In[180]:


right


# In[176]:


pd.merge(left, right, on=['key1', 'key2'])


# In[181]:


left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])


# In[182]:


left


# In[193]:


right


# In[202]:


left.join(right, how = 'right')


# In[209]:


right.join(left, how = 'left')


# In[210]:


conda install sqlalchemy


# In[212]:


get_ipython().system('conda install lxml')


# In[213]:


get_ipython().system('conda install html5lib')


# In[214]:


get_ipython().system('conda install sqlalchemy')


# In[216]:


get_ipython().system('conda install BeautifulSoup4')


# In[220]:


pwd


# In[225]:


df = pd.read_csv('example.csv')


# In[226]:


df


# In[233]:


df.to_csv('My_Output', index = False)


# In[234]:


pd.read_csv('My_Output')


# ##### We set index to false so that the index in the dataset isn't read as a separate column.

# In[246]:


df = pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')


# In[250]:


df


# In[244]:


del df['Unnamed: 0']


# In[245]:


df


# In[260]:


df = pd.read_csv('example.csv')


# In[264]:


df.to_csv('First_output', index = False)


# In[273]:


pd.read_csv('First_output')


# In[289]:


pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')


# In[291]:


pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1', index_col=0)


# In[293]:


df.to_excel('Excel_Sample.xlsx', sheet_name = 'Sheet2')


# In[294]:


data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')


# In[299]:


pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet2', index_col = 0)


# In[301]:


from sqlalchemy import create_engine


# In[302]:


engine = create_engine('sqlite:///:memory:')


# In[307]:


df.to_sql('her_table', engine)


# In[308]:


sqldf = pd.read_sql('her_table', con = engine)


# In[309]:


sqldf


# In[ ]:




