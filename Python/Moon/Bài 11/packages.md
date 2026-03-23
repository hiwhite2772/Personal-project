my_package
|__ __init__.py
|__ module1.py
|__ module2.py
|__ subpackage1
|        |__ __init__.py
|        |__ module3.py
|__ subpackage2
         |__ __init__.py
         |__ module4.py



#import module1
from my_package import module1

#import module2
import mypackage.module2 as m2

#import module3
from my_package.subpackage1 import module3

#import một function trong module 4
from my_package.subpackage2.module4 import my_func