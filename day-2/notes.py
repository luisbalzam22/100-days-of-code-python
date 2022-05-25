# alternative way of typing long NUMERIC values
999_999_999_999 # 999999999999
999_999_999.999 # 999999999.999

# to cast to a specific data type
str()
int()
float()
bool()

type() # same as typeof in JS

# dynamic casting in python
#-------example_start-------
non_floating = 45
floating_point = 4.5
type(non_floating)(floating_point) # 4
#--------example_end--------


# in python, regular divisions ALWAYS return a float
4 / 2 # 2.0

# but "floor" divisions return a trunc value
4 // 2 # 2

# round() vs .format()
round(153.6, 2) # 153.6 (FLOAT)
"{:.2f}".format(153.6) # "153.6" (STRING)

