#!/usr/bin/env python
# coding: utf-8

# # Drag and Lift
# 
# :::{admonition} Course Website
# [http://54.243.252.9/ce-3305-webroot/](http://54.243.252.9/ce-3305-webroot/)
# :::

# ## Readings
# 
# 1. [DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013.  ](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-22.pdf)
# 1. [Cleveland, T. G. (2015) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019): Drag and Lift *, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture018.pdf)
# 
# 

# ## Videos

# ## Lesson Outline

# In[ ]:





# In[ ]:





# ## Stoke-em Law

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




