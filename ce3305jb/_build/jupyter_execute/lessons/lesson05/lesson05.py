#!/usr/bin/env python
# coding: utf-8

# # Euler Equation
# 
# ## Lesson Outline
# - Background
# - Constant velocity; constant acceleration
# - Translation
# - Rotation

# ### Background
# 
# This lesson introduces the Euler (and Bernoulli) equations which arefundamental in applied fluid mechanics.
# 
# The lesson also examines lagrangian and eularian reference frames in the contaext of variational gonckulus as applied to fluid mechanics.  
# 
# Start with flow patterns

# #### Flow Patterns and Visualization
# 
# In real fluids, markers such as dye, smoke, heat are used to visualize how things flow.
# 
# The markers are tracers; the tracer hypothesis is that the tracer moves with the host fluid.  
# 
# > [MIT videos of different flow regimes](https://www.youtube.com/watch?v=nuQyKGuXJOs) 
# 
# Some of the patterns are:
# 
# - **Timeline** is a line formed by marking adjacent particles at some instant
# - **Pathline** is the trajectory of a particular fluid particle
# - **Streakline** is the trajectory of many particles that pass through some common point in space
# - **Streamline** is a line in a flow field that is tangent to velocity; no flow crosses a streamline (3D equivalent is called a streamtube)
# 
# In steady flow streamlines, streaklines, and pathlines are coincident.  In unsteady (time-varying) flow this relationship is not preserved (and the three patterns will look different)
# 
# ```{figure} buckner-funnel.png
# ---
# width: 400px
# name: buckner-funnel
# ---
# Flow in a tank with a holy bottom
# ```
# Consider the flow depicted in the tank above; is the flow field uniform or non-uniform?  What about the flow above the dashed line?

# Flow dimensions are classified by how many space coordinates are required to speciofy the velocity field.  All real flows are 3D, but useful results are possible with 2D and 1D approximations.
# 
# ### Velocity Field
# 
# Velocities are expressed in either a LaGrangian sense, or Eulerian sense.
# 
# ```{figure} velocity-field.png
# ---
# width: 500px
# name: velocity-field
# ---
# Coordinate systems for velocity description
# ```
# 
# Field is from the mathematical description of a field.  Various rules apply to fields, and these are used later on.
# 
# - Magnetic Fields
# - Elactric Fields
# - Gravitational Fields
# - Strawberry Fields (forever)
# 
# Are examples of "things" that are fields.  The idea is that if you know location, you know behavior.
# ```{figure} velocity-equation.png
# ---
# width: 500px
# name: velocity-equation
# ---
# Parametric (in time) velocity field equation
# ```
# 
# ```{figure} velocity-stream.png
# ---
# width: 500px
# name: velocity-stream
# ---
# Streamline coordinates for a velocity 
# ```

# In[ ]:





# ### Will it float
# 

# In[ ]:





# 
# ## Readings
# 
# 1. CE-3305-2022-1 Syllabus. [http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html](http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html)
# 
# 2. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 93-177
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013.  (placeholder file to get links working). [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-5.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-5.pdf)
# 
# 4. Cleveland, T. G. (2014) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. [http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-005.0.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-005.0.pdf)
# 
# 5. De Lima, R. P., Cleveland, T. G., De Carvalho, R.P., 2014. *Infrared thermography as a heat tracer method for velocity estimation in shallow flows* [Die Bodenkultur, Journal for Land Management, Food, and Envrionment, Vol 65, No. 3-4, pp. 71-77. ISSN 006-5471](http://54.243.252.9/ce-3305-webroot/3-Readings/Thermal-Image.PDF)

# In[ ]:





# In[ ]:




