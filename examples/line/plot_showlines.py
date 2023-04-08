"""
Plot lines using showlines
==========================

.. currentmodule:: pygeode

Compute numerical integrals using :func:`Var.integrate()` and use :func:`showlines()` to make plot.
"""
# %%
# Example 1: Compute the integral of sin(x) using :func:`Var.integrate`
#
# f = sin(x)
#
# F = \int_0^x f dx' = 1 - cos(x)

import pygeode as pyg, numpy as np
import pylab as pyl

# Use longitudes as horizontal axis
x = pyg.regularlon(45)

# Convert to radians
lam = np.pi * x / 180.

f = pyg.sin(lam)

# Different numerical integration methods
Fr = f.integrate('lon', dx = lam, type='rectr')
Fl = f.integrate('lon', dx = lam, type='rectl')
Ft = f.integrate('lon', dx = lam, type='trapz')

# Plot the exact answer along with each of the numerically computed integrals
# Set line formats and labels for each plot to appear in the legend
pyl.ioff()
ax1 = pyg.showlines([1 - pyg.cosd(x), Fr, Fl, Ft], 
                   fmts = ['k-', '_', '_', 'x'], 
                   labels = [r'$1 - \cos \lambda$', 'rectr', 'rectl', 'trapz'], fig=3)

# Set panel title and axes labels
ax1.setp(title = r"$\int_0^\lambda \sin(\lambda') d\lambda'$", ylabel = '')
# Adjust size and axis padding
ax1.size = (4.1, 3)
ax1.pad = [0.5, 0.3, 0.1, 0.4]
pyl.ion()
ax1.render()

# %%
# Example 2: Compute the integral of cos(x) using :func:`Var.integrate`
# Integrate in different directions

f = pyg.cos(lam)

Ff = f.integrate('lon', dx = lam, order=1)
Fb = f.integrate('lon', dx = lam, order=-1)

pyl.ioff()
ax2 = pyg.showlines([f, Ff, Fb], 
                   fmts = ['k', '+', 'x'], 
                   labels = [r'$\cos \lambda$', 'order = 1', 'order = -1'], fig=3)

# Set panel title and axes labels
ax2.setp(title = r"$\int_0^\lambda \cos \lambda' d\lambda'$, $\int_{2\pi}^\lambda \cos \lambda' d\lambda'$", ylabel = '')
# Adjust size and axis padding
ax2.size = (4.1, 3)
ax2.pad = [0.5, 0.3, 0.1, 0.4]

pyl.ion()
ax2.render()

