"""
Plot multiple lines using showlines()
======================================

.. currentmodule:: pygeode

In this example we'll illustrate plotting multiple lines on a single plot using
:func:`showlines()`. We also illustrate various ways of computing numerical
integrals using :func:`Var.integrate()`.
"""
# %%
# Example 1: Compute the integral of sin(x) using :func:`Var.integrate` using different
# methods and compare against the analytical solution:
#
# f = sin(x)
#
# F = \int_0^x f dx' = 1 - cos(x)

import pygeode as pyg, numpy as np
import pylab as pyl

# Use longitudes as horizontal axis; we'll use a coarse grid (21 values between
# 0 and 360 degrees including both end points) to make the differences between
# the numerical and exact answers more obvious
x = pyg.regularlon(20, repeat_origin=True)

# Convert to radians
lam = np.pi * x / 180.

f = pyg.sin(lam)

# Different numerical integration methods
Fr = f.integrate('lon', dx = lam, type='rectr')
Fl = f.integrate('lon', dx = lam, type='rectl')
Ft = f.integrate('lon', dx = lam, type='trapz')

# Plot the exact answer along with each of the numerically computed integrals
# Set line formats and labels for each plot to appear in the legend
# Set as well the size of the figure
pyl.ioff()
ax1 = pyg.showlines([1 - pyg.cos(lam), Fr, Fl, Ft], 
                   fmts = ['k-', '+', '+', 'x'], 
                   labels = [r'$1 - \cos \lambda$', 'rectr', 'rectl', 'trapz'],
                   size = (4.1, 3))

# Set panel title and axes labels
ax1.setp(title = r"$\int_0^\lambda \sin(\lambda') d\lambda'$", ylabel = '')

pyl.ion()
ax1.render()

# %%
# Example 2: Compute the integral of cos(x) using :func:`Var.integrate`
# Integrate in different directions

f = pyg.cos(lam)

# Ff = \int_0^x cos(x) dx' = sin(x)
Ff = f.integrate('lon', dx = lam, type='trapz', order=1)
# Fb = \int_x^2 pi cos(x) dx' = -sin(x)
Fb = f.integrate('lon', dx = lam, type='trapz', order=-1)

pyl.ioff()
ax2 = pyg.showlines([f, Ff, Fb], 
                   fmts = ['k', '+', 'x'], 
                   labels = [r'$\cos \lambda$', 'order = 1', 'order = -1'])

# Set panel title and axes labels
ax2.setp(title = r"$\int_0^\lambda \cos \lambda' d\lambda'$, $\int_{2\pi}^\lambda \cos \lambda' d\lambda'$", ylabel = '')

# Another way to adjust the figure size and padding around the axes
ax2.size = (4.1, 3)
ax2.pad = [0.5, 0.3, 0.1, 0.4]

pyl.ion()
ax2.render()

