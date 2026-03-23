#import <ten_module>
import math
s = math.sqrt(25)
print(s)

#import <ten_module> as <ten_viet_tat>
import math as m
s = m.sqrt(25)
print(s)

#from <ten_module> import <ten_ham>, <ten_bien>
from math import sqrt
x = sqrt(25)
print(x)

#from <ten_module> import *
from math import *
x = sqrt(25)
print(x)

#from module_name import <ten_ham> as <ten_viet_tat>, <ten_bien>
from math import sqrt as s
x = s(25)
print(x)
