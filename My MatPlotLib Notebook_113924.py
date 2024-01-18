#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


import numpy as np
x = np.linspace(0,5,11)
y = x ** 2


# In[5]:


x


# In[6]:


y


# In[11]:


plt.plot(x, y)
plt.xlabel('Label for X')
plt.ylabel('Label for Y')
plt.title('Overall Title')


# In[17]:


plt.subplot(1, 2, 1)
plt.plot(x, y, 'b-')

plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')


# In[29]:


fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x,y)


# In[47]:


fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x,y)
axes1.set_title('Larger Plot')

axes2.plot(y,x)
axes2.set_title('Smaller Plot')


# In[66]:


fig, axes = plt.subplots(nrows = 1, ncols = 2)

axes[0].plot(x,y)
axes[1].plot(y,x)
axes[1].set_xlabel('Checking')


# In[70]:


fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (8,2))

axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()


# In[75]:


fig.savefig('my_picture.tiff')


# In[80]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2, label='X squared')
ax.plot(x, x**3, label='X cubed')
ax.legend(loc=0)


# In[89]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.plot(x, y, color = 'gray')


# In[91]:


fig, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x+1, color="red", linewidth=0.25)
ax.plot(x, x+2, color="red", linewidth=0.50)
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="green", lw=3, linestyle='-')
ax.plot(x, x+6, color="green", lw=3, ls='-.')
ax.plot(x, x+7, color="green", lw=3, ls=':')

# custom dash
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10]) # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
ax.plot(x, x+12, color="blue", lw=3, ls='-', marker='1')

# marker size and color
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green");


# In[ ]:




