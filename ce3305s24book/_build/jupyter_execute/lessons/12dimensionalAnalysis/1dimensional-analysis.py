#!/usr/bin/env python
# coding: utf-8

# # Dimensional Analysis
# 
# :::{admonition} Course Website
# [http://54.243.252.9/ce-3305-webroot/](http://54.243.252.9/ce-3305-webroot/)
# :::
# 
# Fluid mechanics design problems rely upon experimental data, either collected directly or inferred from prior published works.  In most cases empirical results do not directly apply to general situations so engineers need to interpret the original data in normal design practice.
# 
# Such data are found in handbooks, journals, and other authorative sources.  Some examples are friction loss coefficients for pipes, valves, and other fittings; drag coefficients; fluid properties. 
# 
# **Dimensional Analysis** is a tool used to guide such expermental design and practice and reduce the number of experiments required. **Similitude** is a tool used to *scale* laboratory results to full-scale situations.
# 

# 
# ## Readings
# 
# 1. Hibbeler, R.C, Fluid Mechanics, 2ed. Prentice Hall, 2018. ISBN: 9780134655413 pp. 444-469
# 
# 3. DF Elger, BC Williams, Crowe, CT and JA Roberson, *Engineering Fluid Mechanics 10th edition*, John Wiley & Sons, Inc., 2013.  (placeholder file to get links working). [http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-10.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/EFM-10.pdf)
# 
# 4. Cleveland, T. G. (2014) *Fluid Mechanics Notes to Accompany CE 3305 at Jade-Holshule (TTU Study Abroad 2015-2019)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. [http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture11.pdf](http://54.243.252.9/ce-3305-webroot/3-Readings/ce3305-lecture11.pdf)
# 
# 5. Cleveland, T. G. (2009) [Error Analysis](http://54.243.252.9/ce-3305-webroot/3-Readings/ce_5333_1.1_error_analysis.pdf) in *Instructor Notes to Accompany CE 5333 Studies in Dimensional Analysis and Similitude*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. 
# 
# 5. Cleveland, T. G. (2009) [Propagation of Error](http://54.243.252.9/ce-3305-webroot/3-Readings/ce_5333_1.2_error_analysis.pdf) in *Instructor Notes to Accompany CE 5333 Studies in Dimensional Analysis and Similitude*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. 
# 
# 5. Cleveland, T. G. (2009) [Dimensional Analysis](http://54.243.252.9/ce-3305-webroot/3-Readings/ce_5333_2.1_dimensional_analysis.pdf) in *Instructor Notes to Accompany CE 5333 Studies in Dimensional Analysis and Similitude*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. 
# 
# 5. Doebelin, E. O. (1990). Measurement Systems (4th ed.). New York, NY: McGraw-Hill.
# 
# 6. Holman, J. P. (1989). [Analysis of Experimental Data](http://54.243.252.9/ce-3305-webroot/3-Readings/holman1989.pdf) in *Experimental Methods for Engineers, 5th Edition.* New York, NY: McGraw-Hill.
# 
# 7. Kline, S. J. and F. A. McClintock (1953). [Describing uncertainties in single-sample experiments](http://54.243.252.9/ce-3305-webroot/3-Readings/Kline_McClintock1953.pdf). Mechanical Engineering (No. 75), 3–9.
# 
# 8. Buckingham, E. (1915). Model experiments and the forms of empirical equations. Transactions of American Society of Mechancial Engineers (No. 37), 263.
# 
# 9. Hwang, N. H. C. and C. E. Hita (1987). [Dimensional Analysis](http://54.243.252.9/ce-3305-webroot/3-Readings/hwang_1987_selected_readings.pdf) in *Fundamentals of Hydraulic Engineering Systems*. San Diego, CA: Prentice Hall. 
# 
# 10. White, F. M. (1979). Fluid Mechanics. New York, NY: McGraw-Hill <br> [Dimensional Analysis Part 1](http://54.243.252.9/ce-3305-webroot/3-Readings/white_1979_part1.pdf)<br> [Dimensional Analysis Part 2](http://54.243.252.9/ce-3305-webroot/3-Readings/white_1979_part2.pdf)<br> [Dimensional Analysis Part 3](http://54.243.252.9/ce-3305-webroot/3-Readings/white_1979_part3.pdf)<br>[Dimensional Analysis Part 4](http://54.243.252.9/ce-3305-webroot/3-Readings/white_1979_part4.pdf)
#  

# ## Videos
# 1. [placeholder](placeholder)

# ## Lesson Outline
# 1. Dimensionless ($\pi$) groups
# 2. Important dimensionless numbers
# 3.  Buckingham $\Pi$ Theorem
# 
# ---

# 
# 
# 
# 

# ## Example 1: 

# In[1]:


# computational thinning
import math
q = 0.1 #discharge
v_jet = 50.0
omega = 500*2*math.pi/60
radius = 0.5
rho = 1000.0
power = rho*q*v_jet*radius*omega - rho*q*omega**2*radius**2
print("Power ",round(power,2)," Newton-meters/sec    ")


# ## Example 2: 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




