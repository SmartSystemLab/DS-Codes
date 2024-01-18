#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = 40
name = 'Jane'


# In[3]:


print(f'My name is {name} and I am {num} years old.')


# In[4]:


s = 'hello'


# In[17]:


s[-5]


# In[6]:


s[0]


# In[7]:


s[:-2]


# In[8]:


s[:]


# In[11]:


d = {'k': [1,4,5,6,7]}


# In[13]:


d['k'][0]


# In[20]:


if False:
    print("Yep!")
else:
    print("Dang!")


# In[19]:


if True:
    print("Nope!")


# In[21]:


def cube(v):
    return v**3


# In[22]:


cube(6)


# In[23]:


range(10)


# In[25]:


list(range(10))


# In[84]:


def times2(num):
    return num * 2
def times3(num1):
    return num1 * 3


# In[85]:


seq = [1,2,3,4,5]
lane = [3,4,5,6,6]


# In[109]:


double = list(map(times2, seq))


# In[110]:


triple = list(map(times3, lane))


# In[111]:


double, triple


# In[91]:


list(map(times3, seq, lane))


# In[ ]:





# In[62]:


list(map(times2, lane))


# In[115]:


t = lambda num: num * 2


# In[116]:


t(87)


# In[120]:


list(map(lambda num:num * 4, [6, 8, 10, 12, 12]))


# In[126]:


t = 'Hello, my name is #Tanya'


# In[122]:


t.upper()


# In[123]:


t.capitalize()


# In[128]:


t.split('#')


# In[129]:


t.split('T')


# In[130]:


x = [(1,2), (3,4), (5,6)]


# In[137]:


liste = x.pop()
print(liste)
print(x)
    


# In[136]:


print(item)


# In[138]:


conda install numpy


# In[139]:


pip install numpy


# In[1]:


get_ipython().system('pip install numpy')


# In[2]:


get_ipython().system('conda install numpy')


# In[3]:


get_ipython().system('conda install numpy')
get_ipython().system('pip install numpy')


# In[4]:


get_ipython().system('conda install numpy')


# In[5]:


$ conda update -n base -c defaults conda


# In[ ]:




