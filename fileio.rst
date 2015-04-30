File Input and Output
=====================

.. currentmodule:: pygeode

Serialized data stored in files on disk (or over the network) can be imported
into PyGeode with the routines :func:`open` (for single files), :func:`openall`
(for small numbers of files), and :func:`open_multi` (for large numbers of
files).  Variables and datasets can be saved to disk with :func:`save`. Several
formats are supported natively by pygeode, including NetCDF (versions 3 and 4),
HDF (versions 4 and 5) and grib files, though support for NetCDF and HDF is the
most complete.

.. autofunction:: open

.. autofunction:: openall

.. autofunction:: open_multi

.. autofunction:: save

.. currentmodule:: pygeode.format

.. autofunction:: autodetectformat
