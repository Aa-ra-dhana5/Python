# Package

-- Packages are way of structuring Python's module namespace by using "dotted module names"
-- Apackage can have one or more modules which means a package is collection of modules and packages

-- package can contatin package

## Craeting Package
 --must contain __init__.py file for python2 but now its not required


## accessed using 
import package_name.subPackageName.ModuleNAme

exa: import Admin.Common.footer

to do 
from package_name import *
it will show error 

__all__ 
if a package's __init__.py code defines a list named __all__ , then it is taken to the list of module names that should be imported from *