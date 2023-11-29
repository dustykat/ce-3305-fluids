#!/usr/bin/env python
# coding: utf-8

# ## Example 1: Application of Angular Momentum to a Reaction Turbine
# 
# Application of angular momentum often involves use of continunity and energy (bernoulli's equation).  Selection of CV is important to make analysis straightforward.  Consider the following example involving a reaction turbine (like a Rain-Bird)
# 
# ![](https://5.imimg.com/data5/RX/YB/MY-710552/x-500x500.jpeg)
# 
# The problem statement is depicted in {numref}`angular-ex1-1`
# 
# ```{figure} angular-ex1-1.png
# ---
# width: 600px
# name: angular-ex1-1
# ---
# Caption
# ```
# 
# Apply continunity as in {numref}`angular-ex1-2`
# 
# ```{figure} angular-ex1-2.png
# ---
# width: 600px
# name: angular-ex1-2
# ---
# Caption
# ```
# 
# Then momentum as in {numref}`angular-ex1-3`
# 
# ```{figure} angular-ex1-3.png
# ---
# width: 600px
# name: angular-ex1-3
# ---
# Caption
# ```
# 
# Continue the analysis (break the CV into upper and lower arm, use symmetry to cancel the volume integrals) as in {numref}`angular-ex1-4`
# 
# 
# ```{figure} angular-ex1-4.png
# ---
# width: 600px
# name: angular-ex1-4
# ---
# Caption
# ```
# 
# Complete the analysis as in {numref}`angular-ex1-5`
# 
# ```{figure} angular-ex1-5.png
# ---
# width: 600px
# name: angular-ex1-5
# ---
# Caption
# ```
# 
# now apply ENGR-1330 to perform the calculations.

# In[1]:


# computational thinning
import math
q = 0.1 #discharge
v_jet = 50.0
omega = 500*2*math.pi/60
radius = 0.5
rho = 1000.0
power = rho*q*v_jet*radius*omega - rho*q*omega**2*radius**2
print("Power ",round(power,2)," Newton-meters/sec    ")


# ## Example 2: Application of Angular Momentum to a Reaction Turbine
# 
# Here we will do the same problem, but using a fixed reference frame CV
# 
# ```{figure} angular-ex2-1.png
# ---
# width: 600px
# name: angular-ex2-1
# ---
# Caption
# ```
# {numref}`angular-ex1-5` is analysis of the volume integral in a vector representation of the moment of momentum
# 
# ```{figure} angular-ex2-2.png
# ---
# width: 600px
# name: angular-ex2-2
# ---
# Caption
# ```
# {numref}`angular-ex1-5` is analysis of the flux integrals in a vector representation of the moment of momentum
# After the equations are constructed, the analysys proceedes the same as in the earlier example.
