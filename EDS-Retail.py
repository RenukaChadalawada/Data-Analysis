#!/usr/bin/env python
# coding: utf-8

# # Author: Renuka Chadalawada

# ### Technical Task 3 : Exploratory Data Analysis - Retail 
# In this task, we will perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’. As a business manager, we will try to find out the weak areas where we can work to make more profit, and what all business problems can be derived by exploring the data.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew


# ### Read the Dataset

# In[2]:


dataset=pd.read_csv(r"D:\Data sciece SP project\SampleSuperstore.csv")


# In[3]:


# can see top 5 and bottom 5 rows of dataset
dataset


# ### Checking for the data's information and type

# In[4]:


dataset.shape


# In[5]:


dataset.info()


# In[6]:


dataset.describe()


# ### Checking for any null values and duplicate data. If yes, then dropping the duplicate data.

# In[7]:


dataset.isnull().any() # Checks the missing values.


# In[8]:


dataset.duplicated().sum() # Checks the duplicated data


# In[9]:


dataset.drop_duplicates() # drops the duplicated data


# In[10]:


dataset.nunique() 


# ### Dropping irrelevant columns

# In[11]:


# Deleting the column Postal Code

dataset.drop(columns=["Postal Code"],axis=1,inplace=True)


# In[12]:


dataset.head() # loads the first five rows


# ### Checking statistical relation between the different variables

# In[13]:


# Correlation between variables
dataset.corr()


# ## Data Visualization

# In[14]:


plt.figure(figsize=(12,7))
plt.bar(dataset['Sub-Category'],dataset['Category'])
plt.title('Category vs Sub Category')
plt.xlabel('Sub-Catgory')
plt.ylabel('Category')
plt.xticks(rotation=45)
plt.show()


# In[15]:


dataset.hist(bins=30,figsize=(20,10))
plt.show()


# ###
# So, the data here is not normal as revealed by this histogram graph.

# In[16]:


# Count of total repeatable states
dataset['State'].value_counts()


# In[17]:


plt.figure(figsize=(20,12))
sns.countplot(x=dataset['State'])
plt.xticks(rotation=90)
plt.title("STATE")
plt.show()


# In[18]:


dataset["Profit"].value_counts()


# In[19]:


plt.figure(figsize=(12,7))
plt.bar(dataset['Sub-Category'],dataset['Profit'])
plt.title('Profit vs Sub Category')
plt.xlabel('Sub-Catgory')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.show()


# ## The above barchart shows the profit and loss of each and every subcategories.
# 
# Here from the graph we can visualize that "Machines" sub-category has suffered the highest amount of loss and also profit amongst all other sub-Categories (For now we can't say that what is the reason it may be because of discounts given on binders subcategory).
# Next,"Copiers" sub-category has gained highest amount of profit with no loss.There are other sub-categories too haven't faced any kind of losses but their profit margins are also low.
# Next, suffering from highest loss is machines.

# In[44]:


sns.catplot(x = 'Sub-Category', y ='Profit', data=dataset,kind ='bar',
            height =8,aspect= 2 )
plt.suptitle('Consumption Patterns in the United States', fontsize=20)
plt.show()


# In[21]:


from plotnine import *
import warnings
warnings.filterwarnings('ignore')


# In[22]:


Profit_plot = (ggplot(dataset, aes(x='Sub-Category', y='Profit', fill='Sub-Category')) + geom_col() + coord_flip()
+ scale_fill_brewer(type='div', palette="Spectral") + theme_classic() + ggtitle('Pie Chart'))

display(Profit_plot)


# In[23]:


category_shipmode=pd.crosstab(dataset["Ship Mode"],dataset["Category"])


# In[24]:


category_shipmode


# In[25]:


category_shipmode.plot(kind="bar")


# In[29]:


figsize=(15,10)
sns.pairplot(dataset,hue='Sub-Category')
plt.show


# In[30]:


flip_xlabels = theme(axis_text_x = element_text(angle=90, hjust=1),figure_size=(10,5),
                     axis_ticks_length_major=10,axis_ticks_length_minor=5)
(ggplot(dataset, aes(x='Sub-Category', fill='Sales')) + geom_bar() + facet_wrap(['Segment']) 
+ flip_xlabels +theme(axis_text_x = element_text(size=12))+ggtitle("United States Sales Segment Data"))


# ### Observations
# From the above Graph we can say that "Home Office" segment has less purchased sub-categories and in that "Tables", "Supplies", "Machines", "Copiers", "Bookcases" has the lowest sales. "Consumer" has purchased more sub-categories as compared to other segments.

# In[31]:


flip_xlabels = theme(axis_text_x = element_text(angle=90, hjust=1),figure_size=(10,5),
                     axis_ticks_length_major=10,axis_ticks_length_minor=5)
(ggplot(dataset, aes(x='Sub-Category', fill='Discount')) + geom_bar() + facet_wrap(['Segment']) 
+ flip_xlabels +theme(axis_text_x = element_text(size=12))+ggtitle("Discount on Categories From Every Segment Of United States"))


# In[32]:


flip_xlabels = theme(axis_text_x = element_text(angle=90, hjust=1),figure_size=(10,8),axis_ticks_length_major=50,
                     axis_ticks_length_minor=50)
(ggplot(dataset, aes(x='Category', fill='Sales')) + geom_bar() + theme(axis_text_x = element_text(size=10)) 
+ facet_wrap(['Region']) + flip_xlabels+ ggtitle(" United States Sales From Every Region"))


# In[33]:


plt.figure(figsize=(10,4))
sns.lineplot('Discount','Profit', data=dataset , color='y',label='Discount')
plt.legend()
plt.show()


# In[34]:


import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[35]:


state_code = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO',
              'Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID',
              'Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME',
              'Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO',
              'Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM',
              'New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR',
              'Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN',
              'Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','District of Columbia': 'WA','Washington': 'WA',
              'West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'}
dataset['state_code'] = dataset.State.apply(lambda x: state_code[x])


# In[47]:


state_data = dataset[['Sales', 'Profit', 'state_code']].groupby(['state_code']).sum()


fig = go.Figure(data=go.Choropleth(locations=state_data.index, z = state_data.Sales, locationmode = 'USA-states', 
                                   colorscale = 'blues',colorbar_title = 'Sales in USD',))

fig.update_layout(title_text = 'Total State-Wise Sales',geo_scope='usa',height=800,)

fig.show()


# ###### Now, let us analyze the sales of a few random states from each profit bracket (high profit, medium profit, low profit, low loss and high loss) and try to observe some crucial trends which might help us in increasing the sales.
# 
# We have a few questions to answer here.
# 
# What products do the most profit making states buy?
# 
# What products do the loss bearing states buy?
#                                                                                                                         `
# What product segment needs to be improved in order to drive the profits higher?

# In[37]:



def state_data_viewer(states):
    """Plots the turnover generated by different product categories and sub-categories for the list of given states.
    Args:
        states- List of all the states you want the plots for
    Returns:
        None
    """
    product_data = dataset.groupby(['State'])
    for state in states:
        data = product_data.get_group(state).groupby(['Category'])
        fig, ax = plt.subplots(1, 3, figsize = (28,5))
        fig.suptitle(state, fontsize=14)        
        ax_index = 0
        for cat in ['Furniture', 'Office Supplies', 'Technology']:
            cat_data = data.get_group(cat).groupby(['Sub-Category']).sum()
            sns.barplot(x = cat_data.Profit, y = cat_data.index, ax = ax[ax_index])
            ax[ax_index].set_ylabel(cat)
            ax_index +=1
        fig.show()


# In[38]:



states = ['California', 'Washington', 'Mississippi', 'Arizona', 'Texas']
state_data_viewer(states)


# ###### 
# From the above data visualization,we can see the states and the category where sales and profits are high or less. We can 
# improve in those states by providing discounts in prefered range so that the company and cosumer will both be in profit. Here,
# while the superstore is incurring losses by providing discounts on their products, they can't stop doing so. Most of the heavy
# discounts are during festivals, end-of-season and clearance sales which are necessary so that the store can make space in their
# warehouses for fresh stock. Also, by incurring small losses, the company gains in the future by attracting more long term 
# customers. Therefore, the small losses from discounts are an essential part of company's businesses.

# In[ ]:




