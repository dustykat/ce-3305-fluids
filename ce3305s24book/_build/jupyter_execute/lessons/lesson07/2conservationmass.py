#!/usr/bin/env python
# coding: utf-8

# ### CV Relationships for Mass Conservation (Continunity)
# 
# To use CV analysis the system equations are converted to volume variation relations.
# 
# Recall that extensive properties are defined throughout an entire mass of a fluid (a system) whereas intensive properties are an amount of property per unit mass.
# 
# Starting with mass itself, the extensive property is mass $m$
# 
# The mass per unit mass is unity; $\frac{m}{m}=1$
# 
# The mass per unit volume is density; $\frac{m}{V}=\rho$
# 
# <!--
# The fundamental relationship of the system is:
# 
# $B_{sys} = \int \beta dm = \int \beta \rho dV$ -->
# 
# In the case of mass we have
# 
# ```{figure} rtt-mass.png
# ---
# width: 600px
# name: rtt-mass
# ---
# 
# ```
# Now consider a system (gold cube in the figure at time $t=t_0$
# 
# 
# ```{figure} rtt-mass-t0.png
# ---
# width: 600px
# name: rtt-mass-t0
# ---
# 
# ```
# 
# A short time ($t+\Delta t$) later the system has moved, some parts have left the CV.
# 
# 
# ```{figure} rtt-mass-tdt.png
# ---
# width: 600px
# name: rtt-mass-tdt
# ---
# 
# ```
# 
# Examination of the three zones and the system total mass gives:
# 
# 
# ```{figure} rtt-mass-tdt-1.png
# ---
# width: 600px
# name: rtt-mass-tdt-1
# ---
# 
# ```
# 
# Inserting these into the system to volume expression:
# 
# ```{figure} rtt-mass-tdt-2.png
# ---
# width: 600px
# name: rtt-mass-tdt-2
# ---
# 
# ```
# 
# Now using the divergence theroem to cope with the terms in Parts I and III of space in the drawing
# 
# ```{figure} divergence.png
# ---
# width: 600px
# name: divergence
# ---
# 
# ```
#  The application of Gauss' divergence theorem produces the "flux integrals".
# 
# ```{figure} divergence-2.png
# ---
# width: 600px
# name: divergence-2
# ---
# 
# ```
# 
# Now examine the relationship between velocity and area in the flux integrals
# 
# ```{figure} vdotDA.png
# ---
# width: 600px
# name: vdotDA
# ---
# 
# ```
# 
# Collect the terms together into the Reynolds Transport Expression for Mass
# 
# ```{figure} RTT-MassBalance.png
# ---
# width: 600px
# name: RTT-MassBalance
# ---
# 
# ```
# 
# To summarize:
#  
# 
# ```{figure} rtt-summary.png
# ---
# width: 600px
# name: rtt-summary
# ---
# 
# ```

# ## Example 1: Application of Continunity to a Holy Grail
# 
# > Actually our just a vessel with a hole in the bottom; a grail, with a hole in the bottom is the holey grail!
# 
# ```{figure} example-1.png
# ---
# width: 600px
# name: example-1
# ---
# 
# ```

# In[1]:


# problem statement - above Yay!


# In[2]:


# sketch


# In[3]:


# known
V_in = 7 # m/s
A_in = 0.0025 # m^2
Q_out = 0.003 #m^3/s
# rho = 1000 # kg/m3
# grabity = 9.8 # m/s/s

# change in storage
dSdt = V_in*A_in - Q_out
print('storage accumulation is .... wait for it ...',dSdt)


# ## References
# 
# 1. [Reynolds Transport Theorem (Wikipedia)](https://en.wikipedia.org/wiki/Reynolds_transport_theorem#:~:text=Reynolds%20transport%20theorem%20can%20be,(not%20the%20flow%20velocity).)

# In[ ]:




