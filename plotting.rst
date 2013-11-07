==================
Plotting
==================

The plotting system in PyGeode is intended to provide sensible defaults so that
you can quickly see a reasonably annotated plot of the contents of a PyGeode
variable, but also to allow as much flexibility in customizing your plots as
possible. In general it is intended to map very closely to the matplotlib
library, and to give you access to as much of the matplotlib functionality as
possible. This tutorial is intended to introduce some of the basic concepts; a
gallery is also available with sample plots. Though you could use either
document as a starting point for plotting even without any matplotlib
experience, both will make more sense if you have had some.

There are three levels of plotting commands. The highest levels, mostly prefixed
by ``show``, make the most assumptions about the structur of the plot they
produce. The next level, prefixed with ``v``, are lower level wrappers around
matplotlib commands that are aware of PyGeode variables and try to make
formatting decisions accordingly. The lowest level are very thin wrappers around
individual matplotlib commands that know nothing about PyGeode variables, but
allow for the most direct control.

The basic high-level plotting command is :func:`showvar()`, which in its
simplest form will plot a one or two dimensional variable:

.. ipython::

  @suppress
  In [0]: import pylab as pyl; pyl.ion();

  In [1]: import pygeode as pyg; from pygeode.tutorial import t1, t2

  # A line plot
  @savefig showvar1d.png width=4in
  In [2]: pyg.showvar(t1.Temp(lat=45))

  # A contour plot
  @savefig showvar2d.png width=4in
  In [2]: pyg.showvar(t1.Temp)

The axes are labelled and formatted according to behaviour set by the axis
objects (explained in more detail below), and the title is set from the variable
name, and the coordinates of any degenerate axes. In the case of the contour
plot, a colorbar is added automatically.

Line Plots
================

If :func:`showvar()` is passed a one dimensional variable, it will produce a
line plot (ultimately using :func:`matplotlib.plot()`), automatically extracting
the coordinates and values from the variable. If the axis is recognized by
PyGeode as being a vertical axis, the plot will be transposed. This can be
reversed if desired by setting the keyword argument ``transpose = True``.

Like the plot command, the format of the line can be set by passing a string
immediately following the command; moreover, any other keyword argument
recognized by :func:`matplotlib.plot()` will be passed through. 

.. ipython::

  # A vertical plot
  @savefig lp_vertical.png width=4in
  In [2]: pyg.showvar(t2.Temp.mean('time', 'lat', 'lon'), 'k--', lw=3.)

  # A transposed plot
  @savefig lp_transpose.png width=4in
  In [2]: pyg.showvar(t2.Temp.mean('time', 'lat', 'lon'), transpose = True)

Notice that these commands all return a :class:`AxesWrapper` object - this
holds all the data and settings used to contruct your plot, and it can be used
to make further modifications. 

Contour Plots
================

Customizing contour levels



basic plotting command; plotvar

1d plots: - simple? axis annotation, titles, plotting to a particular axis, overplotting

2d plots: specifying contour levels, filled vs lines; colorbar, projection, contour labels, pcolor,
overplotting
