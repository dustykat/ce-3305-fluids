#!/usr/bin/env python
# coding: utf-8

# # Pressure Forces, Bouyancy, Stability
# 
# ## Lesson Outline
# 1. Forces on Submerged Objects 
# 2. Bouyancy 
# 3. Stability

# ### Examples
# 
# Below are some example applications of the force and line-of-action expressions of the previous lesson.
# 
# #### Example 1: Concrete retaining wall form specification
# 
# Assuming that concrete behaves as a liquid ($\gamma = 150\frac{lbf}{ft^3}$) just after placement, determine the force per foot of length exherted on a form by the concrete if it is poured into forms for a wall that is to be 9 feet tall.  
# 
# ```{figure} wall-setup.png
# ---
# width: 500px
# name: wall-setup
# ---
# Concrete retaining wall form design
# ```
# If the forms are held in place as shown in {numref}`wall-setup`, with ties between vertical braces spaced every 2 feet, what force is exherted on the bottom tie?
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
# 
# ##### State the problem
# 
# Essentially same as above, but there is some simplification in {numref}`pr-state`
# 
# ```{figure} pr-state.png
# ---
# width: 300px
# name: pr-state
# ---
# Concrete retaining wall form design, problem statement
# ```
# ##### Sketch the situation
# 
# A sketch of one side of the form is shown in {numref}`wall-side`
# 
# ```{figure} wall-side.png
# ---
# width: 300px
# name: wall-side
# ---
# Concrete retaining wall FBD and force identification.
# ```
# Using the sketch as a guide our known quantities are the dimensions, the specific weight of concrete as a liquid.
# 
# ##### Identify (list) unknown quantities
# The unknown quantities are the resultant force (the equivalent point load) $F_R$. per unit length.
# 
# ##### Identify (list) governing principles
# - hydrostatic equation of a liquid
# - centroid of a rectangle (to find magnitude of the pressure force)
# - centroid of a triangle (to find point of application in the pressure prism
# - moment balance to find how force is resisted by the ties
# 
# ##### Solve for the unknowns
# 
# ```{figure} unknowns-1.png
# ---
# width: 600px
# name: unknowns-1
# ---
# Solve for pressure force per unit length (foot of wall)
# ```
# {numref}`unknowns-1` shows the analysis and solution for pressure force and line of application for each foot of wall.
# 
# ```{figure} unknowns-2.png
# ---
# width: 600px
# name: unknowns-2
# ---
# Solve for load distribution in upper and lower ties per unit length (foot of wall)
# ```
# {numref}`unknowns-2` shows the analysis and solution for load distribution in the ties for each foot of wall. Each tie pair must support 2-feet of wall (except for the end pairs) which gives the end result of 8100 lbs for the lower ties.  Using this value we can decide what size rods to use as ties.  For example 
# - [1/4 all-thread tensile strength](https://www.google.com/search?client=firefox-b-1-d&q=What+is+the+tensile+strength+of+1/4+threaded+rod%3F&sa=X&ved=2ahUKEwin-YjDlLf1AhVfl2oFHRmHDI0Qzmd6BAgdEAU&biw=1063&bih=882&dpr=1) has an upper limit strength of 150000 psi, so we multiply by the rod cross sectional area to see if it is strong enough.
# - [1/2 all-thread tensile strength](https://www.google.com/search?q=What+is+the+tensile+strength+of+1%2F2+threaded+rod%3F&client=firefox-b-1-d&biw=1063&bih=882&ei=1obkYbjvD_qzqtsP8dSo0Aw&ved=0ahUKEwi4ssvTlLf1AhX6mWoFHXEqCsoQ4dUDCA0&uact=5&oq=What+is+the+tensile+strength+of+1%2F2+threaded+rod%3F&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEB4yBQgAEIYDMgUIABCGAzoHCAAQRxCwA0oECEEYAEoECEYYAFD_BVj_BWDlD2gBcAJ4AIABR4gBR5IBATGYAQCgAQHIAQjAAQE&sclient=gws-wiz)
# has an upper limit strength of 60000 psi, so we multiply by the rod cross sectional area to see if it is strong enough.
# 
# The scripts to compute the strength are below; 1/4-inch is suitable for the upper ties; 1/2-inch is plenty strong for the lower ties.

# In[1]:


import math
tensile = 150000 #psi
diameter = 0.25 #inches
area = 0.25*math.pi*diameter**2 #area in inches
force = tensile*area
print('1/4 inch tie rod strength = ', round(force,3), 'lbs')


# In[2]:


import math
tensile = 60000 #psi
diameter = 0.50 #inches
area = 0.25*math.pi*diameter**2 #area in inches
force = tensile*area
print('1/2 inch tie rod strength = ', round(force,3), 'lbs')


# ### Forces on Submarged Objects
# 
# The integral methods will always work, but an easier approach for common geometries is a projection of volumes approach.
# 
# ```{figure} fd-4.1.png
# ---
# width: 300px
# name: fd-4.1
# ---
# Force diagram submerged plate
# ```
# 
# The idea is that the distributed force as depicted in {numref}`fd-4.1` is equivalent to the vertical and horizontal component forces depicted in {numref}`fd-4.2`.  The horizontal component is found using the hydrostatic equation applied to the projection of the object onto a vertical plane.
# 
# ```{figure} fd-4.2.png
# ---
# width: 300px
# name: fd-4.2
# ---
# Resultant forces by displacement
# ```
# 
# The vertical component is found as the weight of the volume of liquid above the object.

# In[ ]:





# In[ ]:





# ### Will it float?
# 
# [Will it float?](https://www.google.com/search?client=firefox-b-1-d&q=will+it+float) was a popular TV sgement on Late Night with David Letterman.  We can use these bouyancy principles to answer the question for most things (not nearly as fun as the TV show's way to answer the question).
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
# #### State the problem
# 
# ```{figure} will-it-float-setup.png
# ---
# width: 400px
# name: will-it-float-setup
# ---
# Cube floating in water; problem statement
# ```
# 
# #### Sketch and list knowns
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
# #### Unknowns
# 
# Draft of the block ($d$ in the drawing)
# 
# #### Governing Principles
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
# #### Validate/Discuss
# 
# Now you can do "will it float" on your own, so if there is ever a revival of the sketch you can win serious prizes!
# 
# This kind of computation is vital in near shore vessel (boat) operations to prevent running aground.  It also plays a role in offshore oil platforms in controlling their stability in rough seas.
# 
# 

# In[ ]:





# 
# ## Readings
# 
# 1. CE-3305-2022-1 Syllabus. [http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html](http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html)
# 
# 2. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 3-14
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013.  (placeholder file to get links working). [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-1.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-4.pdf)
# 
# 4. Cleveland, T. G. (2014) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. [http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-004.0.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-004.0.pdf)

# In[ ]:





# ### Topic 1
# 
# ipsum lorem
# 
# #### Subtopic 
# 
# ipsum lorem
# 
# #### Subtopic
# 
# ipsum lorem
# 

# ### Topic 2
# 
# ipsum lorem
# 
# #### Subtopic 
# 
# ipsum lorem
# 
# #### Subtopic
# 
# ipsum lorem
# 

# ### Topic 3
# 
# ipsum lorem
# 
# #### Subtopic 
# 
# ipsum lorem
# 
# #### Subtopic
# 
# ipsum lorem
# 

# ## Readings
# 
# 1. [CE-3305-2022-2 (Summer2) Syllabus](http://54.243.252.9/ce-3305-webroot-su22/0-Syllabus/ce-3305-2022-1-syllabus.html)
# 
# 2. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 3-14
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013.  (placeholder file to get links working). [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-1.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-1.pdf)
# 
# 4. Cleveland, T. G. (2014) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. [http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-001.1.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-001.1.pdf)

# ## Exercises
# 
