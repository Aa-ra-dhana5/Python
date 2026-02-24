# Module
--A module is file containing python defination and statemetns
-- A module is a file containing group of variables, methods, function and classes
--They are executed only the first time the module naem is encountered in inport statement


Type of modules
1. User-defined modules
2. Built in modules
      -- array, math ,sys


--- easy to debug and seprate logics and reusability

How to use module
Syntex
 -- import module_name
 -- import module_name as alias_name
 -- from module_name import fun1, fun2 ... or var or class or dict or tuple
 -- from module_name import fun_name alias_F_name
 -- from module_name import *  --- import all values


**module can import other modules.

Namespace Pollution: 

1. With import cla    -- Is good practice
→ Everything stays inside cla namespace.

2. With from cla import *
→ Everything is dumped into your current file.

Both load the module once into memory

