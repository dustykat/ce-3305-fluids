#!/usr/bin/env python
# coding: utf-8

# # Pressure Force on Submerged Objects (pp 64-78)
# 
# Now we consider the forces generated on submerged objects by hydrostatic pressure.  
# It's the same force you feel on your [耳](https://translate.yandex.com/?lang=en-ja&text=ears) when you dive to the bottom of a [schwimmbad](https://dictionary.cambridge.org/us/dictionary/german-english/schwimmbad).
# 
# :::{note}
# I am having a little fun with the language translators on Google; the sentence in English is "... It's the same force you feel on your ears when you dive to the bottom of a swimming pool".
# :::
# 
# ## Uniform Pressure
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
# ## Distributed Pressure
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

# In[ ]:




