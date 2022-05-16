#!/usr/bin/env python
# coding: utf-8

# # Viscosity
# 
# "... a property of a fluid that relates the resistance to motion (in a thin layer) when a shear force is applied..."  
# 
# This somewhat useless definition is trying to convey how fluids deform under shear, and more importantly the rate of deformation.  
# Consider a steel sheet that we cut with a shear (like sicssors), if we want to cut fast we need a lot of force; using the same shears on an equal thickness of plastic sheet will take less force for the same rate of cut.  
# This solids analog to viscosity conveys that steel is more viscous than plastic (usually).
# 
# ```{figure} viscosity-one.png
# ---
# width: 400px
# name: viscosity-one
# ---
# Viscosity Schematic
# ```
# {numref}`viscosity-one` Is a diagram attempting to convey the concept of viscosity.  In the drawing the thickness $\partial y$ and the deformation angle $\partial \alpha$ are small, and the sine of the angle is approximated by the angle itself.
# 
# ```{figure} viscosity-two.png
# ---
# width: 400px
# name: viscosity-two
# ---
# Viscosity Trigonometry
# ```
# {numref}`viscosity-two` shows the relevant trigonometry to relate deformation rate to shear stress.
# 
# ## Absolute Viscosity
# 
# ```{figure} newtonian.png
# ---
# width: 400px
# name: newtonian
# ---
# Absolute viscosity (definition) 
# ```
# {numref}`newtonian` defines a Newtonian fluid and introduces the absolute viscosity $\mu$ in terms of the thin layer, cross-layer velocity profile $\frac{du}{dy}$ and the applied shear stress $\tau$.  The viscosity has dimensions of $\frac{Force \cdot Time}{Area}$
# 
# ## Apparent Viscosity
# 
# ```{figure} non-newtonian.png
# ---
# width: 400px
# name: non-newtonian
# ---
# Apparent viscosity (definition) power-law model
# ```
# {numref}`non-newtonian` shows a typical power-law model of viscosity; the term is referred to as an apparent viscosity.  Many real fluids are Non-Newtonian and will have some type of viscosity model to explain the deformation behavior.
# 
# ## Kinematic Viscosity
# 
# The ratio of absolute (or apparent) viscosity to the fluid density is called the *kinematic* viscosity. The usual symbol is $\nu = \frac{\mu}{\rho}$  The kinematic viscosity has dimensions of $\frac{Area}{Time}$
# 
# ## General Comments
# Viscous effects cause a velocity gradient (profile) to develop across the fluid layers as shown in {numref}`slip-profile`.
# 
# ```{figure} slip-profile.png
# ---
# width: 400px
# name: slip-profile
# ---
# Velocity Profile Diagram
# ```
# {numref}`slip-profile` is a diagram of the cross-layer velocity profile. The slope of the profile is related to shear force and hence the apparent or absolute viscosity.
# 
# :::{note}
# The no-slip condition is deduced from experiments - in my opinion it is an assumption that velocity vanishes at the contact interface.  In your future studies keep this in mind; it is quite possible that slip occurs at some scale, however it is a useful and accepted boundary condition.
# :::

# ## Example 1 
# 
# Here is a hand-worked example to illustrate viscosity concepts and problem solving protocol.
# 
# We start with a problem statement:
# 
# ```{figure} problem-statement.png
# ---
# width: 500px
# name: problem-statement
# ---
# Block sliding on an inclined plane
# ```
# {numref}`problem-statement` is a problem statement of the problem we wish to solve. 
# 
# The next step is to sketch the situation, mindful of several different scales in the problem.
# 
# ```{figure} problem-sketch.png
# ---
# width: 500px
# name: problem-sketch
# ---
# Block sliding on an inclined plane (various definining sketches)
# ```
# {numref}`problem-sketch` is a set of sketches, showing the macro-scale conditions, as well as a free-body-diagram, and a sketch of the fluid layer between the block and the plane.
# 
# Next we list knowns, unknowns, and governing equations:
# 
# ```{figure} problem-known.png
# ---
# width: 500px
# name: problem-known
# ---
# Known or given values
# ```
# {numref}`problem-known` is a list of known or supplied (in the problem statement) values
# 
# ```{figure} problem-unknown.png
# ---
# width: 500px
# name: problem-unknown
# ---
# Unknown (sought) values
# ```
# {numref}`problem-unknown` is a list of unknown or sought values
# 
# ```{figure} problem-governing-equations.png
# ---
# width: 500px
# name: problem-governing-equations
# ---
# Relevant equations
# ```
# {numref}`problem-governing-equations` is an initial list of applicable equations (we may add to this list as the analysis proceedes).
# 
# Now we proceede with the analysis
# 
# ```{figure} problem-solution-1.png
# ---
# width: 500px
# name: problem-solution-1
# ---
# Solution
# ```
# {numref}`problem-solution-1` is our initial work towards a solution, ending with an expression relating shear force and viscosity.
# 
# ```{figure} problem-solution-2.png
# ---
# width: 500px
# name: problem-solution-2
# ---
# Solution(continued)
# ```
# {numref}`problem-solution-2` is the completion where the geomtric terms are inserted and a numerical answer is supplied.
# 
# ```{figure} problem-discussion.png
# ---
# width: 500px
# name: problem-discussion
# ---
# Discussion of results
# ```
# {numref}`problem-discussion` is a discussion of results; this part is important as part of professional documentation, esp. if the analysis is a first approximation and is being used to determine whether further work will be needed.

