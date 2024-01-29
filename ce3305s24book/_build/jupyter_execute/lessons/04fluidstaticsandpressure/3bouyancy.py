#!/usr/bin/env python
# coding: utf-8

# # Bouyancy (pp. 85-88)
# 
# Buoyancy is the upward force exerted by a fluid on a partially or fully immersed object. In a column of liquid, pressure increases with depth as a result of the weight of the overlying liquid. Thus the pressure at the bottom of a column of liquid is greater than at the top of the column. Similarly, the pressure at the bottom of an object submerged in a liquid is greater than at the top of the object. The pressure difference results in a net upward force on the object. The magnitude of the force is proportional to the pressure difference, and (as explained by Archimedes' principle) is equivalent to the weight of the displaced fluid. 

# ## Will it float?
# 
# [Will it float?](https://www.google.com/search?client=firefox-b-1-d&q=will+it+float) was a popular TV segment on Late Night with David Letterman.  It is a direct appeal to bouyancy in terms of everyday objects, of course its purpose was entertainment. 
# 
# We can use bouyancy principles to answer the question for most things (not nearly as fun as the TV show's way to answer the question).
# 
# ## Example
# 
# Imagine a cube of material, 1-foot on each side.  Further imagine the cube has specific weight ($\gamma = 40 \frac{lbf}{ft^3}$).  The cube is placed in the "will it float" tank. The tank is filled with water.  How deep will it float (or will it sink)?
# 
# Now recall our problem protocol.
# 
# 
# 1. State the problem
# 2. Sketch the situation (sketching no matter how ugly helps organize thoughts!). Identify (list) known quantities
# 3. Identify (list) unknown quantities
# 4. Identify (list) governing principles and equations that appear relevant to the problem
# 5. Starting from one or more governing principles and the known quantities solve for the unknowns.
# 6. Validate/discuss results
# 
# ### State the problem
# 
# ```{figure} will-it-float-setup.png
# ---
# width: 400px
# name: will-it-float-setup
# ---
# Cube floating in water; problem statement
# ```
# 
# ### Sketch and list knowns
# 
# ```{figure} will-it-floatFBD.png
# ---
# width: 200px
# name: will-it-floatFBD
# ---
# Vertical force balance on the cube
# ```
# The known values are:
# 
# - $\rho g = 40 \frac{lbf}{ft^3}$
# - $V_{block} = (1ft)(1ft)(1ft) = 1 ft^3$
# 
# ### Unknowns
# 
# Draft of the block ($d$ in the drawing)
# 
# ### Governing Principles
# 
# ```{figure} will-it-float-gov-eqn.png
# ---
# width: 400px
# name: will-it-float-gov-eqn
# ---
# Governing principles (vertical force balance, and definition of bouyant force)
# ```
# 
# #### Solve for unknowns
# ```{figure} will-it-float-soln1.png
# ---
# width: 400px
# name: will-it-float-soln1
# ---
# Finding the volume displaced to make bouyant force and weight of block equal
# ```
# 
# ```{figure} will-it-float-soln2.png
# ---
# width: 400px
# name: will-it-float-soln2
# ---
# Insert numerical values and compute draft
# ```
# ### Validate/Discuss
# 
# Now you can do "will it float" on your own, so if there is ever a revival of the sketch you can win serious prizes!
# 
# This kind of computation is vital in near shore vessel (boat) operations to prevent running aground.  It also plays a role in offshore oil platforms in controlling their stability in rough seas.

# ## Videos
# 
# 1. [Bouyancy (YouTube)](https://www.youtube.com/watch?v=6UWx2LVy61g)
