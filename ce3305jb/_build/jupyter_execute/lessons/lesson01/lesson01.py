#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# ## Lesson Outline
# 1. Problem Solving and Documentation
#   - Problem Solving Protocol
#   - Jupyter Notebooks (preferred way to record your work)
#   - Illustrative Example
# 2. What is Fluid Mechanics?
#   - Definition of a Fluid
#   - Fundamental Properties

# ### Problem Solving and Documentation
# 
# The exercises are instruments to practice problem solving.  
# 
# - Format 
# - Process
# 
# The purpose of such practice is to:
# 
# - Develop a systematic method to solve closed (solvable) engineering problems.
# - Develop *muscle memory* to apply the process
# - Become accustomed to documenting effort
# 
# #### Suggested Protocol
# 
# 1. State the problem
# 2. Sketch the situation (sketching no matter how ugly helps organize thoughts!). Identify (list) known quantities 
# 3. Identify (list) unknown quantities 
# 4. Identify (list) governing principles and equations that appear relevant to the problem
# 5. Starting from one or more governing principles and the known quantities solve for the unknowns.
# 6. Validate/discuss results
# 
# #### Suggested Format (Paper-Based)
# 
# The format will differ slightly if you prepare a Notebook, or work the problem by-hand. Here is an example worked out on paper which will be repeated in a Notebook.
# 
# ```{figure} example-1-1.png
# ---
# width: 400px
# name: ex1-1
# ---
# Example of fluid mechanics homework problem solution format (page 1 of 4)
# ```
# {numref}`ex1-1` is a screen capture of the problem with the first four solution protocol items listed.  The author used headings (underlined) in the figure to keep track of the protocol items.  Also observe the simplistic sketch - a device to organize knowns and unknowns.
# 
# ```{figure} example-1-2.png
# ---
# width: 400px
# name: ex1-2
# ---
# Example of fluid mechanics homework problem solution format (page 2 of 4)
# ```
# {numref}`ex1-2` is a screen capture of the solution process.  Here the author uses various definitions of volumes, mass, and the ideal gas law to try to find the sought after quantity.  Part way into the solution an additional quantity was needed - simply add that known or governing principle where needed and make a note as done in the example.
# 
# ```{figure} example-1-3.png
# ---
# width: 400px
# name: ex1-3
# ---
# Example of fluid mechanics homework problem solution format (page 3 of 4)
# ```
# {numref}`ex1-3` is a screen capture of the solution.  Here the author uses the computed volumes, mass, and the ideal gas law to solve for the desired quantity.  Then a unit conversion is applied because the problem was stated in mixed (SI and Imperial) units.  Finally the results are discussed from a problem solving perspective; so years later anyone reading will understand the thinking process applied for the problem.
# 
# ```{figure} example-1-4.png
# ---
# width: 400px
# name: ex1-4
# ---
# Example of fluid mechanics homework problem solution format (page 4 of 4)
# ```
# {numref}`ex1-4` is a screen capture of a Periodic Chart of Elements.  Here it is included as a citation for the source of the molar masses of the gasses in the problem.  The URL is circled on the chart, again establishing a persistent citation to the data source.

# ### Example (Repeated as a Jupyter Notebook)
# 
# :::{note}
# Here we will repeat the example.  Because this "lesson" is actually a Jupyter Notebook, I am embedding some code directly into the "lesson" - you will not need to mix markdown code blocks with actual code in your notebooks
# :::

# ---
# **Name**<br>
# **R Number**<br>
# **Date**<br>
# 
# #### Problem Statement
# Find the total weight of a 17 $ft^3$ tank of nitrogen at 500 $psia$.  The vessel itself weighs 50 $lbf$.  The gas is stored at a temperature of 20 $^o~C$
# #### Sketch
# This is the hardest part, draw the sketch, then save as a png file and embed using
# ```
# ![](filename.png)
# ```
# like so:
# 
# ```{figure} FBD-tank.png
# ---
# width: 400px
# name: ex1-fbd
# ```
# 
# #### Known Quantities
# Here we will be mixing code and text

# In[1]:


# This is a code cell
vol_tank = 17 # tank volume in cubic feet
p_gas = 500 # gas pressure in psi
temp = 20 # gas temperature in celsius
wt_tank = 50 # tank weight in pounds


# #### Unknown Quantities
# 
# Our unknowns are
# 
# ```
# wt_gas
# wt_total = wt_tank+wt_gas
# ```
#     
# #### Governing Principles
# 1. $pV=\frac{m}{M}RT$ Ideal gas law
# 2. $wt_{total} = wt_{tank}+wt_{gas}$ Duh!
# 3. $R = 0.0821 \frac{L \cdot atm}{K \cdot mol}$ Definition of universal gas constant
# 4. $T_{K}=T_{C}+273$ Definition of Kelvin temperature scale
# 5. $1 atm = 14.7 psi$ Unit conversion
# 6. $M_{N_2} = 28.014 \frac{g}{mol}$ Molar weight of nitrogen gas 
# 
# #### Solution
# Now simply produce a sequential script to solve for total weight

# In[2]:


mwN2=28.014 # MW nitrogen
R = 0.0821 # universal gas constant
grabity = 9.8 # acceleration of gravity
vol_tank_l=vol_tank*((1/3.28)**3)*1000 # tank volume in liters
temp_k=temp+273 # temp in kelvin
p_atm=p_gas*(1/14.7) # gas pressure in atmospheres
mass_gas = (p_atm*vol_tank_l*mwN2)/(R*temp_k) # gas mass in grams
wt_gas = mass_gas*grabity/1000 # weight of gas in newtons
wt_total = wt_tank + wt_gas*(2.2)/grabity # total weight in pounds
print('Total weight = ', round(wt_total,1),' pounds')


