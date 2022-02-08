#!/usr/bin/env python
# coding: utf-8

# # Euler and Bernoulli Equations
# 
# ## Lesson Outline
# - Applications
# -

# ### Background
# 
# The last lesson introduced the Euler (and Bernoulli) equations which are fundamental in applied fluid mechanics.
# 
# This lesson also examines applications using the equations as-is.
# 
# ### Bernoulli Equation
# 
# Recall from last time the equation of 
# 
# - steady ($\frac{\partial}{\partial t} = 0$)
# - inviscid ($ \frac{\partial V}{\partial y} = 0$)
# - gravity vector is down ($-z$)
# - incompressible ($\rho = constant$)
# - irrotational ($curl(V)=0$)
# 
# Results in 
# 
# $ \frac{p_1}{\rho g} + \frac{V_1^2}{2g} + z_1 = \frac{p_2}{\rho g} + \frac{V_2^2}{2g} + z_2  $
# 
# Below are some examples illustrating its use

# #### Example: Flow out of a holy tank
# 
# Identify the problem solving steps employed
# 
# ```{figure} bernoulli-ex1.png
# ---
# width: 600px
# name: bernoulli-ex1
# ---
# 
# ```

# #### Example: Pressure near tank outlet
# 
# Identify the problem solving steps employed
# 
# ```{figure} bernoulli-ex2.png
# ---
# width: 600px
# name: bernoulli-ex2
# ---
# 
# ```
# 
# 

# #### Example: How high will a fountain go?
# 
# Consider the fountains at a resort.  What kind of pressures and velocities are required to make the show happen?
# 
# ```{figure} bellagio.png
# ---
# width: 400px
# name: bellagio
# ---
# 
# ```
# 
# Here's a related problem that could form the basis of fountain design.
# 
# Identify the problem solving steps employed
# 
# ```{figure} bernoulli-ex3.png
# ---
# width: 600px
# name: bernoulli-ex3
# ---
# 
# ```
# 
# 

# 
# ## Readings
# 
# 1. CE-3305-2022-1 Syllabus. [http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html](http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html)
# 
# 2. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 93-177
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013.  (placeholder file to get links working). [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-5.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-5.pdf)
# 
# 4. Cleveland, T. G. (2014) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. [http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-005.0.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-005.0.pdf)
# 
# 5. De Lima, R. P., Cleveland, T. G., De Carvalho, R.P., 2014. *Infrared thermography as a heat tracer method for velocity estimation in shallow flows* [Die Bodenkultur, Journal for Land Management, Food, and Envrionment, Vol 65, No. 3-4, pp. 71-77. ISSN 006-5471](http://54.243.252.9/ce-3305-webroot/3-Readings/Thermal-Image.PDF)
