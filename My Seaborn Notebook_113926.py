#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('conda install seaborn')


# In[3]:


import seaborn as sns


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


tips = sns.load_dataset('tips')


# In[6]:


tips.head()


# In[25]:


sns.distplot(tips['total_bill'], kde = False, bins = 30)


# In[43]:


sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex')


# In[41]:


sns.pairplot(tips, hue = 'sex', palette = 'coolwarm')


# In[7]:


sns.rugplot(tips['total_bill'])


# In[9]:


# Don't worry about understanding this code!
# It's just for the diagram below
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Create dataset
dataset = np.random.randn(25)

# Create another rugplot
sns.rugplot(dataset);

# Set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min,x_max,100)

# Set up the bandwidth, for info on this:
url = 'http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'

bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2


# Create an empty kernel list
kernel_list = []

# Plot each basis function
for data_point in dataset:
    
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    #Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)

plt.ylim(0,1)


# In[15]:


sum_of_kde = np.sum(kernel_list,axis=0)

# Plot figure
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

# Add the initial rugplot
sns.rugplot(dataset,c = 'indianred')

# Get rid of y-tick marks
plt.yticks([])

# Set title
plt.suptitle("Sum of the Basis Functions")


# ## Categorical Plots

# In[18]:


tips.head()


# In[19]:


import numpy as np


# In[23]:


sns.barplot(x = 'sex', y = 'total_bill', data = tips)


# In[24]:


sns.barplot(x = 'sex', y = 'total_bill', data = tips, estimator=np.std)


# In[27]:


sns.countplot(x = 'time', data = tips)


# In[ ]:




