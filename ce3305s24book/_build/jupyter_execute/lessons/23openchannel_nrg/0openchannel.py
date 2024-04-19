#!/usr/bin/env python
# coding: utf-8

# # Open Conduits (pp. 632-691)
# 
# :::{admonition} Course Website
# [http://54.243.252.9/ce-3305-webroot/](http://54.243.252.9/ce-3305-webroot/)
# :::

# ## Readings
# 
# 1. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2022. ISBN: pp. 632-691
# 
# 2. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 3-14
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013. pp. 554-570 [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-16.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-16.pdf)
# 
# 4. Cleveland, T. G. (2014) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. [http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture016.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture016.pdf)

# ## Videos
# 
# - b

# ## Lesson Outline
# - Basic Principles
# - Characteristics of Open Channel Flow
# - Normal Flow
# - Specific Energy and Flow Regimes

# ## Basic Principles
# 
# Open channel flow - free surface, gravity driven.  
# 
# > From pg. 1 of [Sturm, T. Open Channel Hydraulics, 1 st Ed.](https://www.amazon.com/Channel-Hydraulics-Third-Terry-Sturm/dp/1260469700)
# >
# >![](open-flow-narrative.png)
# 
# :::{note}
# The gravity "drive" is mostly true - I would say such flows are dominated by momentum conditions, mostly with gravity influence.  Open flow can go uphill (adverse to gravitational drive) but not for much distance (os one will run out of momentum)
# :::
# 
# Common examples of open channels:
# 
# - rivers, streams, brooks, creeks, cricks (Applacian meaning small stream), billabongs, bourns, wadis, and many more localized terms for small streams
# - ditches, canals, aqueducts, storm sewers, sanitary sewers
# 
# > From pg. 1 of [Sturm, T. Open Channel Hydraulics, 1 st Ed.](https://www.amazon.com/Channel-Hydraulics-Third-Terry-Sturm/dp/1260469700) 
# >
# > ![](examples-ocf.png)
# 
# Applications of open channel flow principles
# 
# - Culvert design, bridge design, spillway design
# - Floodway analysis, and nusiance flooding prediction
# - Fate and transport of yummy/yucky stuff (dissolved and/or suspended)
# - Surge estimation and coastal flooding from cyclonic storms [(hurricane,typhoon)](https://en.wikipedia.org/wiki/Tropical_cyclone)
# 
# > From pg. 1 of [Sturm, T. Open Channel Hydraulics, 1 st Ed.](https://www.amazon.com/Channel-Hydraulics-Third-Terry-Sturm/dp/1260469700) 
# >
# > ![](applications-ocf.png)
# 

# ## Characteristics of Open Channel Flow
# 
# Three important characteristics of open channels are
# 
# - A free surface
# - Extremely variable cross section geometries
# - Inertia (momentum) and gravitational dominance on flow behavior reflected in the importance of the Froude number on predicting open channel behavior
# 
# :::{note}
# The Reynolds number still matters, just not as overarching as in closed conduit (pipe) flow
# :::
# 
# ### Free Surface
# 
# The free surface is an extra degree of freedom as compared to a conduit directed boundary; it is usually treatable as a streamline with constant pressure in equilibrium with the local atmosphere (i.e. $p=0_{gage}$)
# 
# ### Cross Sections
# 
# The cross section geometries are remarkably variable, but usually can be reduced to a few terms including:
# 
# - $T$ the topwidth, a function of cross section geometry and depth (above the thalweg reference elevation)
# - $A$ the flow area, a function of cross section geometry and depth (above the thalweg reference elevation).  Shown as the magenta shading in the drawing.
# - $P$ the wetted perimeter, which is the length of the liquid-solid contact curve.  Also a function of cross section geometry and depth (above the thalweg reference elevation)
# - $y$ the flow depth, ususlly measured from the local minimum elevation in the channel.  The locus of these minima in the longitudinal direction (downstream) forms a curve called the [thalweg](https://en.wikipedia.org/wiki/Thalweg).  The term derives from the German *talweg* whose literal translation is valley path.
# 
# A sketch depicting some of the common terms is
# 
# ![](cross-section.png)
# 
# Some additional terms in common application are:
# 
# - $R_H$ the hydraulic radius; the ratio of area to wetter perimeter
# - $D_H$ the hydraulic depth; the ratio of area to topwidth
# 
# ### Flow Resistance
# 
# Flow resistance is acombination of frictional shear at the liquid-solid boundary, as well as form resistance from various "roughness" components (even bridge piers can be grouped into this term) that are collectively modeled in practice as a single term that plays the same role that shear does in Euler's equation when we discuss viscous flow.
# 
# ![](friction-form.png)
# 
# ### Froude Number
# 
# The most important dimensionless parameter in open channel flow is the **Froude** number:
# 
# $$ Fr = \frac{V}{\sqrt{gL}} $$
# 
# where $V$ is the mean section velocity (speed), and $L$ is a characteristic length scale related to depth.  $Fr$ is the ratio of inertia to gravity forces.

# ## Solution of Open Channel Problems
# 
# Solutions to problems are achieved by a combination of
# 
# - Fluid Mechanics: conservation of mass, momentum, and energy
# - Empirical and theoretical equations & [nomographs](https://en.wikipedia.org/wiki/Nomogram) (graphical calculators).   These are espeically common in 1-D steady flow applications.
# - Computational hydraulics.  Complex geometries, unsteady flow.  
#   1. 1-D steady/unsteady is routine 
#   2. 2-D steady/unsteady is state-of-practice
#   3. 3-D steady is state-of-art
#   4. 3-D unsteady is research (for now; but just wait a few years as technology advances)
#   
# ### History
# 
# Experiments/Observations -> Empiricism -> Theoretical -> Mathematics -> Computational Methods

# 

# ## Definitions
# 
# Unsteady flow means discharge,$Q(t)$ is not constant in time at a cross-section. (Panels A and D in the drawing)
# 
# Steady flow means that discharge, $Q(t)$, is constant in time at a cross-section. (Panels B and C in the drawing)
# 
# ![](definitions.png)
# 
# If the flow depth $y$ is the same at all locations along the thalweg of a prisimatic channel, then the flow is *uniform* (Panel B in the drawing).  Steady flow that is *nonuniform* is either rapidly varying (changing over a short distance) or gradually varying (changing over a long distance).  Unsteady flows can also exhibit rapid and gradual variations.
# 
# ### Control Volumes and Basic Equations
# 
# The basic euqations (mass, momentum, and energy) are usually employed from cross-section to cross-section in a "flow tube" or stream tube which represents a kind of control volume (Panel B in the drawing) 
# 
# ![](control-effing-volumes.png)
# 
# Between cross sections the analytical unit is called a *reach* which is a part of a channel with **approximately** constant geometrical shape, constant bottom slope, and constant roughness characteristics.
# 
# Application of Reynolds' Transport Theorem to a control volume is used to derive (hypothesize) the conservaton of mass, momentum, and energy in a reach.  A collection of reaches is then analyzed  to represent an entire stream of interest
# 
# ![](reaches-bitch.png)
# 
# For mass conservation a control volume like that below can be employed
# 
# ![](reach-cv.png)

# ## Conservation of Mass
# The conservation of mass in the cell is the statement that mass entering and leaving the cell is balanced by the accumulation or lass of mass within the cell.   For pedagogical clarity, this section goes through each part of a mass balance then assembles into a difference equation of interest.    
# 
# *Mass Entering:*  Mass enters from the left of the cell in our sketch.  This direction only establishes a direction convention and negative flux means the arrow points in the direction opposite of that in the sketch.  In the notation of the sketch mass entering in a short time interval is:
# 
# 
# $$
# \dot{M}_{in}= \rho * ( Q-\frac{\partial Q}{\partial x}*\frac{\Delta x}{2})*\Delta t
# $$
# 
# where $\rho$ is the fluid density.  Notice that the mass flux is evaluated at the cell interface and not the centroid, while by convention $\rho$ is assumed to be defined as an average cell property.
# 
# *Mass Leaving:*  Mass leaves from the right of the cell in our sketch.    In the notation of the sketch mass leaving is:
# 
# $$
# \dot{M}_{out}= \rho * ( Q+\frac{\partial Q}{\partial x}*\frac{\Delta x}{2})*\Delta t
# $$
# 
# *Mass Accumulating:*  Mass accumulating within the reach is stored in the prism depicted in the sketch by the dashed lines.  The product of density and prism volume is the mass added to (or removed from) storage.  
# 
# The rise in water surface in a short time interval is $\frac{\partial y}{\partial t}*\Delta t$.
# The plan view area of the prism is $T(y)* \Delta x$.
# The product of these two terms is the mass added to storage, expressed as:
# 
# $$
# \dot{M}_{storage} = \rho *( \frac{\partial y}{\partial t}*\Delta t) *T(y)* \Delta x 
# $$
# 
# Equating the accumulation to the net inflow produces 
# 
# $$
#  \rho *( \frac{\partial y}{\partial t}*\Delta t) *T(y)* \Delta x =  \rho * ( Q-\frac{\partial Q}{\partial x}*\frac{\Delta x}{2})*\Delta t - \rho * ( Q+\frac{\partial Q}{\partial x}*\frac{\Delta x}{2})*\Delta t
# $$
# 
# This is the mass balance equation for the reach.  If the flow is isothermal, and essentially incompressible then the density is a constant and can be removed from both sides of the equation.  
# 
# $$
# ( \frac{\partial y}{\partial t}*\Delta t) *T(y)* \Delta x =  ( Q-\frac{\partial Q}{\partial x}*\frac{\Delta x}{2})*\Delta t - ( Q+\frac{\partial Q}{\partial x}*\frac{\Delta x}{2})*\Delta t
# $$
# 
# Rearranging the right hand side produces
# 
# $$
# ( \frac{\partial y}{\partial t}*\Delta t) *T(y)* \Delta x =  -\frac{\partial Q}{\partial x}*\frac{\Delta x}{2}*\Delta t - \frac{\partial Q}{\partial x}*\frac{\Delta x}{2}*\Delta t = -\frac{\partial Q}{\partial x}*\Delta x*\Delta t
# $$
# 
# Dividing both sides by $\Delta x*\Delta t$ yields
# 
# $$
# ( \frac{\partial y}{\partial t}) *T(y) = -\frac{\partial Q}{\partial x}
# $$
# 
# This equation is the conventional representation of the conservation of mass in 1-D open channel flow.   If the equation includes lateral inflow the equation is adjusted to include this additional mass term.  The usual lateral inflow is treated as a discharge per unit length added into the mass balance as expressed below:
# 
# $$
# ( \frac{\partial y}{\partial t}) *T(y) + \frac{\partial Q}{\partial x} = q
# \label{eqn:continunity}
# $$
# 
# Compare this equation to Equation 1.6 in [Sturm, T. Open Channel Hydraulics, 1 st Ed.](https://www.amazon.com/Channel-Hydraulics-Third-Terry-Sturm/dp/1260469700) and observing that $q=0$ (in the book), and $\frac{\partial A}{\partial t} = (\frac{\partial y}{\partial t}) *T(y)$ and we have the same result.
# 
# $$
# \frac{\partial A}{\partial t}  + \frac{\partial Q}{\partial x} = 0
# $$

# ## An application of Mass Conservation (Continunity) - Example 1
# 
# The river flow at an upstream gauging station is measured as 1500 $\frac{m^3}{sec}$, and at another gauging station 3 $km$ downstream, the discharge is measured as 750 $\frac{m^3}{sec}$ at the same moment in time. The channel is uniform, with a width of 300 $m$.
# 
# Determine:
# 
# - The rate of change in the average water surface elevation in meters per hour.
# - Whether the stage (average water surface elevation) is rising or falling.
# 

# 
# 

# >## Sketch(s) here
# >
# >## Known quantities
# >The problem statement supplies:
# >- Station 1 is upstream of station 2
# >- At station 1;  $Q_1=~1500 \frac{m^3}{s}$,$x_1=0~m$,$T_1=300~m$
# >- At station 2;  $Q_2=~750 \frac{m^3}{s}$,$x_2=3000~m$,$T_2=300~m$<br>
# >
# >## Unknown quantities
# >
# >The change in $y$, and the sign of the change.
# >
# >## Governing principles
# >
# >Here we apply continunity in a generalized structure:
# >
# >$$( \frac{\partial y}{\partial t}) *T(y) + \frac{\partial Q}{\partial x} = 0$$
# >
# > ## Solution (step-by-step/computations)
# >
# >So we will set-up the computations for this case
# >
# >$\frac{\Delta WSE}{\Delta t} = \frac{\partial(y)}{\partial t} + \frac{\partial(z)}{\partial t}$
# ><br>but $z$ is the channel bottom, which should be time invariant so 
# ><br>$\frac{\Delta WSE}{\Delta t} = \frac{\partial y}{\partial t}$
# ><br>The spatial change in discharge is given in the problem so that
# ><br>$\frac{\partial Q}{\partial x} = \frac{\Delta Q}{\Delta x} = \frac{Q_2 - Q_1}{x_2 - x_1}$
# ><br>Now make the substitutions 
# ><br>$ \frac{\partial y}{\partial t}   =  \frac{(\frac{Q_1 - Q_2}{x_1 - x_2})}{T(y)}$
# ><br>And script a solution

# In[1]:


# script
Q1 = 1500
Q2 = 750
T1 = 300
T2 = 300
X1 = 0
X2 = 3000

DQDX = (Q2-Q1)/(X2-X1)
dydt = -DQDX/((T1+T2)*0.5)
if dydt > 0.0:
    print("WSE is changing at",dydt*3600,"meters per hour, and rising")
else:
    print("WSE is changing at",dydt*3600,"meters per hour, and falling")


# >## Discussion
# >
# >In this case we used the average topwidth to quantify the storage prism.

# ## Conservation of Momentum
# The conservation of momentum is the statement of the change in momentum in the reach is equal to the net momentum entering the reach plus the sum of the forces on the water in the reach.  As in the mass balance, each component will be considered separately for pedagogical clarity.
# 
# ![](fbd-cell.png)
# 
# *Momentum Entering:*
# Momentum entering on the left side of the sketch is 
# 
# $$
# \rho*QV = \rho*V^2A
# $$
# 
# 
# *Momentum Leaving:*
# Momentum leaving on the right side of the sketch is 
# 
# $$
# \rho*QV+\frac{\partial}{\partial x}(\rho*QV)\delta x = \rho*V^2A+\frac{\partial}{\partial x}(\rho*V^2A)\delta x
# $$
# 
# *Momentum Accumulating:*
# The momentum accumulating is the rate of change of linear momentum:
# 
# $$
# \frac{dL}{dt}= \frac{d~(mV)}{dt}=\frac{\partial}{\partial t}(\rho*AV*\delta x)=\rho*\delta x\frac{\partial}{\partial t}(AV)
# $$
# 
# 
# *Forces on the liquid in the reach:*
# 
# *Gravity forces:*  The gravitational force on the element is the product of the mass in the element and the downslope component of acceleration.
# 
# The mass in the element is $\rho*A\delta x$ 
# 
# The $x$-component of acceleration is $g~sin(\alpha)$, which is $\approx~S_0$ for small values of $\alpha$.
# 
# The resulting force of gravity is is the product of these two values:
# 
# $$
# F_g=\rho g *AS_0~\delta x
# $$
# 
# 
# 
# *Friction forces:*   Friction force is the product of the shear stress and the contact area.  In the reach the contact area is the product of the reach length and average wetted perimeter.  
# 
# $$
# F_{fr} = \tau * P_w * \delta x
# $$
# 
# :::{note}
# I am taking liberties with friction here - as stated previously, form friction is going to be lumped with stress into some kind of collective friction term.
# :::
# 
# where $P_w = A/R$, $R$ is the hydraulic radius.  A good approximation for shear stress in unsteady flow is $\tau = \rho g R S_f$.  $S_f$ is the slope of the energy grade line at some instant and is also called the friction slope.  This slope can be empirically determined by a variety of models, typically Chezy's or Manning's equation is used.  In either of these two models, we are using a STEADY FLOW equation of motion to mimic unsteady behavior --- nothing wrong, and it is common practice, but this decision does limit the frequency response of the model (the ability to change fast --- hence the shallow wave theory assumption!).
# 
# The resulting friction model is
# 
# $$
# F_{fr} =  \rho g A S_f * \delta x
# $$
# 
# 
# *Pressure forces:*   
# 
# Need narrative to explain the parts
# 
# $$
# F_p = \int_{A} {dF}
# $$
# 
# ![](pressure_sketch.png)
# 
# $$
# dF = (z-h)\rho g \xi (h) dh
# $$
# 
# where $\xi (h)$ is the width of the panel at a given distance above the channel bottom ($h$) at any section.
# 
# $$
# F_{p~net} = F_{p~up} - F_{p~down}
# $$
# 
# $$
# F_{p~net} = F_p -( F_p + \frac{\partial F_p}{\partial x}*\delta x) = - \frac{\partial F_p}{\partial x}*\delta x
# $$
# 
# $$
#  - \frac{\partial F_p}{\partial x}*\delta x = -\frac{\partial}{\partial x}[\int_{0}^{Z}\rho g (z-h) \xi(h) dh ] \delta x
# $$
# 
# $$
# F_{p~net}  = -\rho g [\frac{\partial z}{\partial x}\int_{0}^{Z} \xi(h) dh + \int_{0}^{Z} (z-h) \xi(h) \frac{\partial \xi(h)}{\partial x} dh] \delta x
# $$

