**********************
Installing PyGeode
**********************

Anaconda
============================

Conda packages for PyGeode are maintained in the custom channel `<https://conda.anaconda.org/aph42>`_


Pip
==========

To install the latest version via pip:

    ``pip install pygeode``


From the source code
=====================================================

This approach should only be used if you are unable to install from a binary package.  You may have to do some fiddling to get it to compile on your system.

1) Download the latest stable release `here <https://github.com/pygeode/pygeode/releases>`_.

2) Unpack the tarball:

   ``tar -xzvf pygeode-<version>.tar.gz``

   ``cd pygeode-<version>``

3) Ensure you have the prerequisite packages listed in the ``INSTALL`` file.

4) Compile the source, and install:

   ``python setup.py build``

   ``sudo python setup.py install``



