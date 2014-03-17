==================
Creating a custom variable
==================

Suppose one wants to perform an operation on data represented by some pygeode
variable that cannot be done by existing pygeode variables. One can always
load in the data directly, access the underlying numpy array, and perform the
operation directly; often this is the fastest and most straightforward approach.

Alternatively one can defined a new pygeode variable type in order to perform
the operation within the pygeode context. This can involve more work, certainly
if you are not familiar with the inner workings of PyGeode. This has several
advantages; metadata consistency, tools for manipulating and interpreting the
grids defined by an arbitrary pygeode variable, and often robustness. Once you
get the hang of it, pygeode implementations can often be nearly as simple as a
direct implemention, and are far more versatile (the former is _not_ always
true :)). 

variable construction, subclassing an appropriate var object
views and selecting axes
accessing data
reducing memory footprints, rule of thumb

