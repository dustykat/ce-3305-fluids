#!/usr/bin/env python
# coding: utf-8

# # Conservation of Linear Momentum
# 
# ## Lesson Outline
# - Measuring velocity and pressure using pitot-static systems (Bernoulli application)
# - Examples of CV applications for continunity
# - CV Relationships for momentum

# ### Background
# 
# Linear momentum relates forces to changes in translational velocity.  Reynolds Transport Theorem is used to generate integral expressions of momentum balances in a control volume.
# 
# ### Linear Momentum
# 
# ```{figure} momentum-p1-1.png
# ---
# width: 600px
# name: momentum-p1-1
# ---
# Caption
# ```
# {numref}`momentum-p1-1` relates the extensive property of linear momentum for a system to the intensive property of momentum per unit mass which is the velocity vector. {numref}`momentum-p1-2` extends to the intensive property of momentum per unit volume which is the product of density and velocity vector $\rho \bar V$
# 
# ```{figure} momentum-p1-2.png
# ---
# width: 600px
# name: momentum-p1-2
# ---
# Caption
# ```
# The result of application of theReynolds Transport Theorem to the linear momentum term is an integral equation that relates the sum of external forces to the rate of change of linear momentum in the control volume plus the net momentum leaving across the control surface as depicted in {numref}`momentum-p1-3`
# 
# ```{figure} momentum-p1-3.png
# ---
# width: 600px
# name: momentum-p1-3
# ---
# Caption
# ```
# 
# ```{note} Application of momentum principles uses three primary principles:
# - Select an inertial (non-acelerating) reference frame
# - Indicate positive and negative coordinate directions
# - Draw the CV/CS and indicate
#     - Forces
#     - Velocities
#     - Outward pointing area vectors ($dA \bar$ vectors)
# ```
# 
# 

# ## Example 1: Application of Momentum to a Jet Pump
# 
# A water jet pump has jet area of 0.01 sq.m. and jet speed of 30 m/s. The jet is within a secondary stream of water having speed 3 m/sec.  The total duct area is 0.075 sq.m. The water is completely mixed in the pump and exits at uniform velocity; find the speed at the pump exit and the pressure rise in the pump.
# 
# The problem statement is explicitly repeated in {numref}`momentum-ex1-1`
# 
# ```{figure} momentum-ex1-1.png
# ---
# width: 600px
# name: momentum-ex1-1
# ---
# Caption
# ```
# 
# Apply our problem solving protocol as in {numref}`momentum-ex1-2`
# 
# ```{figure} momentum-ex1-2.png
# ---
# width: 600px
# name: momentum-ex1-2
# ---
# Caption
# ```
# Note on the CV diagram to draw:
# 
# - the +/- directions
# - the CV/CS
# - the $\bar dA $ vectors, and 
# - the $\bar V $ vector(s)
# 
# Then apply continunity and momentum to find the unknown values as in {numref}`momentum-ex1-3`
# 
# ```{figure} momentum-ex1-3.png
# ---
# width: 600px
# name: momentum-ex1-3
# ---
# Caption
# ```

# In[1]:


# computational thinning
u_jet = 30.0
u_approach = 3.0
a_jet = 0.01
a_approach = 0.065
a_total = 0.075
rho = 1000.0
# continunity
u_exit = (u_jet*a_jet+u_approach*a_approach)/a_total
# momentum
delta_p = -(rho/a_total)*(a_total*u_exit**2 - a_jet*u_jet**2 - a_approach*u_approach**2)
# results
print("Pump exit velocity ",round(u_exit,3),"     meters per second")
print("Added pressure     ",round(delta_p,3)," Pascals")


# ## Example 2: Forces in a Pipe Fitting
# 
# Consider a pipe fitting as depicted in {numref}`momentum-ex2-1`
# 
# ```{figure} momentum-ex2-1.png
# ---
# width: 600px
# name: momentum-ex2-1
# ---
# Caption
# ```
# 
# Apply our problem solving protocol as in {numref}`momentum-ex2-2`
# 
# ```{figure} momentum-ex2-2.png
# ---
# width: 600px
# name: momentum-ex2-2
# ---
# Problem Solving Protocol: Sketch, CV Definition, Governing Principles, Knowns and Unknowns
# ```
# Apply our analysis tools as in {numref}`momentum-ex2-3`
# 
# ```{figure} momentum-ex2-3.png
# ---
# width: 600px
# name: momentum-ex2-3
# ---
# Application of linear momentum in the two coordinate directions
# ```
# 

# In[ ]:





# ## Applications of Momentum
# 
# Momentum is used to find forces on objects that are changing the flow field.
# 
# Forces are important in things like
# 
# - Bridge piers
# - Wind turbine support columns
# - Retaining walls
# - Dams
# 
# As an example consider the force on a sluice gate (underflow from a powerhouse) as depicted in {numref}`momentum-p2-1`
# 
# ```{figure} momentum-p2-1.png
# ---
# width: 600px
# name: momentum-p2-1
# ---
# Schematic elevation view of a sluice gate
# ```
# Upon first inspection one would be tempted to treat the gate as a submerged plate and use hydrostatic calculations, except at point A the pressure is atmospheric, same as at the free surface just upstream of the gate, so the required conditions for hydrostatic analysis do not apply in this case. 
# 
# So instead of trying to find pressure on the gate, find force of gate on the water, then by eth equal-opposite action-reaction (Newtons's 2nd law) we can find force of water on the gate .
# 
# A first step is to draw a control volume as depicted in {numref}`momentum-p2-2`
# 
# ```{figure} momentum-p2-2.png
# ---
# width: 600px
# name: momentum-p2-2
# ---
# CV/CS for sluice gate
# ```

# ### Example 4
# 
# 

# In[ ]:





# While not at all perfect it illustrates using a calculator to approximate the problem.  

# 
# ## Readings
# 
# 1. CE-3305-2022-1 Syllabus. [http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html](http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html)
# 
# 2. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 293-355
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013.  (placeholder file to get links working). [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-9.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-9.pdf)
# 
# 4. Cleveland, T. G. (2014) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. [http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-7.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture09.pdf)
# 