# The first term integrates to the cross sectional area, the second term is the variation in pressure with position along the channel.
# 
# The other pressure force to consider is the bank force (the pressure force exerted by the banks on the element).  This force is computed using the same type of integral structure except the order is swapped.
# 
# $$
# F_{p~bank} =  [\int_{0}^{Z} \rho g (z-h) \frac{\partial \xi(h)}{\partial x} \delta x] dh
# $$
# 
# Now we put everything together.
# 
# $$
# {Momentum}_{in}-{Momentum}_{out} + \sum{F} = \frac{d(mV)}{dt}
# $$
# 
# Substitution of the pieces:
# 
# $$
# {Momentum}_{in}-{Momentum}_{out} + F_{p~net}+F_{bank} + F_{gravity} - F_{friction}  = \frac{d(mV)}{dt}
# $$
# 
# Now when the expressions for each expressions for each part
# 
# $$
# \begin{split}
# \rho*V^2A- \rho*V^2A-\frac{\partial}{\partial x}(\rho*V^2A)\delta x  \\
# -\rho g \frac{\partial z}{\partial x}\int_{0}^{Z} \xi(h) dh \delta x
# - [\int_{0}^{Z}\rho g (z-h)  \frac{\partial \xi(h)}{\partial x} dh] \delta x \\ 
# +[\int_{0}^{Z} \rho g (z-h) \frac{\partial \xi(h)}{\partial x} \delta x] dh\\
# +\rho g *AS_0~\delta x \\- (\rho g R S_f * \delta x)  \\ =  \rho*\delta x\frac{\partial}{\partial t}(AV)
#  \\
# \end{split}
# \label{eqn:momentum_expanded}
# $$
# 
# Each row of  the Equation above represents, in order:
# 
# 1. Net momentum entering the reach. 
# 2. Pressure force differential at the end sections.
# 3. Pressure force on the channel sides.
# 4. Gravitational force.
# 5. Frictional force opposing flow.
# 6. Total acceleration in the reach (change in linear momentum).
# 
# 
# Canceling terms and dividing by $\rho \delta x$ (isothermal, incompressible flow; reach has finite length) the equation simplifies to 

# $$
# \begin{split}
# -\frac{\partial}{\partial x}(V^2A) - g \frac{\partial z}{\partial x}\int_{0}^{Z} \xi(h) dh + g *AS_0~ - ( g R S_f * )  =  \frac{\partial}{\partial t}(AV)
# \end{split}
# \label{eqn:momentum_simpler}
# $$

# The second term integral is the sectional flow area, so it simplifies to 
# 
# $$
# -\frac{\partial}{\partial x}(V^2A) - g \frac{\partial y}{\partial x}A + gAS_0~ -  g A S_f   =  \frac{\partial}{\partial t}(AV)
# $$
# 
# The term with the square of mean section velocity is expanded by the chain rule, and using continunity becomes (notice the convective acceleration term from the change in area with time)
# 
# $$
# \begin{split}
# \frac{\partial}{\partial t}( AV) = A \frac{\partial V }{\partial t} + V \frac{\partial A }{\partial t} = A \frac{\partial V }{\partial t} -VA \frac{ \partial V }{\partial x} - V^2 \frac{\partial A }{\partial x} 
# \end{split}
# \label{eqn:momentum_simpler1}
# $$
# 
# Now expand and construct
# 
# 
# $$
# \begin{split}
# -V^2\frac{\partial A}{\partial x} - 2VA \frac{\partial V}{\partial x}
# - gA \frac{\partial y}{\partial x} + gA(S_0-S_f)   = A \frac{\partial V }{\partial t} -VA \frac{ \partial V }{\partial x} - V^2 \frac{\partial A }{\partial x} 
# \end{split}
# \label{eqn:momentum_simpler2}
# $$
# 
# Cancel common terms and simplify
# 
# $$
# \begin{split}
# -VA \frac{\partial V}{\partial x}
# - gA \frac{\partial y}{\partial x} + gA(S_0-S_f)   = A \frac{\partial V }{\partial t} 
# \end{split}
# \label{eqn:momentum_simpler3}
# $$

# The above equation is the final form of the momentum equation for practical use.  It will be rearranged in the remainder of this discuaaion to fit some other purposes, but this is the expression of momentum in the channel reach.
# 
# Divide by $gA$ and obtain 
# 
# $$
# \begin{split}
# - \frac{V}{g}\frac{\partial V}{\partial x}
# -  \frac{\partial y}{\partial x} + (S_0-S_f)   =  \frac{1}{g}\frac{\partial V }{\partial t} 
# \end{split}
# \label{eqn:momentum_simpler4}
# $$
# 
# Now rearrange to place the two slopes on the left side, and the remaining part of momentum to the right side.  
# 
# The next equation lets us examine the several flow regimes common in open channel flows.
# 
# $$
# \begin{split}
# S_0-S_f   =  \frac{1}{g}\frac{\partial V }{\partial t}   +  \frac{\partial y}{\partial x} + \frac{V}{g}\frac{\partial V}{\partial x}
# \end{split}
# \label{eqn:momentum_simpler5}
# $$
# 
# If the local acceleration (first term on the right) is zero, the depth taper (middle term on the right) is zero,
# 
# :::{note}
# Zero depth taper means constant depth flow.
# :::
# 
# and the convective acceleration (last term on the right) is zero, then the expression degenerates to the algebraic equation of *normal/uniform* flow ($S_0=S_f$).  If just the local acceleration term is zero, and all the remaining terms are considered, then the expression degenerates to the ordinary differential equation of gradually varied flow.
# 
# Finally, if all the terms are retained, then the dynamic flow (shallow wave) conditions are in effect and the resulting model is a partial differential equation.
# 
# Re-iterating these typical flow regimes:
# 
# > - Uniform flow; algebraic equation.
#   
#   > $$S_f = S_0 $$
# > - Gradually varied flow; ordinary differential equation.
#   
#   > $$S_f = S_0 -  \frac{\partial y}{\partial x} - \frac{V}{g}\frac{\partial V}{\partial x} $$
# > - Dynamic flow (shallow wave) conditions; partial differential equation.
#   
#   > $$S_f = S_0 -  \frac{\partial y}{\partial x} - \frac{V}{g}\frac{\partial V}{\partial x} - \frac{1}{g}\frac{\partial V }{\partial t} $$

# ### Some Foreshadowing
# 
# The coupled pair of equations, for continuity and momentum are called the St. Venant equations and comprise a coupled hyperbolic differential equation system.
# 
# $$
# (\frac{\partial y}{\partial t}) *T(y) + \frac{\partial Q}{\partial x} = q
# $$
# 
# $$
# S_0 - S_f  -  \frac{\partial z}{\partial x} - \frac{V}{g}\frac{\partial V}{\partial x}
# - \frac{1}{g}\frac{\partial V }{\partial t} = 0
# $$
# 
# 
# Solutions ($(z,t)$ and $(V,t)$ functions) are found by a variety of methods including finite difference, finite element, finite volume, and characteristics methods.
# 

# ## Conservation of Energy
# 
# Under reasonable practical assumptions the energy balance for a reach reduces to a modified bernoulli equation.  Equation 1.18 in the text is probably more familiar as
# 
# $$\frac{p_1}{\gamma} + z_1 + \frac{\alpha_1 V_1^2}{2g} + h_s = \frac{p_2}{\gamma} + z_2 + \frac{\alpha_2 V_2^2}{2g} + h_L$$
# 
# If the flow is steady and we know where the free surface is, then the pressure terms are simply the depth at their respective locations.

# ## Discharge Measurements
# 
# [USGS Discharge Measurements (a primer)](https://ca.water.usgs.gov/FERC/presentations/Discharge-Measurement-Data.pdf)
# 
# [USGS Creating Rating Curves (a different primer)](https://www.usgs.gov/centers/wyoming-montana-water-science-center/creating-rating-curve)
# 
# Rating curve lest us relate discharge $Q$ to a stage $y$;  stage is far easier (and safer to measure), but a rating is needed to establish accurate discharges.  

# ## Exercises
# 
