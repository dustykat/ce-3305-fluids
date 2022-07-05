#!/usr/bin/env python
# coding: utf-8

# # Fluid Mechanics - A definition
# Clearly to define fluid mechanics requires some discourse on various states of matter 
# 
# ## What is a Solid?
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
# ## What is a Fluid?
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
# ## What is Fluid Mechanics?
# 
# The study of motion, deformation, momentum, energy and related properties of materials that cannot resist shear stress (i.e the fluid schematic above).  Fluid mechanics has practical engineering utility and many engineering problems can be addressed directly with fluid mechanics analytical methods.
# 
# ### Continuum Mechanics
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
# ### Particle Mechanics
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
