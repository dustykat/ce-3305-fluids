#!/usr/bin/env python
# coding: utf-8

# # Pressure (pp XXX-XXX)
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
