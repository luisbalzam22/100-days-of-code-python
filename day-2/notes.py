type() # same as typeof

# to cast to a specific data type
str()
int()
float()
bool()

# in python, regular divisions ALWAYS return a float
4 / 2 # 2.0

# but "floor" divisions return a trunc value
4 // 2 # 2

# round() vs .format
round(153.6, 2) # 153.6 (FLOAT)
"{:.2f}".format(153.6) # "153.6" (STRING)
