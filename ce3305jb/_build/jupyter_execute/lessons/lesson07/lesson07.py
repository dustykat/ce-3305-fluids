#!/usr/bin/env python
# coding: utf-8

# # Control Volume Analysis
# 
# ## Lesson Outline
# - Control Volumes
# - Concepts of Flux (a prelude to Reynolds Transport Theorem)

# ### Background
# 
# This lesson introduces the concept of control volumes for analysis of fluids problems.
# 
# ### Control Volumes
# 
# A control volume (CV) is the equivalent of a free-body diagram in other fields of engineering mechanics (statics, dynamics).
# 
# A control volume is some defined area in space, as depicted by the cube below.  
# 
# ```{figure} control-volume.png
# ---
# width: 600px
# name: control-volume
# ---
# 
# ```
# 
# ```{note}
# The control volume is the basis of reynold's transport theorem that is employed to allow analysis from a Eulerian reference frame rather than tracking individual particles.  The goal is to describe fundamental laws of mechanics in integral form
# ```
# The bounding surface is called the *control surface* (CS)
# 
# ```{figure} cs-areas.png
# ---
# width: 600px
# name: cs-areas
# ---
# 
# ```
# The outward pointing area vectors for each face are shown above; these play an important role in application of CV analysis.
# 
# The principle is to express various conservation principles in integral form including:
# 
# > #### Conservation of mass (continunity)
# >
# > $\frac{dm}{dt}|_{sys} = 0$
# 
# > #### Conservation of linear momentum 
# >
# > $m\frac{d\bar V}{dt}|_{sys} = \sum \bar F$
# 
# > #### Conservation of angular momentum 
# >
# > $m\frac{d\bar \omega}{dt}|_{sys} = \sum (\bar r \times \bar F)$
# 
# > #### Conservation of energy
# >
# > $\frac{E}{dt}|_{sys} = \frac{dQ}{dt} - \frac{dW}{dt}$
# >
# > where $Q$ is heat flow into the system and $W$ is work done by the system.
# 
# > #### Entropy principle
# >
# > $\frac{S}{dt}|_{sys} >= \frac{1}{T}\frac{dQ}{dt}$
# >
# > where $Q$ is heat flow into the system, S is entropy, and T is the absolute temperature of the system.
# 
# The first four conservation principles are the most useful in fluid mechanics problems.
# 
# 

# ### CV Relationships for Mass Conservation (Continunity)
# 
# To use CV analysis the system equations are converted to volume variation relations.
# 
# Recall that extensive properties are defined throughout an entire mass of a fluid (a system) whereas intensive properties are an amount of property per unit mass.
# 
# Starting with mass itself, the extensive property is mass $m$
# 
# The mass per unit mass is unity; $\frac{m}{m}=1$
# 
# The mass per unit volume is density; $\frac{m}{V}=\rho$
# 
# <!--
# The fundamental relationship of the system is:
# 
# $B_{sys} = \int \beta dm = \int \beta \rho dV$ -->
# 
# In the case of mass we have
# 
# ```{figure} rtt-mass.png
# ---
# width: 600px
# name: rtt-mass
# ---
# 
# ```
# Now consider a system (gold cube in the figure at time $t=t_0$
# 
# 
# ```{figure} rtt-mass-t0.png
# ---
# width: 600px
# name: rtt-mass-t0
# ---
# 
# ```
# 
# A short time ($t+\Delta t$) later the system has moved, some parts have left the CV.
# 
# 
# ```{figure} rtt-mass-tdt.png
# ---
# width: 600px
# name: rtt-mass-tdt
# ---
# 
# ```
# 
# Examination of the three zones and the system total mass gives:
# 
# 
# ```{figure} rtt-mass-tdt-1.png
# ---
# width: 600px
# name: rtt-mass-tdt-1
# ---
# 
# ```
# 
# Inserting these into the system to volume expression:
# 
# ```{figure} rtt-mass-tdt-2.png
# ---
# width: 600px
# name: rtt-mass-tdt-2
# ---
# 
# ```
# 
# Now using the divergence theroem to cope with the terms in Parts I and III of space in the drawing
# 
# ```{figure} divergence.png
# ---
# width: 600px
# name: divergence
# ---
# 
# ```
#  The application of Gauss' divergence theorem produces the "flux integrals".
# 
# ```{figure} divergence-2.png
# ---
# width: 600px
# name: divergence-2
# ---
# 
# ```
# 
# Now examine the relationship between velocity and area in the flux integrals
# 
# ```{figure} vdotDA.png
# ---
# width: 600px
# name: vdotDA
# ---
# 
# ```
# 
# Collect the terms together into the Reynolds Transport Expression for Mass
# 
# ```{figure} RTT-MassBalance.png
# ---
# width: 600px
# name: RTT-MassBalance
# ---
# 
# ```
# 
# To summarize:
#  
# 
# ```{figure} rtt-summary.png
# ---
# width: 600px
# name: rtt-summary
# ---
# 
# ```

# ## Example 1: Appliocation of Continunity to a Holy Grail
# 
# ```{figure} example-1.png
# ---
# width: 600px
# name: example-1
# ---
# 
# ```

# 
# ## Readings
# 
# 1. CE-3305-2022-1 Syllabus. [http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html](http://54.243.252.9/ce-3305-webroot/0-Syllabus/ce-3305-2022-1-syllabus.html)
# 
# 2. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 177-
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013.  (placeholder file to get links working). [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-8.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-8.pdf)
# 
# 4. Cleveland, T. G. (2014) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. [http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-7.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture-7.pdf)
# 