# ## Example 2 - Radial Geometry Kinematics
# 
# A similar example is presented below, however the geometry is changed a bit. 
# 
# ```{figure} example2-p1.png
# ---
# width: 600px
# name: example2-p1
# ---
# Fluid drive problem (i.e how a transmission works!)
# ```
# {numref}`example2-p1` is a problem statement and list of known values and governing equations.
# 
# ```{figure} example2-p2.png
# ---
# width: 600px
# name: example2-p2
# ---
# Schematic sketches to define problem terms
# ```
# {numref}`example2-p2` is a list of unknown values and defining sketches.  Notice the geometry poses some complexity, hence the varied drawings to guide analysis.
# 
# ```{figure} example2-p3.png
# ---
# width: 600px
# name: example2-p3
# ---
# Schematic sketches to define problem terms (continued)
# ```
# {numref}`example2-p3` are continued defining sketches and associated analyses.
# 
# ```{figure} example2-p4.png
# ---
# width: 600px
# name: example2-p4
# ---
# Results and Discussion
# ```
# {numref}`example2-p4` is the results in useful units, and a discussion of the findings. The problem parts are straightforward using concepts for prior classes, but the analyst does have to keep track of the steps to get to a useable solution.
# 

# ## Viscometers
# 
# A variety of [instruments](https://en.wikipedia.org/wiki/Viscometer) are used to measure viscosity.
# 
# They all operate on roughly the same principle - determine the force requires to make two solid planes move with a fluid between then; from the force and known geometry the viscosity can be inferred. The example problem below is a falling piston viscometer - with the question asked in an unusual fashion, but it could easily be used to measure viscosity based on a measured fall velocity.
# 
# ### Example Problem
# 
# Figure {numref}`FallingCylinderViscosity` is a schematic of a cylinder falling inside a pipe that is filled with oil. The annular space between the cylinder and the pipe is lubricated with an oil film that has viscosity $\mu$.
# 
# ```{figure} FallingCylinderViscosity.png
# ---
# width: 300px
# name: FallingCylinderViscosity
# ---
# Falling cylinder in an oil-filled pipe
# ```
# 
# - Derive a formula for the steady rate of descent of a cylinder with weight $W$ , diameter $d$, and length $l$ sliding inside a vertical smooth pipe that has inside diameter $D$. Assume the cylinder remains concentric with the pipe as it falls.
# - Use the general formula you develop to estimate the rate of descent for a cylinder 100 millimeters in diameter that slides inside a 100.5 millimeter inside diameter pipe. The cylinder is 200 millimeters long and weighs 15 Newtons. The lubricant is SAE 20W oil at $10^o~C$.
# 
# Applying the problem solving methodology we have:
# 
# ```{figure} FallingCylinderViscosity-Soln.png
# ---
# width: 400px
# name: FallingCylinderViscosity-Soln
# ---
# 
# ```
# 
# We can easily script a tool for frequent application of a falling cylinder viscometer

# In[1]:


# falling piston viscometer
import math
# viscosity function for falling piston in a tube geometry
def viscosity(weight,spacing,dpiston,lpiston,velocity):
    viscosity = (weight*spacing)/(2*math.pi*dpiston*lpiston*velocity)
    return viscosity
# Example Problem Values
weight = 15 #newtons
spacing = 0.5e-03 #meters spacing
dpiston = 0.1 #meters
lpiston = 0.2 #meters
velocity = 0.17 #meters/sec
print("Viscosity = ",round(viscosity(weight,spacing,dpiston,lpiston,velocity),3)," Newtons per square meter")

