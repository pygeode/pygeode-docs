**********************
Installing PyGeode
**********************

Anaconda
============================

Conda packages for PyGeode are maintained in the custom channel `<https://conda.anaconda.org/aph42>`_


Windows installer
============================

You'll need to install the following packages (make sure to download the 32-bit versions):

1) `Python 2.7 <http://python.org/download/>`_
2) `Numpy <http://sourceforge.net/projects/numpy/files/NumPy/>`_ (handles the number crunching)
3) `Matplotlib <http://sourceforge.net/projects/matplotlib/files/matplotlib/>`_ (handles the plotting)
4) `PyGeode <https://bitbucket.org/pygeode/pygeode/downloads>`_ *(that's us!)*

Optional Packages:

5) `ipython <http://ipython.scipy.org/moin/Download>`_ (a better interactive Python shell)
6) `PyReadline <http://ipython.scipy.org/moin/PyReadline/Intro>`_ (endows ipython with tab completion and history)
7) `basemap <http://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/>`_ (handles maps and projections for plotting)

Ubuntu (*via Launchpad PPA*)
=============================================

This is the recommended approach for Ubuntu systems, since it will automatically keep you updated with the latest stable version.

1) Add the PyGeode PPA to your list of repositories:

   ``sudo add-apt-repository ppa:pygeode/ppa``

2) Scan the repositories for new packages:

   ``sudo apt-get update``

3) Install the PyGeode package

   ``sudo apt-get install python-pygeode``


RPM-based Linux distributions (Fedora, CentOS, openSUSE, etc.)
===============================================================

Pre-built RPM packages are available via the `openSUSE Build Service <https://build.opensuse.org/package/show/home:neishm/python-pygeode>`_


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



