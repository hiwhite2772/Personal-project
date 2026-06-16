# Series & DataFrame - Pandas
import pandas as pd
# print(pd.__version__)

# 1. Series
a = [1, 2, 3]

myvar = pd.Series(a, index=["x","y","z"])

print(myvar)
print(myvar["y"])

calories = {
    'day1' : 420,
    'day2' : 380,
    'day3' : 390
}

myvar1 = pd.Series(calories)
myvar2 = pd.Series(calories, index = ["day1", "day3"])

print(myvar1)
print(myvar2)

# 2. DataFrame
data = {
    "Calories" : [420, 380, 390],
    "Duration" : [50, 40, 45]
}
myvar3 = pd.DataFrame(data)
myvar4 = pd.DataFrame(data, index=["day1","day2","day3"])

print(myvar3)
print(myvar3.loc[1])
print(myvar3.loc[[0,2]])
print(myvar4)
print(myvar4.loc["day3"])