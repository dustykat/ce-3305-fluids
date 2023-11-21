#!/usr/bin/env python
# coding: utf-8

# # Stoke-em Law

# In[1]:


import math
rhos = 6000 #kg/m^3
rhoo = 850 # kg/m^3
gee = 9.8
dsp = 0.012
Cd = 5.0
muo = 0.1
velocity = math.sqrt(  ((rhos*gee-rhoo*gee)*(4/3)*dsp)/(Cd*rhoo))
print(velocity)
re=velocity*dsp/muo
print(re)


# In[ ]:




