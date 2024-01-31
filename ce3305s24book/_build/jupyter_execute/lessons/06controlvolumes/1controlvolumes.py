#!/usr/bin/env python
# coding: utf-8

# # Control Volumes (pp. 178)
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
# The control volume is the basis of Reynolds' transport theorem that is employed to allow analysis from a Eulerian reference frame rather than tracking individual particles.  The goal is to describe fundamental laws of mechanics in integral form
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
# > ## Conservation of mass (continunity)<br>
# >
# > $\frac{dm}{dt}|_{sys} = 0$
# >
# > ## Conservation of linear momentum <br>
# >
# > $m\frac{d\bar V}{dt}|_{sys} = \sum \bar F$
# >
# > ## Conservation of angular momentum <br>
# >
# > $m\frac{d\bar \omega}{dt}|_{sys} = \sum (\bar r \times \bar F)$
# >
# > ## Conservation of energy<br>
# >
# > $\frac{E}{dt}|_{sys} = \frac{dQ}{dt} - \frac{dW}{dt}$
# >
# > where $Q$ is heat flow into the system and $W$ is work done by the system.
# >
# > ## Entropy principle<br>
# >
# > $\frac{S}{dt}|_{sys} >= \frac{1}{T}\frac{dQ}{dt}$
# >
# > where $Q$ is heat flow into the system, S is entropy, and T is the absolute temperature of the system.
# 
# The first four conservation principles are the most useful in fluid mechanics problems; the last principle is applied in various forms in mechanical and chemical thermodynamics problems - its relevant in Civil and Environmental Engineering, but covered in later classes.

# In[ ]:




