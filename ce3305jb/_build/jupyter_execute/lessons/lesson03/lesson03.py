#!/usr/bin/env python
# coding: utf-8

# # Fluid Statics and Pressure 
# 
# ## Lesson Outline
# - Fluid Statics
#  - Pressure
# - Measurment
# - Hydrostatic Forces on a Plane Surface

# ## Fluid Statics
# 
# Fluid statics deals with forces in fluids that are have no relative motion within the fluid.  The vessel containing the fluid may be at non-zero velocity or acceleration, but the fluid body within the vessel has no relative motion.
# 
# Two principal types of forces involved are body and surface forces as shown in {numref}`FluidStatics` 
# 
# ```{figure} FluidStatics.png
# ---
# width: 500px
# name: FluidStatics
# ---
# A sphere of some fluid, depicting a local coordinate system, differential area and a normal and tangential force pair
# ```
# Body forces are developed without contact and are distributed over the entire volume of a fluid.  In the sketch the weight of the sphere is a body force.
# 
# Surface forces act at boundaries of a medium through contant.  The normal force in the sketch (which is the product of pressure and area) is a surface force, defined on the surface of the sphere.
# 
# Stress is the limiting value of $\frac{dF}{dA}$; in the sketch there are two stresses: a normal stress (usually called pressure), and a tangential stress (usually called shear).
# 
# Shear stresses are formed by friction, no-slip assumption, and other practically occuring situations.

# ```{figure} Stresses.png
# ---
# width: 500px
# name: Stresses
# ---
# Shear and normal stresses on a plane parallel to x-y coordinate plane, at some value z.
# ```
# {numref}`Stresses` is a diagram of a small planar element in a 3-D cartesian coordinate system that illustrate normal and shear stresses.  The tensor-like naming system is also indicated.  
# 
# A conventional notation is $\sigma_{n,i-k}$ for normal stress, and $\tau_{n,i-k}$ for shear stress.  The first subscript is the direction of the outward pointing normal vector from the application plane (in the drawing +z), the second subscript is the direction of force application, with the normal stress positive into the plane.  In the drawing the three stresses are $\sigma_{z,z}$,$\tau_{z,x}$, and $\tau_{z,y}$.
# 
# ### Pressure
# 
# Fluid pressure (usual symbol $p$) is the normal stress applied to a fluid element, so in practice we simply make the direct substitution.
# 
# :::{note}
# The use of pressure in fluids and normal stress in solids is simply a convention - one could refer to solids pressure but that would confuse people.
# :::
# 
# Pressure is a normal force per unit area, so at any **point** within a fluid it is a scalar quantity. The dimensionality of pressure is the ratio of force to area; typical units are $\frac{N}{m^2} = Pa$,$\frac{lbs}{in^2}$.  Pressure is also expressed in atmospheres $1 atm = 101325Pa = 14.75psi$ and liquid column height $1 atm \approx 10m_{water} \approx 29.92in_{Hg}$
# 
# :::{note}
# Pressure is scalar (magnitude), the force it causes when pushing against an object is a vector (magnitude and direction)
# :::

# ```{figure} PressureWedge.png
# ---
# width: 500px
# name: PressureWedge
# ---
# FBD of small wedge of a static fluid.
# ```
# {numref}`PressureWedge` is a free body diagram of a small wedge of fluid; analyzing the wedge we can demonstrate that pressure is a scalar (Pascal's Law).
# 
# First we will stipulate the fluid is a rest; no internal motion.  Next perform a force balance in each direction as in {numref}`ForceBalanceWedge`
# 
# ```{figure} ForceBalanceWedge.png
# ---
# width: 500px
# name: ForceBalanceWedge
# ---
# Force balance x,y, and z directions on fluid wedge.
# ```
# Notice we immediately invoke the definition of pressure to compute forces $F=p \cdot A$ where $A = \Delta x \Delta z$ and such, applying trigonometry to the wedge to resolve its force components. The directions are associated with the outward pointing normal vectors associated with the various planar areas.
# 
# We complete the analysis by studying the requirement of zero motion (statics) and find thet indeed pressure is a scalar as in {numref}`FBComplete`
# 
# ```{figure} FBComplete.png
# ---
# width: 500px
# name: FBComplete
# ---
# Force balance x,y, and z directions on fluid wedge.
# ```
# 
# Because the three pressures are all the same at a point, we can drop the double subscript notation and simplify our notation herein.
# 
# Some practical application of Pascal's Law is that in a closed system a change in pressure is transmitted undiminished throughout the entire system.  This phenomenon is the basis of hydraulic machinery like pneumatic jacks (pg. 49 of the textbook)

# ### Absolute and Gage Pressure
# Pressure is usually measured against some reference value.  Two values in common use are a vaccum (zero pressure) and a standard atmosphere.
# 
# If the measurement is referenced to a standard atmosphere the measure is called *gage pressure*.
# 
# If the measurement is referenced to a vaccum, the measure is called *absolute pressure*
# 
# Gage pressures can be negative, but negative absolute pressures don't make any sense.
# 
# ```{figure} AbsolutePressure.png
# ---
# width: 500px
# name: AbsolutePressure
# ---
# Force balance x,y, and z directions on fluid wedge.
# ```
# {numref}`AbsolutePressure` is a diagram depicting the relationship of gage and absolute pressures.
# 
# ### Hydrostatic Equation
# Here we develop the fundamental equation of fluid statics, and examine a couple of applications (pg. 52 is a condensed explaination).
# 
# Recall fluid statics means no relative motion within the fluid - the entire fluid behaves as a rigid body. The absence of angular deformation implies absence of shear stress; static fluids only sustain normal stress (pressure)
# 
# ```{figure} fstatics-1.png
# ---
# width: 500px
# name: fstatics-1
# ---
# Velocity gradient in static fluid
# ```
# {numref}`fstatics-1` is the mathematical statement of these stipulations. 
# 
# ```{figure} fruid-element.png
# ---
# width: 500px
# name: fruid-element
# ---
# Small fluid element in space (the final frontier!)
# ```
# 
# Consider a fluid element as in {numref}`fruid-element`. We analyze the forces on the element taking limits as appropriate (continuum hypothesis) to recover the equation of a static fluid.
# 
# ```{figure} fstatics-2.png
# ---
# width: 500px
# name: fstatics-2
# ---
# Small fluid element in space (the final frontier!)
# ```
# {numref}`fstatics-2` 
# 
# Writing the surface and body forces of the element as a rigid body, and equating these forces to acceleration (Newton's 2nd Law) produces a set of terms in {numref}`fstatics-3`
# 
# ```{figure} fstatics-3.png
# ---
# width: 500px
# name: fstatics-3
# ---
# Caption
# ```
# Using Taylor-series expansions about the centroid of the element 
# 
# ```{figure} fstatics-4.png
# ---
# width: 500px
# name: fstatics-4
# ---
# Caption
# ```
# {numref}`fstatics-4`
# 
# ```{figure} fstatics-5.png
# ---
# width: 500px
# name: fstatics-5
# ---
# Caption
# ```
# {numref}`fstatics-5`
# 
# ```{figure} fstatics-6.png
# ---
# width: 500px
# name: fstatics-6
# ---
# Caption
# ```
# {numref}`fstatics-6`
# 
# ```{figure} fstatics-7.png
# ---
# width: 500px
# name: fstatics-7
# ---
# Caption
# ```
# {numref}`fstatics-7`
# 
# ```{figure} fstatics-8.png
# ---
# width: 500px
# name: fstatics-8
# ---
# Caption
# ```
# {numref}`fstatics-8`
# 
# ```{figure} fstatics-9.png
# ---
# width: 500px
# name: fstatics-9
# ---
# Caption
# ```
# {numref}`fstatics-9`
# ## Pressure Measurements
# 
# 
# Specific gravity is the ratio of density of a fluid to a reference fluid.  In Civil Engineering the reference fluid is typically liquid water. Typical symbol is $S$ 
# 
# $$ S =\frac{\rho_{i}}{\rho_{water}}=\frac{\gamma_{i}}{\gamma_{water}} $$
# 
# ## Examples
# 
# ### Example 1
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
# ### Example 2
# 
# The heat amount added to a unit mass of fluid to raise the temperature one degree (units system dependent!) while volume is held constant.  
# Typical symbol is $c_v$.
# 
# ### Example 3
# 
# The heat amount added to a unit mass of fluid to raise the temperature one degree (units system dependent!) while pressure is held constant.  
# 
# Typical symbol is $c_p$.
# 
# ## Pressure Force on Submerged Objects
# 
# Energy a unit mass possesses because of its state of molecular activity.  Typical symbol is $u$
# 
# :::{note}
# The symbol $u$ is also commonly used for the x-component, or streamline component of velocity.  Be aware of context to avoid confusion.  In some documents $U$ is the velocity vector - again the context should be a clue.
# :::
# 
# ### Example 4
# 
# Energy a substance possesses because of internal energy and applied normal stress (aka pressure).  Typical symbol is $h = u + \frac{p}{\rho}$
# 
#  

# ## References
# 
# 1. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 47-80
# 
# 2. Cleveland, T. G. (2014) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. [http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-003.1.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-003.1.pdf)
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013. [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-3.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-3.pdf)
# 
# 4. CE-3305-2022-1 Syllabus. [http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html](http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html)

# In[ ]:




