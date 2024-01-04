#!/usr/bin/env python
# coding: utf-8

# # Flow Patterns and Visualization
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
# 
# ---

# Flow dimensions are classified by how many space coordinates are required to speciofy the velocity field.  All real flows are 3D, but useful results are possible with 2D and 1D approximations.
# 
# ## Velocity Field
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

# ## Uniform Flow
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
# Consider another image
# 
# ```{figure} starrynight.png
# ---
# width: 500px
# name: starrynight
# ---
# Multiple flow regimes ... What would you caption this?
# ```
# 
# How many regimes appear to be represented in {numref}`starrynight`?  
# 
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

# ## Example: Flow field in a nozzle
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

# In[ ]:




