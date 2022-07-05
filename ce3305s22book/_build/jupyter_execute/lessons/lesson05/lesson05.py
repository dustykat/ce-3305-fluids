#!/usr/bin/env python
# coding: utf-8

# # Flow Kinematics
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





# ### Uniform Flow
# 
# Uniform flow occurs in things with relatively straight pathlines (streamlines), and constant cross section geometries.  Things like pipes, channels of constant geometry, aquifers (like sand-filled pipes), and petroleum reservoirs (like aquifers, but with hydrocarbons in economically useable amounts).
# 
# If geometry changes like in a nozzle, then non-uniform flow.  If at steady flowrate, non-uniform can have convective acceleration.
# 
# ```{figure} uniform-flow.png
# ---
# width: 500px
# name: uniform-flow
# ---
# Uniform flow examples
# ```
# 
# Laminar flow is where fluid in adjacent layers (think back to definition of viscosity) move smoothly with respect to each other (very little mixing across layers).  Turbulent flow has layers mixing substantially.
# 
# **Viscous** shear stresses impact the flow.
# 
# **Inviscid** shear stresses small enough to ignore.
# 
# ```{figure} boundary6-1.png
# ---
# width: 500px
# name: boundary6-1
# ---
# Multiple flow regimes around a cylinder
# ```
# 
# Different regimes can exist simultaneously in adjacent space as in {numref}`boundary6-1`. The approach region is nearly inviscid, at the boundary viscid flow along the interface, separation where flow leaves the interface, and a wake region.  Drag increases where there is separation - prevention is impossible but drag reduction by delaying sepaeration is possible.
# 
# ```{figure} cannonball.png
# ---
# width: 500px
# name: canonball
# ---
# Surface modifications to delay separation
# ```
# 
# Acceleration occurs when there is a change in speed and/or direction.
# 
# 
# ```{figure} acceleration1D1.png
# ---
# width: 500px
# name: acceleration1D1
# ---
# 
# ```
# 
# Apply these ideas in multiple spatial dimensions:
# 
# 
# ```{figure} acceleration3D1.png
# ---
# width: 500px
# name: acceleration3D1
# ---
# 
# ```
# Re-expressing using kinematics terms 
# 
# ```{figure} acceleration3D2.png
# ---
# width: 500px
# name: acceleration3D2
# ---
# 
# ```
# 
# Some tidying
# 
# ```{figure} acceleration3D3.png
# ---
# width: 500px
# name: acceleration3D3
# ---
# 
# ```
# 
# A schematic of particle motion over a short time interval.
# 
# ```{figure} acceleration3D4.png
# ---
# width: 600px
# name: acceleration3D4
# ---
# 
# ```
# 
# We can examine the acceleration either as above or as:
# 
# ```{figure} acceleration3D5.png
# ---
# width: 400px
# name: acceleration3D5
# ---
# 
# ```
# Now recall the expression derived when we demonstrated that pressure should be scalar
# 
# 
# ```{figure} euler-replay.png
# ---
# width: 400px
# name: euler-replay
# ---
# 
# ```
# 
# Employ some of these ideas in an example.

# #### Example: Flow field in a nozzle
# 
# Here is an example of the type of analysis involved.  Identify the problem solving steps depicted.
# 
# ```{figure} trapezoid-nozzle.png
# ---
# width: 600px
# name: trapezoid-nozzle
# ---
# 
# ```
# 
# 

# ### Euler's Equation and the Bernoulli Equation
# 
# Here we will start with the Euler equation and from a sequence of plausible stipulations arrive at the Bernoulli Equation.  This development is an alternative to the way most books present the Bernoulli Equation - choose whichever makes more sense to you.
# 
# ```{figure} euler-one.png
# ---
# width: 500px
# name: euler-one
# ---
# 
# ```
# 
# #### Example: Fluid surface under constant linear acceleration
# 
# Here is an example combining hydrostatic pressure equation and acceleration.  Identify the problem solving steps depicted.  
# 
# ```{figure} linear-acc-1.png
# ---
# width: 600px
# name: linear-acc-1
# ---
# 
# ```
# 
# ```{figure} linear-acc-2.png
# ---
# width: 600px
# name: linear-acc-2
# ---
# 
# ```
# #### Example: Constant Angular Velocity
# 
# ```{figure} ang-vel-1.png
# ---
# width: 600px
# name: ang-vel-1
# ---
# 
# ```
# 
# ```{figure} ang-vel-2.png
# ---
# width: 600px
# name: ang-vel-2
# ---
# 
# ```
# 
# Now to continue to onward to the Bernoulli Equation.
# 
# ```{figure} euler-two.png
# ---
# width: 500px
# name: euler-two
# ---
# 
# ```
# 
# ```{figure} euler-three.png
# ---
# width: 500px
# name: euler-three
# ---
# 
# ```
# 
# ```{figure} euler-four.png
# ---
# width: 500px
# name: euler-four
# ---
# 
# ```
# 
# ```{figure} euler-five.png
# ---
# width: 500px
# name: euler-five
# ---
# 
# ```
# 
# ```{figure} euler-six.png
# ---
# width: 500px
# name: euler-six
# ---
# 
# ```
# 
# ```{figure} bernoulli-one.png
# ---
# width: 500px
# name: bernoulli-one
# ---
# 
# ```
# 
# 

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
