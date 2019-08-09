================
Basic Operations
================

.. currentmodule:: pygeode

Much of the functionality of PyGeode is found in the operations you can perform
on Var objects. We'll start with the basics of slicing variables, then move on
to more complicated operations. An important thing to keep in mind, as
discussed in :doc:`tut_gettingstarted`, is that these operations all delayed until
the data is specifically requested. For instance, one can compute an average
over longitude as follows:

.. ipython::

  In [6]: import pylab as pyl; pyl.ion();

  In [1]: import pygeode as pyg

  In [2]: from pygeode.tutorial import t1

  In [3]: t_av = t1.Temp.mean('lon') # Fast: no computations carried out

However, while the variable ``t_av`` now represents this average (and one
can carry out further operations with it), no actual averaging has been done.
This only happens when the data itself is requested (either explicitly as a
numpy array as below, or when writing the data to disk, or plotting it):

.. ipython::

  In [4]: print(t_av[:]) # Slower: data is loaded, and the averaging is carried out

This should be kept in mind for the rest of the tutorial! We'll get a bit lazy:
what line 3 in the code above really does is return a new PyGeode variable
that represents the mean over the longitude axis of the source variable, without
actually calculating the mean, but we'll just say that we've computed the mean.
All of the operations in this section work this way - in fact, almost all of the
functions in PyGeode do, with a few exceptions that we'll mention explicitly
when we get there.

Selecting subsets
------------------

Reference: :meth:`Var.__call__`

One of the most basic operations is to select a subset or subdomain of your
variable. For instance, to select a rectangular region of the same temperature
variable we just saw:

.. ipython::

  In [5]: print(t1.Temp(lat=(30, 50), lon=(100, 180)))
  
  # We can take a look at the latitude grid points for reference
  In [6]: t1.Temp.lat[:] 

PyGeode makes use of the calling syntax of Python to do slicing. While this is
arguably an abuse of the syntax, this operation is so common that it's a
default behaviour for PyGeode variables. The axes are specified as keyword
arguments, and ranges are given as a tuple in coordinate space (as opposed to
the indices). Not all axes need be specified: any axes not mentioned are left
alone. Note that the subset includes elements lying on and within the
boundaries of the range requested (30 N to 50 N in this case). To demonstrate
this we've printed out the grid points of the latitude axis in line 6; so one
can see that this call returns a subset from latitude 30 N (on the boundary of
the range requested) to 48 N, since the next grid point is at 54 N. 

You can also request a single element. The returned variable will always have
the same number of dimensions as the source variable (in the same order, though
not necessarily the same length), even if some of them are of length 1. 

.. ipython::

  In [6]: print(t1.Temp(lat=12))

If the (zero-based) index is more convenient, you can specify this by prefixing
the axis name with ``i_``:

.. ipython::

  In [5]: print(t1.Temp(i_lat=5).lat)

Negative values index the axes in reverse, as in Python:

.. ipython::

  In [5]: print(t1.Temp(i_lat=-5).lat)

Another useful prefix is ``l_``, which lets you select an arbitrary set of
points:

.. ipython::

  In [7]: print(t1.Temp(l_lat=(-25, 0, 60, 92)).lat.values)

You'll notice that if the requested value lies between two grid points in the
subsetted axis (``lat`` in this case), the closer of the two will be returned.
This is also the case for values lying outside the range of the axis - this can
lead to some surprises if the axes has a different range than you expect. This
'nearest match' behaviour only holds for floating-point valued axes -
integer-valued axes (such as those that might index members of an ensemble, for
instance) only return exact matches. 

The subsetted axis will always retain the order of the source axis, regardless
of what order you give the list. There are some other useful shortcuts here, but
we'll introduce them a bit later on. In most cases, these prefix shortcuts can
be combined, so that ``li_`` can be used to select a list based on indices of
the subsetted axes instead of values.

Time axes are a bit of special case. PyGeode has a reasonably sophisticated
time axis, which is aware of four types of calendars - the standard Gregorian
calendar (:class:`StandardTime`), a 365-day calendar (:class:`ModelTime365`), a
360-day calendar (:class:`ModelTime360`), and a yearless calendar
(:class:`Yearless`), which might better be described as a time axis with no
calendar at all. The example data set ``t2``, for instance, is defined on a
365-day calendar. These are represented internally as a list of offsets (in
this case in days) from a reference date:

.. ipython::

  In [10]: from pygeode.tutorial import t2

  In [5]: print(t2.time.startdate)

  In [5]: print(t2.time.values)

Time axes can be subsetted exactly as above, in which case the requested value
is matched against this offset:

.. ipython::

  In [5]: print(t2.Temp(time=8).time)

However, these can be difficult to use directly, and can easily correspond to
very different dates if two time axes have different reference dates. Other
possibilities exist:

.. ipython::

  # Select a range of dates, from 12 December 2013 to 18 January 2014
  In [5]: print(t2.Temp(time=('12 Dec 2013', '18 Jan 2014')).time)

PyGeode also recognizes the format ``16:00 13 May 1982`` if a more precise
specification is required.

