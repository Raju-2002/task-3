#!/usr/bin/env python
# coding: utf-8

# ### task
# - take input from the user
# - check the lenght of the string even or odd
# - if the string length is odd access one middle charecter
# - if the string length is even access two middle charecters

# In[1]:


s = input("ENTER YOUR STRING ")
if len(s)%2==0:
    print("middle letters of the given string is : ")
    print(s[(len(s)//2)-1],s[len(s)//2])
else:
    print("middle letter of given string is : ",s[len(s)//2])


# In[ ]:




