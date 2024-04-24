Example package
===============

This is a package for providing critical constants for chemical compounds
There are two functions: 
One for providing critical constants with input as path to excel file within the package and the name of compound in form of string.
The other one for giving molar volume with input as path to excel file within the package and name of compound along with given operating conditions (P,T) in a form of list.
The user can find the path to excel file as follows,
1) This line will give the path to the package (critical):
    packdir = pkg_resources.get_distribution("critical").location
2) Once the path to directory is found, the path to find excel file within the package directory:
    add = '/critical/critical.xlsx'
3) Combine to two strings above and the path to the excel file is obtained:
    join = packdir + "" + add
    
