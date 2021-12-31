#!/usr/bin/env python
# coding: utf-8

# # Intensive and Extensive Fluid Properties 
# 
# ## Lesson Outline
# 1. Basic Fluid Properties
#   - Intensive/Extensive Properties
#   - Typical physical and thermodynamic properties
#   - Equations of state (IGL)
# 2. Viscosimiters
#   - Measuring viscosity
#   - Example problems
# 3. Vapor Pressure
#   - Barometers

# ## Fluid Properties
# 
# Extensive properties apply to a system and are associated with a fixed quantity of mass.
# 
# Intensive properties apply to components of a system, and are defined with restect to a boundary in space. 
# 
# Imagine a gallon of water; its weight is an extensive property assocated with that gallon.  The specific weight, $\gamma$, is the weight per volume is an intensive property. The properties in the textboox (pp 14-19) are for the most part intensive properties (mostly defined per unit volume)
# 
# ```{figure} gallon-properties.png
# ---
# width: 400px
# name: gallon-properties
# ---
# One gallon, and a 30cc sample removed
# ```
# {numref}`gallon-properties` is a schematic of a simple example to relate extensive and intensive properties.  
# We first weigh the entire gallon, 8.32 lbs. Then we weigh the 30cc subsample, 0.065 lbs.
# 
# The extensive property of weight for the gallon is 8.32 lbs; the extensive property of weight for the 30cc is 0.065 lbs.
# 
# If we now compute specific weights of each entity and adjust to a common basis volume:

# In[1]:


spwt_gallon = 8.32 # lbs per gallon
spwt_30cc = 0.065 # lbs per 30 cc
# convert to common volume
spwt_30cc = spwt_30cc*(128/1)  # 30cc==1oz; 128oz==1gal conversion to common volume basis.
print('Sp. Wt. of 1 gallon sample = ',round(spwt_gallon,3))
print('Sp. Wt. of 30 cc sample = ',round(spwt_30cc,3))


# They are the same value (as anticipated); intensive properties are useful in most fluid mechanics problems because they are a property of a specific fluid, rather that some fixed volume of that fluid - however we must be comfortable using both.
# 
# ### Density
# Density (or mass density) is the mass per unit volume.  Typical symbol is $\rho$, sometimes subscripted to identify fluid in multiiple fluid problems.
# 
# $$ \rho = \frac{m}{V} $$
# 
# ### Specific Weight
# Specific weight is the weight per unit volume.  Typical symbol is $\gamma$.
# It is related to density by gravitational acceleration: 
# 
# $$\gamma = \rho g$$
# 
# ### Specific Gravity
# 
# Specific gravity is the ratio of density of a fluid to a reference fluid.  In Civil Engineering the reference fluid is typically liquid water. Typical symbol is $S$ 
# 
# $$ S =\frac{\rho_{i}}{\rho_{water}}=\frac{\gamma_{i}}{\gamma_{water}} $$
# 
# ### Bulk Modulus (of elasticity)
# 
# The bulk modulus relates the change in volume of a fluid element to a change in pressure.  For liquids it is quite high, gasses quite a bit smaller - it is essentially a Hooke's law (springs) for a continuum element.  It conveys how much pressure change is needed to effect a incremental volume change.
# 
# $$ E_v = -\frac{dp}{(\frac{dV}{V})} $$
# 
# Dimensionally it is a pressure.  For water at terresterial pressure and temperature its value is upwards of 2.2 GPa (about 23 atmospheres); for solid steel well over 150 GPa (about 1550 atmospheres).
# 
# In our practical sense, gas is compressible, water is not very compressible, steel smaller still.
# 
# All the properties above are temperature dependent, and in gasses the compressibility is small, hence they are called compressible fluids.
# 
# A few thermodynamic properties are useful too:
# 
# ### Constant Volume Specific Heat
# 
# The heat amount added to a unit mass of fluid to raise the temperature one degree (units system dependent!) while volume is held constant.  
# Typical symbol is $c_v$.
# 
# ### Constant Pressure Specific Heat
# 
# The heat amount added to a unit mass of fluid to raise the temperature one degree (units system dependent!) while pressure is held constant.  
# 
# Typical symbol is $c_p$.
# 
# ### Specific Internal Energy
# 
# Energy a unit mass possesses because of its state of molecular activity.  Typical symbol is $u$
# 
# :::{note}
# The symbol $u$ is also commonly used for the x-component, or streamline component of velocity.  Be aware of context to avoid confusion.  In some documents $U$ is the velocity vector - again the context should be a clue.
# :::
# 
# ### Specific Enthalpy
# 
# Energy a substance possesses because of internal energy and applied normal stress (aka pressure).  Typical symbol is $h = u + \frac{p}{\rho}$
# 
# ## Equation of State
# 
# The state of a fluid is the value of all its properties at specified temperature, pressure, and gravitational filed strength.  The Ideal Gas Law is a relatively simple equation of state for gasses.
# 
# ```{figure} pvnrt.png
# ---
# width: 400px
# name: pvnrt
# ---
# Ideal Gas Law (Equation of State)
# ```
# {numref}`pvnrt` is the equation of state in two different forms for gasses. An equation of state allows prediction of state as temperature, pressure, or volume are changed.  

