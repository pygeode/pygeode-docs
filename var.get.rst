Retrieving values from a variable
=================================

.. currentmodule:: pygeode

The framework of PyGeode is designed to work with data that is too large to fit
in memory.  That is to say, you don't normally *have* the numerical values at
hand.  Instead, you work with a symbolic reference to the data, and build a
sequence of operations that will be performed *only when data is needed*.
Usually, this is when:

  * You are saving the variable to a file
  * You are generating a plot
  * You are calling an iterative routine such as :func:`EOF`, or some other
    complicated operation for which there is no efficient symbolic wrapper.

In the above routines, the logistics of retrieving the data is handled
internally, so you only see the end result.  There may be times, however, when
you *want* to work with raw values.  Perhaps you are using PyGeode in
conjunction with some other packages which operate on numpy arrays.  Or,
perhaps you just feel more comfortable working with an array instead of some
abstract data object.  We won't judge you.  Just call :func:`Var.get` and you
can do whatever you want with the data.

.. automethod:: Var.get

.. automethod:: Var.__getitem__

**See Also:**
  :doc:`var`
