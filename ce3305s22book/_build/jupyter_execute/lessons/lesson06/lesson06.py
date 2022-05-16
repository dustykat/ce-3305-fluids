#!/usr/bin/env python
# coding: utf-8

# # Bernoulli Applications
# 
# ## Lesson Outline
# - Applications
# - Concepts of Flux (a prelude to Reynolds Transport Theorem)

# ### Background
# 
# The last lesson introduced the Euler (and Bernoulli) equations which are fundamental in applied fluid mechanics.
# 
# This lesson also examines applications using the equations as-is.
# 
# ### Bernoulli Equation
# 
# Recall from last time the equation of 
# 
# - steady ($\frac{\partial}{\partial t} = 0$)
# - inviscid ($ \frac{\partial V}{\partial y} = 0$)
# - gravity vector is down ($-z$)
# - incompressible ($\rho = constant$)
# - irrotational ($curl(V)=0$)
# 
# Results in 
# 
# $ \frac{p_1}{\rho g} + \frac{V_1^2}{2g} + z_1 = \frac{p_2}{\rho g} + \frac{V_2^2}{2g} + z_2  $
# 
# Below are some examples illustrating its use

# #### Example: Flow out of a holy tank
# 
# Identify the problem solving steps employed
# 
# ```{figure} bernoulli-ex1.png
# ---
# width: 600px
# name: bernoulli-ex1
# ---
# 
# ```

# #### Example: Pressure near tank outlet
# 
# Identify the problem solving steps employed
# 
# ```{figure} bernoulli-ex2.png
# ---
# width: 600px
# name: bernoulli-ex2
# ---
# 
# ```
# 
# 

# #### Example: How high will a fountain go?
# 
# Consider the fountains at a resort.  What kind of pressures and velocities are required to make the show happen?
# 
# ```{figure} bellagio.png
# ---
# width: 400px
# name: bellagio
# ---
# 
# ```
# 
# Here's a related problem that could form the basis of fountain design.
# 
# Identify the problem solving steps employed
# 
# ```{figure} bernoulli-ex3.png
# ---
# width: 600px
# name: bernoulli-ex3
# ---
# 
# ```
# 
# 

# ### Rotation of a Fluid
# 
# 
# 
# ```{figure} rotation-one.png
# ---
# width: 600px
# name: rotation-one
# ---
# 
# ```
# 
# ```{figure} rotation-two.png
# ---
# width: 600px
# name: rotation-two
# ---
# 
# ```
# 
# ```{figure} rotation-three.png
# ---
# width: 600px
# name: rotation-three
# ---
# 
# ```

# ### Control Volumes and Continunity
# 
# Consider a conduit with cross section area, $A$.
# 
# The volume of fluid that passes area $A$ at location $x$ in some time interval $\Delta t$ is given by
# $ A \Delta x = V$
# 
# ```{figure} discharge.png
# ---
# width: 600px
# name: discharge
# ---
# 
# ```
# 
# The flow rate is $Q = \frac{V}{\Delta t} = \frac{\Delta x}{\Delta t}A$, the "velocity term" $u = \frac{\Delta x}{\Delta t}$ is the "mean section velocity".
# 
# If the velocity varies over the cross section one can obtain the mean section velocity by integration; and in fact this is how streamflow is determined.  
# 
# ```{figure} velocity-dist.png
# ---
# width: 600px
# name: velocity-dist
# ---
# 
# ```
# 
# If the orientation is not orthogonal the integrals are the result of the inner product of the velocity vector $\bar V$ and the area vector $\bar {dA}$
# 
# ```{figure} q-flux.png
# ---
# width: 600px
# name: q-flux
# ---
# 
# ```
# 
# The mass flow rate is the product of the volumetric rate and the fluid density
# 
# ```{figure} mass-flow.png
# ---
# width: 600px
# name: mass-flow
# ---
# 
# ```
# 
# As with volume, the mass flows also are obtained by inner products as:
# 
# 
# ```{figure} frux-integrals.png
# ---
# width: 600px
# name: frux-integrals
# ---
# 
# ```

# #### Example: Flow in a Rectangular Conduit
# 
# ```{figure} rect-channel.png
# ---
# width: 600px
# name: rect-channel
# ---
# 
# ```

# #### Example: Flow in a Triangular Conduit
# 
# ```{figure} v-channel.png
# ---
# width: 600px
# name: v-channel
# ---
# 
# ```

# 
# ## Readings
# 
# 1. CE-3305-2022-1 Syllabus. [http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html](http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html)
# 
# 2. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 141-177
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013.  (placeholder file to get links working). [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-5.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-5.pdf)
# 
# 4. Cleveland, T. G. (2014) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. [http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-006.0.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-006.0.pdf)
# 
