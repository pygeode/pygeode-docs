**********************
Installing PyGeode
**********************

Option 1 - Windows installer
============================

*Sorry, not available at this time*


Option 2 - From Launchpad PPA (*Ubuntu*)
=============================================

This is the recommended approach for Ubuntu systems, since it will automatically keep you updated with the latest stable version.

1) Add the PyGeode PPA to your list of repositories:

   ``sudo add-apt-repository ppa:pygeode/ppa``

2) Scan the repositories for new packages:

   ``sudo apt-get update``

3) Install the PyGeode package

   ``sudo apt-get install python-pygeode``


Option 3 - From binary package (*Debian-based systems*)
=======================================================

1) Download the latest Debian package (.deb) for your architecture `here <http://code.google.com/p/pygeode/downloads/list?q=.deb>`_

2) Open and install it from your favourite package manager.



Option 4 - From the source code (*Linux*)
=====================================================

This approach should only be used if you are unable to install from a binary package.  You may have to do some fiddling to get it to compile on your system.

1) Download the latest stable release `here <http://code.google.com/p/pygeode/downloads/list?q=.tar.gz>`_.

2) Unpack the tarball:

   ``tar -xzvf python-pygeode-<version>.tar.gz``

   ``cd python-pygeode-<version>``

3) Ensure you have the prerequisite packages listed in the ``INSTALL`` file.

4) Compile the source, and install:

   ``make``

   ``sudo make install``