.. ipython::

  # Select all elements in year 2013
  In [5]: print(t2.Temp(year = 2013).time)

  # Select all elements in any January, February or December
  In [5]: print(t2.Temp(l_month = (1, 2, 12)).time)

These last two are particularly useful constructs; you will have noticed that
axes need not be regularly spaced. Note that ``year`` and ``month`` here are
not axes of ``t2.Temp`` -- they are technically 'auxilliary arrays' of the time
axis; this detail doesn't much matter for users, except that while in most
cases they behave exactly as if they were an axis for the purpose of subsetting
variables, not all prefixes work. In particular the prefix ``i_`` is not
recognized.  ``day``, ``hour``, ``minute``, and ``second`` work in the same
way. More details about time axes can be found here :ref:`timeaxisops`.

These examples all return a new PyGeode variable, as explained at the beginning
of the section. If you ever do just need the raw numerical data (in the form of
a numpy array), you can use standard slicing notation on a pygeode variable
(``t1.Temp[:]`` will return everything). Note that, unlike keyword-based subsetting, 
but like the behaviour expected with selecting out of numpy arrays, degenerate
axes are removed in this unlike numpy slicing, degenerate axes are removed.
That is, ``t1.Temp[0, 1]`` returns a scalar, while ``t1.Temp(i_lat=0, i_lon=1)``
returns a two dimensional variable.

Arithmetic operations and broadcasting rules
--------------------------------------------

Reference: :doc:`ufunc` and :doc:`var.arith`

Arithmetic and other mathematical operations are also supported by PyGeode. The
simplest are unary operations, which are performed elementwise. Most standard
mathematical functions (powers, exponentials, trigonometric functions, etc.)
are supported, and can be found in the main ``pygeode`` module:

.. ipython::

  @suppress
  In [6]: import pylab as pyl; pyl.ion()

  @suppress
  In [6]: import matplotlib as mpl; mpl.rc('figure', figsize=(5, 3))

  @savefig log_t1Temp.png width=4in
  In [8]: pyg.showvar(pyg.log(t1.Temp))     # Plot the natural logarithm of Temp

There are some convenience functions included, for instance, most trig functions
have a version which takes arguments in degrees rather than radians:

.. ipython::

  @savefig sind_t1lat.png width=4in
  In [10]: pyg.showvar(pyg.sind(t1.lat))     # Compute the sine of latitude

In most cases the underlying operation is performed by the numpy equivalent,
though there are a few additional operations as well. A full list can be found
in :doc:`ufunc`. The PyGeode wrappers are designed to properly handle PyGeode
variables, so one should get accustomed to including the ``pyg`` prefix. This
is also a good reason to import pygeode into its own namespace, rather than
into the top-level namespace itself.

Standard Python binary arithmetic operations (``+``, ``-``, ``*``, ``/``,
``**``, etc.) are supported and work as one would expect if all the
variables are defined on the same axes. Comparison operators (``>``, ``<``, etc.)
are also supported and produce a boolean variable on the same axes with the result of
the operation performed elementwise. This can be very useful for masking data, 
since when cast to scalar values, ``True`` is equal to 1 and ``False`` is equal to 0:

.. ipython::

  In [10]: import numpy as np

  @savefig t1mask.png width=4in
  In [11]: pyg.showvar(t1.Temp > 280., clevs=np.arange(-0.1, 1.11, 0.1))

If the variables do not share the same axes, PyGeode follows a set of rules for
automatically broadcasting them so that the operations behave as one might
typically desire - it's important to be aware of these rules as you can
sometimes end up with some unexpected results, so they are described here in
some detail.

.. _broadcasting:

Broadcasting
............

When performing a binary operation, PyGeode will broadcast each variable along
the dimensions of the other which it does not itself possess. The order of the
axes in the resulting variable is given by the first variable's axes, followed
by those of the second which are not included in the first.

A couple of examples will clarify this:

.. ipython::

  In [13]: print((t2.U + t2.Temp).axes)   # No broadcasting required

  In [11]: print((t2.lat + t2.lon).axes)  # Broadcast to (lat, lon)

  In [12]: print((t2.lon + t2.lat).axes)  # Broadcast to (lon, lat)

The one exception to this rule is that if either variable is defined on a subset
of the other's axes, the order of the latter is maintained:

.. ipython::

  In [12]: print((t2.lon + t2.Temp).axes)  # Broadcast to (time, pres, lat, lon)

You may be wondering how PyGeode decides whether two axes are the same for the
purposes of this broadcasting. If two axes have the same elements (to within a
tolerance - see :func:`numpy.allclose`), and are of the same type, they are
considered equal (see also :func:`Axis:__eq__`) and are matched. If PyGeode finds 
two axes of the same type but with different elements, it attempts to find a complete
mapping from one to the other. In most cases this means that the elements of one
axis must be a subset of the other, and the broadcasted variable acquires the
smaller of the two axes; e.g. in the following case, PyGeode uses the smaller
of the two longitude axes, since it is a subset of the longitude axis of
``t2.Temp``.

.. ipython::

  # Broadcasting restricts longitude axis to subset 
  In [12]: print((t2.Temp(lon=(0, 180)) - t2.Temp).lon)

However, if pygeode finds two axes that could be compatible, but whose elements can
not be simply mapped to one another, PyGeode will raise an exception:

.. ipython::

  # Subsetted longitude axes are not compatible:
  In [12]: try: print((t2.Temp(lon=(0, 180)) + t2.Temp(lon=(120, 240))).lon)
     ....:except ValueError as e: print(e)


Reductions (Averages, Standard deviations)
------------------------------------------

As we saw at the beginning of this section, you can compute averages over a
variable with :meth:`~Var.mean`. By default this computes an average over the
whole domain, but you can specify particular axes you want to average over. For
example,

.. ipython::

  In [4]: print(t2.Temp.mean('pres', pyg.Lon))
  
This computes an average over the both the pressure and longitude axes. You can
specify axes in three ways:

  * by name, e.g. ``t2.Temp.mean('lon')``
  * by class, e.g. ``t2.Temp.mean(pyg.Lon)``
  * or by (zero-based) index, e.g. ``t2.Temp.mean(3)``

These will all (in this case) return the same average. These three ways of
identifying axes are pretty general across PyGeode routines. 

Often it's useful to compute an average over a subset of the domain. You could
first select the subdomain, then compute the mean (``t2.Temp(lat=(70,
90)).mean('lat')``), but this is such a common operation that there is a short
cut in the form of another selection prefix, ``m_``:

.. ipython::

  In [5]: print(t2.Temp(m_lat=(70, 90)))

This selects all latitudes between 70 N and 90 N and performs an average.

You may notice this last operation returned a ``WeightedMeanVar``, rather than just a ``MeanVar``.
PyGeode, by default, will perform weighted averages over axes which have weights associated with
them. In this case, our latitude axis is weighted its cosine, to take in to account the smaller
surface area near the poles:

.. ipython::

  In [6]: print(t2.Temp.lat.weights)

You can turn this off, if desired, by specifying ``weights=False`` as a keyword argument:

.. ipython::

  In [6]: print(t2.Temp.mean('lat', weights=False))

Alternatively, you can specify your own weights to use, in the form of a PyGeode
variable with the same axes as those you would like to weight:

.. ipython::
  
  In [8]: print(t2.Temp.mean('lat', weights=pyg.sind(t2.Temp.lat)))

The weights do not need to be normalized; PyGeode will do that automatically. 

There are several other axes reductions that behave similarly, including
:func:`Var.stdev()`, :func:`Var.variance()`, :func:`Var.sum()`,
:func:`Var.min()`, :func:`Var.max()`; see :ref:`Axis Reductions <reduce-list>`
for the full list.  Some differences exist though:

  * :func:`Var.sum()` by default does *not* use the axes weights; you can use the
    default weights by specifying ``weights=True`` as a keyword argument. 

  * :func:`Var.max()` and  :func:`Var.min()` do not use weights; they return the maximum and
    minimum values (respectively) along the axes being reduced.

Finally, there are also equivalents for several of these methods which are ``NaN`` aware. 

Reshaping variables
-------------------
Finally, there are a whole set of basic manipulations you can perform on variables if you need to
rework their structure. Some of the most common are introduced here; for a complete list see
:ref:`Array manipulation routines <varops-list>`. Keep in mind that variables are thought of as immutable objects - that is, once
they're created, they don't change - as before, what the following operations actually do is return
a new variable with the desired changes that wraps the old one.

:func:`Var.transpose()` reorders the axes of a variable. Not all axes need to
be specified; those that are not will be appended in their present order.

.. ipython::

  In [8]: t2.Temp.axes

  In [9]: print(t2.Temp.transpose('lon', 'lat', 'pres', 'time').axes)

:func:`Var.replace_axes()` replaces any or all axes of a variable. The new
axes must have the same length as those they are replacing.

.. ipython::

  # The logPAxis method returns a log-pressure axis with a given scale height
  In [8]: print(t2.Temp.replace_axes(pres=t2.pres.logPAxis(H=7000)).axes)

:func:`Var.squeeze()` removes degenerate axes (those with one or fewer elements).
As mentioned above, the default selection behaviour is to always return a
variable with the same number of axes as you've started with, even if those
axes have only a single element. If you want to remove these degenerate axes,
you can use this command, which, when called with no arguments, will simply remove
all degenerate axes. Several other methods of calling are also available:

.. ipython::

  # Squeeze all degenerate axes
  In [8]: print(t2.Temp(time = 4, lon = 20).squeeze())

  # Squeeze only the time axis (if it is degenerate)
  In [8]: print(t2.Temp(time = 4, lon = 20).squeeze('time'))

  # Select a single value then squeeze the time axis
  In [8]: print(t2.Temp.squeeze(time = 4))

  # Select a single value and sqeeze the time axis using a selection prefix
  In [8]: print(t2.Temp(s_time = 4, lon = (20, 40)))

There are also commands to rename variables and their axes
(:func:`Var.rename()`, :func:`Var.rename_axes()`), for adding axes to a
variable (:func:`Var.extend()`), reordering axes elements
(:func:`Var.sorted()`) and dealing with NaNs (:func:`Var.fill()`,
:func:`Var.unfill()`).