# ## Viscosity
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
# ### Absolute Viscosity
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
# ### Apparent Viscosity
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
# ### Kinematic Viscosity
# 
# The ratio of absolute (or apparent) viscosity to the fluid density is called the *kinematic* viscosity. The usual symbol is $\nu = \frac{\mu}{\rho}$  The kinematic viscosity has dimensions of $\frac{Area}{Time}$
# 
# ### General Comments
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
# 
# 

# ## Example 1 
# 
# Here is a hand-worked example to illustrate viscosity concepts and problem solving protocol.
# 
# We start with a problem statement:
# 
# ```{figure} problem-statement.png
# ---
# width: 400px
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
# width: 400px
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
# width: 400px
# name: problem-known
# ---
# Known or given values
# ```
# {numref}`problem-known` is a list of known or supplied (in the problem statement) values
# 
# ```{figure} problem-unknown.png
# ---
# width: 400px
# name: problem-unknown
# ---
# Unknown (sought) values
# ```
# {numref}`problem-unknown` is a list of unknown or sought values
# 
# ```{figure} problem-governing-equations.png
# ---
# width: 400px
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
# width: 400px
# name: problem-solution-1
# ---
# Solution
# ```
# {numref}`problem-solution-1` is our initial work towards a solution, ending with an expression relating shear force and viscosity.
# 
# ```{figure} problem-solution-2.png
# ---
# width: 400px
# name: problem-solution-2
# ---
# Solution(continued)
# ```
# {numref}`problem-solution-2` is the completion where the geomtric terms are inserted and a numerical answer is supplied.
# 
# ```{figure} problem-discussion.png
# ---
# width: 400px
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
# width: 400px
# name: example2-p1
# ---
# Discussion of results
# ```
# {numref}`example2-p1` is a problem statement and list of known values and governing equations.
# 
# ```{figure} example2-p2.png
# ---
# width: 400px
# name: example2-p2
# ---
# Discussion of results
# ```
# {numref}`example2-p2` is a list of unknown values and defining sketches.  Notice the geometry poses some complexity, hence the varied drawings to guide analysis.
# 
# ```{figure} example2-p3.png
# ---
# width: 400px
# name: example2-p3
# ---
# Discussion of results
# ```
# {numref}`example2-p3` are continued defining sketches and associated analyses.
# 
# ```{figure} example2-p4.png
# ---
# width: 400px
# name: example2-p4
# ---
# Discussion of results
# ```
# {numref}`example2-p4` is the results in useful units, and a discussion of the findings. The problem parts are straightforward using concepts for prior classes, but the analyst does have to keep track of the steps to get to a useable solution.
# 

# In[ ]:





# In[ ]:





# ## Readings
# 
# 1. CE-3305-2022-1 Syllabus. [http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html](http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html)
# 
# 2. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 14-45
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013.  (placeholder file to get links working). [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-2.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-2.pdf)
# 

# In[ ]:




