#!/usr/bin/env python
# coding: utf-8

# # Volumetric and Mass Flow Rate
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

# ## Example: Flow in a Rectangular Conduit
# 
# ```{figure} rect-channel.png
# ---
# width: 600px
# name: rect-channel
# ---
# 
# ```

# ## Example: Flow in a Triangular Conduit
# 
# ```{figure} v-channel.png
# ---
# width: 600px
# name: v-channel
# ---
# 
# ```
