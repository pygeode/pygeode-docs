File Input and Output
=====================

.. currentmodule:: pygeode

Serialized data stored in files on disk (or over the network) can be imported
into PyGeode with the routines :func:`open` (for single files), :func:`openall`
(for small numbers of files), and :func:`open_multi` (for large numbers of
files).  Variables and datasets can be saved to disk with :func:`save`. 

.. _formats:

Several formats are supported natively by pygeode, including NetCDF (versions 3
and 4), HDF (versions 4 and 5) and grib files, though support for NetCDF and
HDF is the most complete. By default the format is detected through the file extension;
however, many of the methods below accept an optional ``format`` argument which can be used to 
specify the format explicitly. 

========= ============  ================= =========
Format    Extension     String Identifier Notes
========= ============  ================= =========
NetCDF    .nc           netcdf
HDF5                    netcdf            Uses the same library as NetCDF
HDF4      .hdf          hdf4
GRIB      .grib         grib
========= ============  ================= =========

Code also exists to read the native binary format used by the Canadian Centre
for Climate Modeling and Analysis, but this is not distributed with PyGeode by
default.

.. autofunction:: open

.. autofunction:: openall

.. autofunction:: open_multi

.. autofunction:: save

.. currentmodule:: pygeode.formats

.. autofunction:: autodetectformat
