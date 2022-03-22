#!/usr/bin/env python
# coding: utf-8

# # Closed Conduit (Pipe) Flow
# 
# ## Lesson Outline
# - Analyze and design pipe systems with various fittings and connections
# - topic

# ### Background
# 
# 
# ```{note}
# Energy (head) losses in conduits (pipes) arise from frictional losses at the pipe wall (major loss), and additional losses from fittings (minor losses).  
# Major and minor refer to the distances over which the losses occur, and not the magnitude.
# ```
# 
# Recall the modified bernoulli equation for a pipeline system
# 
# $$\frac{p_1}{\rho g}+\frac{V_1^2}{2g}+z_1+h_p = \frac{p_2}{\rho g}+\frac{V_2^2}{2g}+z_2+h_T +h_{loss}$$
# 
# Examine the $h_{loss}$ term:
# 
# $$h_{loss} = f\frac{L}{D}\frac{V^2}{2g} + \sum_{i=1}^{n_{fit}} K_i \frac{V_i^2}{2g} $$
# 
# The first part is the pipeline (major) loss (using the Darcy-Weisbach head loss model), the second part is the fitting losses.
# 
# The kinds of fittings include:
# 
# - Entrances and exits as depicted below
# 
# ```{figure} entrance-effects.png
# ---
# width: 400px
# name: entrance-effects
# ---
# Entrances and exits
# ```
# 
# - Bends, transitions, and valves
# 
# ```{figure} fittings.png
# ---
# width: 400px
# name: fittings
# ---
# Classes of fittings
# ```
# 
# The loss coefficients are tabulated and nearly always require some kind of table look-up.  Here are a few examples:
# 
# - [K-values neutrium.net](https://neutrium.net/fluid-flow/pressure-loss-from-fittings-excess-head-k-method/)
# - [K-values metropumps.com](http://www.metropumps.com/ResourcesFrictionLossData.pdf)
# - [K-values powderprocess.net](https://powderprocess.net/Tools_html/Piping/Pressure_Drop_Key_Piping_Elements_K_Coefficient.html)

# ## Example 1: 
# 
# (Pg 532 Hibbler) The 6-inch diameter galvanized iron pipe depicted below transports water from a reservoir at a temperature of 100$^o~F$.  Determine the head loss and pressure drop in 200 feet of pipe for a discharge of $Q=400~gpm$
# 
# ```{figure} IMG-6180.png
# ---
# width: 400px
# name: IMG-6180
# ---
# Sketch of pipeline situation
# ```
# 
# ### Sketch
# 
# Above 
# 
# ### Known
# 
# $Q=400~gpm$<br>
# $D=0.5~ft$<br>
# material = "galvanized iron pipe" (use to find roughness height)<br>
# $L=200~ft$<br>
# $T=100^o~F$<br>
# 
# ### Unknown
# 
# $h_f$<br>
# $\Delta p$<br>
# 
# ### Governing Equations
# 
# - Darcy-Wiseass head loss model $h_f=f\frac{L}{D}\frac{V^2}{2g}$ 
# - Reynolds' number $Re_d = \frac{VD}{\nu}$
# - Modified bernoulli equation (to find $\Delta p$)
# 
# ### Analysis (Solution)
# 
# - Starting with the given temperature find the necessary water properties; easiest to use an on-line resource such as [http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesUS/WaterPropertiesUS.html](http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesUS/WaterPropertiesUS.html)
# 
# The relevant properties are displayed below 
# 
# ```{figure} fluid-properties14.png
# ---
# width: 400px
# name: fluid-properties14
# ---
# Fluid Properties On-line Database
# ```
# 
# Now we can compute the Reynolds number as depicted below; first a prototype function.

# In[1]:


# reynolds number function - execute this cell to prototype the function
def reynolds(velocity,diameter,viscosity):
    reynolds = velocity*diameter/viscosity
    return(reynolds)


# Then the actual computations

# In[2]:


# compute the reynolds number
gpm = 400
diam = 0.5
long = 200
grav = 32.2
# gpm to cfs
cfs = gpm*(1/60)*(1/7.48)
import math
area = 0.25*math.pi*diam**2
vel = cfs/area
nu = 7.39e-06 # from the database lookup
Re = reynolds(vel,diam,nu)
if Re > 2300:
    print("Reynolds number:",round(Re,3)," flow is turbulent")
if Re >= 2000 and Re <=2300:
    print("Reynolds number:",round(Re,3)," flow is transitional")
if Re < 2000:
    print("Reynolds number:",round(Re,3)," flow is laminar")


# Next we need to find the roughness height from the material describtion, again an on-line tool is helpful [http://54.243.252.9/toolbox/Databases/RoughnessHeight/RoughnessHeight.html](http://54.243.252.9/toolbox/Databases/RoughnessHeight/RoughnessHeight.html)
# 
# ```{figure} roughness14.png
# ---
# width: 400px
# name: roughness14
# ---
# Galvanized Iron Roughness from On-line Database
# ```
# 
# With the roughness height we can complete the analysis.

# In[3]:


roughness = 0.15 #mm
roughness = roughness/25.4/12 #mm to inches, inches to feet
relative_roughness = roughness/diam
print("Relative roughness",relative_roughness)


# Use this value to find a friction factor, easiest to use the Jain equation(s)
# 
# $$f = \frac{0.25}{[log_{10}(\frac{K_s}{3.7D} + \frac{5.74}{Re^{0.9}})]^2}$$

# In[4]:


def friction_fact(roughness,diameter,reynolds):
    import math
    numerator = 0.25
    denominator = math.log10((roughness/(3.7*diameter)) + (5.74/reynolds**0.9))
    ratio = numerator/denominator**2
    return(ratio)

ff = friction_fact(roughness,diam,Re)
print("Friction factor :",round(ff,4))


# Now we can compute the head loss

# In[5]:


headloss = ff*(long/diam)*((vel**2)/(2*grav))
print("Head loss :",round(headloss,3))


# Now to find the pressure drop, we simply express the head loss as an equivalent pressure (assuming horizontal pipe) using the modified bernoulli equation.
# 
# Start with:
# 
# $$\frac{p_1}{\rho g}+\frac{V_1^2}{2g}+z_1+h_p = \frac{p_2}{\rho g}+\frac{V_2^2}{2g}+z_2+h_T +h_{loss}$$
# 
# No pumps or turbines, horizontal, constant diameter pipe all thats left is
# 
# $$\frac{p_1}{\rho g} = \frac{p_2}{\rho g} +h_{loss}$$
# 
# or
# 
# $$\frac{p_1}{\rho g} - \frac{p_2}{\rho g} = \frac{\Delta p}{\rho g} = h_{loss}$$

# In[6]:


deltap = headloss*62.0 # use density for 100F wasser
deltap = deltap*(1/12)*(1/12) # convert psf to psi
print("Pressure drop",round(deltap,3)," psi ")


# ### Discussion of Results

# 

# ## Example 2: 
# 
# Commerical steel pipe in the sketch below has a diameter of 3-inches and transfers glycerin from the tank to a mixing basin at outlet $B$.  The tank is vented at the top as shown. Determine the initial discharge at $B$ when the gate valve at $C$ is fully opened.  
# 
# ```{figure} tank-drain14.png
# ---
# width: 400px
# name: tank-drain14
# ---
# Sketch of Chemical Transfer Tank System
# ```
# 
# ### Sketch
# 
# Above, nothing special to add
# 
# ### Known
# 
# ```{figure} fluid-properties14-2.png
# ---
# width: 400px
# name: fluid-properties14-2
# ---
# Typical Tabulated Fluid Properties
# ```
# 
# Fluid properties: glycerine $\rho= 2.45 slug/ft^3 $,$\nu= 1.22 \times 10^{-2}~ft^2/s$<br>
# Minor Loss Components: 2 Elbows $K_{elb}=0.9$, Flush Entrance $K_{ent}=0.5$, Gate valve $K_{v}=0.19$<br>
# 
# ### Unknown
# 
# $Q_{initial}$ before the liquid level drops very much.  We will stipulste that valve is opened quickly and flow develops rapidly before liquid level drops very much.
# 
# ### Governing Principles
# 
# - Darcy-Weisbach head loss model $h_{loss}=f\frac{L}{D}\frac{V^2}{2g} + \sum_i{K\frac{V^2}{2g}}$ 
# - Reynolds' number definition $Re_d = \frac{VD}{\nu}$
# - Modified bernoulli equation $\frac{p_1}{\rho g}+\frac{V_1^2}{2g}+z_1+h_p = \frac{p_2}{\rho g}+\frac{V_2^2}{2g}+z_2+h_T +h_{loss}$

# ### Analysis (Solution)
# 
# - Starting with the given fluid find the necessary properties (which are already displayed)
# - Stipulate the CV will be applied from $A$ to $B$ with tha datum set at $B$.
# - Apply the modified bernoulli equation: 
# 
# $\frac{p_1}{\rho g}+\frac{V_1^2}{2g}+z_1+h_p = \frac{p_2}{\rho g}+\frac{V_2^2}{2g}+z_2+h_T +h_{loss}$
# 
# - Substutute the DW head loss model into the modified bernoulli equation
# 
# $\frac{p_A}{\rho g}+\frac{V_A^2}{2g}+z_A+h_p = \frac{p_B}{\rho g}+\frac{V_B^2}{2g}+z_B+h_T +f\frac{L}{D}\frac{V^2}{2g} + K_{ent}\frac{V^2}{2g} + 2*K_{elbow}\frac{V^2}{2g}+K_{valve}\frac{V^2}{2g}$
# 
# - Insert loss coefficient values (remove the pump and turbine, they do not exist in this example)
# 
# $$z_A = \frac{V_B^2}{2g} +f\frac{L}{D}\frac{V^2}{2g} + 0.5\frac{V^2}{2g} + 2*0.9\frac{V^2}{2g}+0.19\frac{V^2}{2g}$$
# 
# - Insert numerical values
# 
# $$8 = \frac{V_B^2}{2g} +f\frac{18}{0.25}\frac{V^2}{64.4} + 0.5\frac{V^2}{64.4} + 2*0.9\frac{V^2}{64.4}+0.19\frac{V^2}{64.4}$$
# 
# - Algebra
# 
# $$8 = (72f + 3.49)\frac{V^2}{64.4} $$

# In[ ]:





# 
# ## Readings
# 
# 1. CE-3305-2022-1 Syllabus. [http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html](http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html)
# 
# 2. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 517-539
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013. [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-13.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-13.pdf)
# 
# 4. Cleveland, T. G. (2014) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. [http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture13.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture13.pdf)
# 
#  

# In[ ]:





# In[ ]:




