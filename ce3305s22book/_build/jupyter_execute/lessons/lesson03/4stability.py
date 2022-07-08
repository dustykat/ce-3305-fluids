#!/usr/bin/env python
# coding: utf-8

# # Stability
# 
# A floating body is STABLE if, when it is displaced, it returns to equilibrium.
# A floating body is UNSTABLE if, when it is displaced, it continues to move to a new equilibrium.
# 
# ```{figure} stability-1.png
# ---
# width: 400px
# name: stability-1
# ---
# Object floating in some liquid; tilted a bit - if the bouyancy-weight couple tends to return to initial position, then stable - otherwise will continue to overturn.
# ```
# 
# Consider a floating body tilted by an angle $\Delta \Theta$, as shown in {numref}`stability-1`. For the untilted body the point G is
# the centre of gravity of the body where the body weight, W, acts. The point B is the center of buoyancy
# (the centroid of the displaced volume of fluid) where the upward buoyancy force, FB, acts.
# 
# When the body is tilted the centre of buoyancy moves to a new position, B', because the shape of the
# displaced volume changes. A new point, M, may be defined, called the METACENTRE. This is the
# point where a vertical line drawn upwards from the new centre of buoyancy, B', of the tilted body
# intersects the line of symmetry of the body. The buoyancy force, FB, now acts through B'.
# 
# From the center diagram in the figure we observe that W and FB generate a RESTORING MOMENT (Righting Moment) that
# rotates the body back to its untilted position. From the right hand diagram in the figure we can see that
# W and FB generate an OVERTURNING MOMENT that rotates the body even further in the tilted direction (the body gets too turnt!).
# 
# Thus; if the metacenter, M, lies above the center of gravity, G, then the body is stable. In
# other words the METACENTRIC HEIGHT, MG, is positive ($MG = z_M - z_G > 0$). If the metacentre, M,
# lies below the centre of gravity, G, then the body is unstable. In other words the metacentric height, MG, is negative (MG < 0).
# 
# ```{figure} stability-2.png
# ---
# width: 400px
# name: stability-2
# ---
# Reference sketch for center of bouyancy and metacenter distances.
# ```
# 
# The metacentric height, MG, is given by $$ MG = MB - GB = \frac{I}{V_s} - GB$$,
# where where I is the 2nd moment of area of the plan section of the body
# where it cuts the waterline (this is the solid plane surface you’d see
# if you cut horizontally through a solid body at the water surface
# lifted the top part up and looked at the bottom of it!), VS is the
# submerged volume (i.e. volume of fluid displaced) and GB is the
# distance between the centre of gravity and the centre of buoyancy
# ($= z_G – z_B$). {numref}`stability-2` is a reference sketch for the various distances.

# ## Strategy for solving buoyancy/stability problems
# The usual problem solving protocol works fine, but the additional governing principles/solution algorithm include:
# 
# 1. From geometry of body and density of fluid and body equate; Weight of displaced fluid = Total weight of body. This gives the depth of immersion of the body or the weight of the body, whichever is unknown.
# 2. To assess stability, first find the location of the centre of gravity G of the body.
# 3. Then, find the location of the centre of buoyancy B (centroid of displaced volume). For a regularly shaped body this will be at half the height of the immersed portion of the body.
# 4. Calculate the distance GB.
# 5. Calculate MB, using MB = I / VS. Note $I = \pi \frac{D^4}{64}$ for a circular section body and $\frac{bd^3}{12}$ for a rectangular section body (D is diameter, b and d are the sides of the rectangle).
# 6. Calculate metacentric height, $MG (= z_M – z_G)$, from MG = MB – GB. If MG > 0 then body is stable. If MG < 0 then body is unstable.

# ## Example
# 
# A solid cylindrical pine (SG=0.5) [spar buoy](https://norfloat.com/aids-to-navigation/navigation-buoys-intro/channel-marker-spar-buoys/) has a cylindrical lead (SG=11.3) weight attached as
# shown in {numref}`stability-example`. 
# 
# ```{figure} stability-example.png
# ---
# width: 400px
# name: stability-example
# ---
# Schematic of a spar buoy.
# ```
# 
# Determine: 
# 1. The equilibrium position (i.e. depth of immersion) of the buoy in seawater (SG=1.03). 
# 2. The metacentric height and show that the buoy is stable.

# In[1]:


# sketch here


# In[2]:


# list known quantities


# In[3]:


# list unknown quantities


# ### governing principles
# Weight of fluid displaced = Weight of body

# ### solution (step-by-step)
# 

# # discussion
# 
# N
# become unstable? If the buoy is stable when MG > 0 and unstable when MG < 0, we can say that the
# limit between being stable or unstable is when MG = 0. In this case MB = GB. If you do the problem
# again, setting the length of the pine section as L (instead of 4.88m), and equating MB = GB, you can
# solve for L (by trial and error) to give the maximum length before instability sets in. 