# #### Discussion
# Probably would want a little more description in the calculation sequence, notice units are reported with the answer. If we want to get fancy, could embed a database for common gasses, and some interactive inputs - but that's overkill.  In practice, you will likely use a hybrid of paper-based and notebook-based problem solving.

# ### Definition(s)
# 
# Here we present some fundamental definitions 
# 
# #### What is a Solid?
# 
# A solid is a state of matter that maintains a definite shape and volume.   
# Generally with respect to fluid mechanics we are concerned with deformation, and rates of deformation.
# 
# ```{figure} stress-strain-solid.png
# ---
# width: 400px
# name: stress-strain-solid
# ---
# Stress-strain schematic for a solid material
# ```
# {numref}`stress-strain-solid` is a highly-conceptualized schematic of the stress-strain behavior of a solid material.
# A solid deforms, but not continuously. The deformation is proportional to the applied stress. Assuming the solid does not fail, then deformation is largely time invariant.
# 
# #### What is a Fluid?
# 
# A fluid in contrast to a solid deforms continuously, as long as stress is applied (shear in these drawings), the fluid will continue to deform.
# 
# ```{figure} stress-strain-fluid.png
# ---
# width: 400px
# name: stress-strain-fluid
# ---
# Stress-strain schematic for a fluid (gas or liquid; maybe plasma) material
# ```
# 
# {numref}`stress-strain-fluid` is a highly-conceptualized schematic of the stress-strain behavior of a fluid material.
# The deformation amount (strain) is proportional to the applied stress, and duration of application - fluid strain is time variant.
# 
# #### What is Fluid Mechanics?
# 
# The study of motion, deformation, momentum, energy and related properties of materials that cannot resist shear stress (i.e the fluid schematic above).  Fluid mechanics has practical engineering utility and many engineering problems can be addressed directly with fluid mechanics analytical methods.
# 
# ##### Continuum Mechanics
# 
# The calculus of fluid mechanics uses continuously differentiable functions and implicitly assumes a fluid is a continuum.  A usual definition is that a mass density can be defined and is controlled by the sampling volume $\Delta V$.
# 
# ```{figure} REV.png
# ---
# width: 400px
# name: REV
# ---
# Continuum and sampling volume relationship.
# ```
# {numref}`REV` is a conceptual diagram of sampling size utility. The smallest usable value $\Delta V$ is called a representative elementry volume (REV).  In later classes such minutiae has importance, here its just to be precise.  We will assume we are operating at a correct sample size unless explicitly stated otherwise.
# 
# ##### Particle Mechanics
# 
# Sometimes the concept of a fluid parcel (particle) is a useful construct.
# 
# ```{figure} Lagrangian.png
# ---
# width: 400px
# name: lagrangian
# ---
# Reference systems. Eulerian is most common in our book; but sometimes the Lagrangian system is more useful.
# ```
# {numref}`lagrangian` is a conceptual diagram of different reference systems, in particular Eulerian (which is commonly used) and Lagrangian (also common, but in different contexts). It is used when studying motion in a Lagrangian reference frame.  
# 
# A fluid parcel is a quantity of fluid with fixed identity (usually mass).
# The volume of the parcel can be finite, or infinitesmal - if infinitesmal, the parcels are called fluid particles.
# 
# In air-quality models, the parcels may represent cubic kilometers (definitely finite!) in other contexts the parcel volumes are small, and are called particles.
# 
# ### Dimensions
# 
# Dimensions are things that can be measured such as:
# - length
# - weight
# - temperature
# - speed
# - time
# 
# Most things are expressed in a set of primary dimensions defined either by
# - length-mass-acceleration or
# - length-weight-acceleration
# 
# Primary dimensions are used to construct secondary dimensions.  These secondary dimensions are often more practical in engineering
# 
# ### Units
# 
# Units are how much of a dimension is measured or counted.
# 
# A **meter** is a unit of **length**
# 
# Consistent units is a set of units with conversion factors equal to unity.  The U.S. Customary (Imperial) is conststent as is the SI (System Internationale), but mixing systems leads to spectular errors (the Hubble Telescope comes to mind!). Using a single system, when possible, reduces errors because of fewer arithmetic operations.  Many practical cases commonly use blends of both systems so unit conversions are required.  Page 9 of Hibbler et. al. contains representative tables for conversion - and the example above contained embedded conversions.
# 
# :::{note}
# A Jupyter Notebook to handle conversions should be within your skillset already, but for fun an example is below.
# :::
# <hr>

# In[3]:


# Simple script for unit conversions
lengthUS = 3.28
## lengthUS = float(input('Enter Length in feet')) # Use this line for interactive inputs
lengthSI = lengthUS*0.3048
print(round(lengthUS,3),' feet is equal to ',round(lengthSI),' meters ')


# :::{note} A on-line tool in JavaScript that handles some units is located at [http://54.243.252.9/toolbox/ordinarytools/UnitsConverterTool/UnitsConverterTool.html](http://54.243.252.9/toolbox/ordinarytools/UnitsConverterTool/UnitsConverterTool.html)
# 
# Countless conversions are on the internet, most are probably correct (but beware, your on your own if you don't understand the conversion and trust without verification!
# :::
# 
# ## Readings
# 
# 1. CE-3305-2022-1 Syllabus. [http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html](http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html)
# 
# 2. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 3-14
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013.  (placeholder file to get links working). [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-1.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-1.pdf)
# 

# In[ ]:




