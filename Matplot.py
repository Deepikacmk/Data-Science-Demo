#!/usr/bin/env python
# coding: utf-8

# In[41]:


from matplotlib import pyplot as plt


# In[42]:


plt.plot([1,2,3],[4,5,1])
plt.title('Sample')
plt.ylabel('y Axis')
plt.xlabel('x-axis')
plt.show()


# # Adding Style to plot
# 

# In[43]:


from matplotlib import style


# In[44]:


style.use=('ggplot')


# In[45]:


x=[5,8,10]
y=[12,16,6]
x2=[6,9,11]
y2=[6,15,7]


# In[46]:


plt.plot(x,y,'g',label='line1' ,linewidth=6)
plt.plot(x2,y2,'c',label='line2 ',linewidth=5)
plt.title("sample graph")
plt.xlabel("xaxis")
plt.ylabel("yaxis")
plt.legend()
plt.grid(True,color='k')
plt.show()


#  # Bar Chart

# In[47]:




from matplotlib import pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2],label="icecream")
plt.bar([2,4,6,8,10],[8,6,2,5,6],label="cake",color='g')
plt.legend()
plt.title('food')
plt.show()


# 

# In[ ]:





# In[ ]:





# In[ ]:




