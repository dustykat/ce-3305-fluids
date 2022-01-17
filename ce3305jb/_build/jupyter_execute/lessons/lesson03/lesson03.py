#!/usr/bin/env python
# coding: utf-8

# # Fluid Statics and Pressure 
# 
# ## Lesson Outline
# - Fluid Statics
#  - Pressure
# - Measurement
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
# We complete the analysis by studying the requirement of zero motion (statics) and find that indeed pressure is a scalar as in {numref}`FBComplete`
# 
# ```{figure} FBComplete.png
# ---
# width: 500px
# name: FBComplete
# ---
# Analysis summary and demonstration pressure must be scalar.
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
# Gage and absolute pressure.
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
# Force balance statement, and naming of forces
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
# Expansion of forces from centroid to front, back,left,right, top, bottom face of the small fluid element.
# ```
# Using Taylor-series expansions about the centroid of the element 
# 
# ```{figure} fstatics-4.png
# ---
# width: 500px
# name: fstatics-4
# ---
# Substitution into force definition (surface forces)
# ```
# {numref}`fstatics-4` is the substitution of our forces at each face into the equation of motion.
# 
# ```{figure} fstatics-5.png
# ---
# width: 500px
# name: fstatics-5
# ---
# Surface and body forces into balance equation; rescaling by element volume
# ```
# {numref}`fstatics-5` is the balance equation divided by the small but non-vanishing element volume to produce the fluid equation at an arbitrary point.
# 
# ```{figure} fstatics-6.png
# ---
# width: 500px
# name: fstatics-6
# ---
# Zero acceleration equation of fluid statics
# ```
# {numref}`fstatics-6` is the equation of motion (this is actually Euler's equation - but he does not need it anymore!) at zero acceleration.
# 
# ```{figure} fstatics-7.png
# ---
# width: 500px
# name: fstatics-7
# ---
# Decomposition into cartesian components
# ```
# {numref}`fstatics-7` is the decomposition of the vector equation into its independent components, in this case cartesian coordinates. The $z$-axis equation is the only one conveying meaningful information (because of our choice of gravitational action).
# 
# ```{figure} fstatics-8.png
# ---
# width: 500px
# name: fstatics-8
# ---
# Hydrostatic equation in a liquid
# ```
# {numref}`fstatics-8` is the hydrostatic equation for an incompressible liquid (like water).  Pressure increases moving down from the free surface.
# 
# ```{figure} fstatics-9.png
# ---
# width: 500px
# name: fstatics-9
# ---
# Hydrostatic approximation for compressible fluid (like the atmosphere)
# ```
# {numref}`fstatics-9` is the hydrostatic approximation for compressible fluid. Here the ideal gas law is used as the equation of state.

# ## Pressure Measurements
# 
# Pressure is mesured by a variety of devices depending on the fluid.  Some of these are:
# 
# - barometer (for measuring atmospheric pressure)
# - piezometer
# - manometer
# - [Bourdon-type gages](https://www.bourdon-instruments.com/us/en/product-overview/pressure-gauges/c/36822) The principle of [operation](https://www.sciencedirect.com/topics/engineering/bourdon-tube) is the deformation of a curved tube in response to external pressure force change.
# - pressure transducers
# 
# ### Barometer
# 
# A barometer is a tube filled with liquid (oil,Hg,water), that is capped on one end, inverted into a basin and allowed to equilibrate as in {numref}`barometer`
# 
# 
# ```{figure} barometer.png
# ---
# width: 400px
# name: barometer
# ---
# Schematic of a barometer.  
# ```
# 
# The height of rise is obtained from a force balance between the vapor pressure of the working fluid in the capped end and the surrounding atmospheric pressure.
# 

# ### Piezometer
# 
# A piezometer is a tube inserted into a fluid (usually liquid) which is open at both ends, large enough diameter so that capillary rise is negligible.  The height of rise of liquid in the tube is proportional to the static pressure in the liquid at the bottom of the tube.  
# 
# 
# ```{figure} piezometer.png
# ---
# width: 400px
# name: piezometer
# ---
# Schematic of a piezometer.  
# ```
# 
# A well in an aquifer is a common example of a piezometer that measures the water pressure at the bottom of the tube (or averaged over the well screen length)

# ### Manometer
# 
# Manometers are like a hybrid of a barometer and piezometer.
# 
# ```{figure} manometer.png
# ---
# width: 400px
# name: manometer
# ---
# Schematic of a manometer.  
# ```
# 
# Manometers are connected to a fluid (measured), via an immiscible working fluid (usually oil or Hg).  The force differential between the fluid and atmosphere is indicated by the working fluid.
# 
# As with similar devices the $\frac{F}{A}$ is equated to the column height differential in the working fluid through $h=\frac{p}{\rho_{w.f.}g}$
# 
# ```{figure} manometer-rules.png
# ---
# width: 400px
# name: manometer-rules
# ---
# Reading a manometer.  
# ```
# 
# Multiple tube/fluid manometers follow 2 rules (Pascal's law, and the hydrostatic equation)
# 
# 1. Any two points at the same elevation in a **continuous** length of the **same** fluid are at the same pressure.
# 2. pressure **increases** with depth in a liquid column.

# ### Transducers
# [Insert link to sensor book here]

# ## Examples
# Below are a few examples applying the hydrostatic equation and Pascal's law in a few different situations
# 
# ### Example 1
# 
# ```{figure} example1-1.png
# ---
# width: 500px
# name: example1-1
# ---
# Pressure at the bottom of a vessel.
# ```
# {numref}`example1-1` is a classical pressure at the bottom of a vessel, using the problem solving protocol.

# ### Example 2
# 
# ```{figure} example2-1.png
# ---
# width: 500px
# name: example2-1
# ---
# Pressure in a two-layer fluid system (1 of 2)
# ```
# {numref}`example2-1` is an analysis of a multi-phase system (Air, Oil, Water), using the problem solving protocol.
# 
# ```{figure} example2-2.png
# ---
# width: 500px
# name: example2-2
# ---
# Pressure in a two-layer fluid system (2 of 2)
# ```
# {numref}`example2-2` is an analysis of a multi-phase system (Air, Oil, Water), using the problem solving protocol.

# ### Example 3
# 
# ```{figure} example3-1.png
# ---
# width: 500px
# name: example3-1
# ---
# Manometer with three fluids (1 of 3)
# ```
# {numref}`example3-1` is a manometer system, with two working fluids (and the measured fluid for three total)
# 
# ```{figure} example3-2.png
# ---
# width: 500px
# name: example3-2
# ---
# Manometer with three fluids (2 of 3)
# ```
# {numref}`example3-2` is a manometer system, with two working fluids (and the measured fluid for three total)
# 
# ```{figure} example3-3.png
# ---
# width: 500px
# name: example3-3
# ---
# Manometer with three fluids (3 of 3)
# ```
# {numref}`example3-3` is a manometer system, with two working fluids (and the measured fluid for three total)

# ### Example 4
# 
# ```{figure} example4-1.png
# ---
# width: 500px
# name: example4-1
# ---
# Pressure in a small drop (1 of 2)
# ```
# {numref}`example4-1` is the derivation of a formula to estimate the pressure in a small spherical droplet.
# 
# ```{figure} example4-2.png
# ---
# width: 500px
# name: example4-2
# ---
# Pressure in a small drop (2 of 2)
# ```
# {numref}`example4-2` is the derivation of a formula to estimate the pressure in a small spherical droplet.

# ## Pressure Force on Submerged Objects
# 
# Now we consider the forces generated on submerged objects by hydrostatic pressure.  It's the same force you feel on your [耳](https://translate.yandex.com/?lang=en-ja&text=ears) when you dive to the bottom of a [schwimmbad](https://dictionary.cambridge.org/us/dictionary/german-english/schwimmbad).
# 
# :::{note}
# I am having a little fun with the language translators on Google; the sentance in English is "... It's the same force you feel on your ears when you dive to the bottom of a swimming pool".
# :::
# 
# ### Uniform Pressure
# 
# Consider area $A$ shown with **uniform** pressure as shown on {numref}`panel-uniform` 
# 
# ```{figure} panel-uniform.png
# ---
# width: 500px
# name: panel-uniform
# ---
# Pressure force on some area.
# ```
# The indicated force is the product of the area $A$ and the pressure $p$
# 
# $$F=pA$$
# 
# ### Distributed Pressure
# 
# Now, consider the area $A$ shown with **distributed** pressure as shown on {numref}`panel-distributed`.  As we move around the plate, the value of $p$ changes with position (like going down in a column of water)
# 
# ```{figure} panel-distributed.png
# ---
# width: 500px
# name: panel-distributed
# ---
# Pressure force on a small area in a variable pressure field
# ```
# 
# In this instance, we use calculus to integrate all the little forces fo fine the aggregate (net) force on the entire plate.
# 
# $$F = \int_{A} p \cdot dA$$
# 
# Now lets extend the idea, to an arbitrary angle in the distributed pressure field, as in {numref}`panel-angle`
# 
# ```{figure} panel-angle.png
# ---
# width: 500px
# name: panel-angle
# ---
# Flat plate submerged at an arbitrary angle
# ```
# Depth to an incremental portion of the plate $dy$ is $h$. Distance along the $+y$ axis is $y$.  The value of $y$ is related to depth, $h$, by the angle $\alpha$. 
# 
# :::{note}
# We choose $\alpha$ to represent the angle because it looks like a fish, and fish are found underwater!
# :::
# 
# Next looking at the plate from a viewing angle that is normal to the plate (the eyeball in the sketch)it might look like {numref}`panel-normal`
# 
# ```{figure} panel-normal.png
# ---
# width: 500px
# name: panel-normal
# ---
# Looking perpindicular to the flat plate. Width of the integrand is some function of $y$
# ```
# 
# In this sketch the panel area is $dA = width(y) \cdot dy$ when looking perpindicular to the $+y$ axis.  The resultant net force on the submerged plate (perpindicular to the $y$ axis) is simply 
# 
# $$F = \int_{A} p \cdot dA$$
# 
# Now we apply some geometry and triggernometry to relate the integral to depth (and some moments).
# 
# ```{figure} panel-trig.png
# ---
# width: 500px
# name: panel-trig
# ---
# Geometric/Trigonometric relationships.
# ```
# Generally we will want to express pressure in terms of $y$ or $h$.
# 
# $$ p = \rho g h = \rho g y sin(\alpha)$$
# 
# In practice the actual integration is a nusicance, instead we would likw to be able to deal in total area and depth.  The term in the red box is the [first moment of area](https://en.wikipedia.org/wiki/First_moment_of_area) that you had in statics.
# 
# :::{note}
# The observation of that the red box is the 1st moment of area, makes those tables of centroids and such for common geometric shapes quite useful in fluids!
# :::
# 
# If you recall from statics, the first moment of area is the distance to the centroid of the geometric object from the axis (in this case the $x$ axis that is trying to poke your eye!)
# 
# $$ \frac{1}{A} \int_A y \cdot dA = \bar y$$
# 
# Applying some trigonometry and algebraic substitution
# 
# $$F = \rho g y sin(\alpha) A \bar y = \rho g A \bar h$$
# 
# Where $\bar h$ is the depth from the free surface to the centroid of the plate area.  So we now can express the magnitude of the force in terms of depth (to the centroid) and the plate area.
# 
# $$F = \gamma A \bar h$$

# Now we have the magnitude, and sometimes that might be enough but usually we need to also know the line of action.  We find that by taking a moment to examine {numref}`line-o-action`
# 
# ```{figure} line-o-action.png
# ---
# width: 500px
# name: line-o-action
# ---
# Line of action of equivalent point load (equivalent to the actual distributed load)
# ```
# We will simply require the moment generated by the total force we just determined (equivalent point load) to be equal the the moment generated by the distributed force (actual distributed load).
# 
# Choosing the upper edge of the plate as a rotational axis we have
# 
# $$ \sum M_A = \int_A y dF = y_P F$$
# 
# Rearrangement gives
# 
# $$ y_P = \frac{\int_A y dF}{F} = \frac{\int_A y^2sin(\alpha)dA}{\int_A y sin(\alpha)dA}$$
# 
# Simplification gives
# 
# $$ y_P = \frac{\int_A y^2dA}{\int_A y dA} = \frac{I_x}{A \bar y}$$
# 
# The value $I_x$ is the moment of inertia about the $x$ axis. We will then recall the [parallel axis theorem](https://en.wikipedia.org/wiki/Parallel_axis_theorem) to find the value in terms of our centroidal locations
# 
# $$ y_P =  \frac{I_0}{A \bar y}+ \bar y$$
# 
# Where $I_0$ is the moment of inertia about the plate centroid (tabulated for common geometric shapes).
# 
# The nice thing is that this calculus will work fine for any surface (shape and orientation), but at the expense of having to perform analysis to find the functions to integrate (or do numerical integrations which is easier if we can describe the geometry)

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
# 
# 5. [Pressure Measurement](https://en.wikipedia.org/wiki/Pressure_measurement)
# 
# 6. [Barometer](https://en.wikipedia.org/wiki/Barometer)

# In[ ]:




