# Sample 1: Swap two integers
# Take two variables var_int1 and var_int2 as integer input
# And print them with their values swapped


var_int1 = str(input("Enter value for var_int1: "))
var_int2 = str(input("Enter value for var_int2: "))

var_temp = var_int2
var_int2 = var_int1
var_int1 = var_temp

print(f"var_int1: {var_int1}, var_int2: {var_int2}")

# ----------------------------------------------------------------- #

# Sample 2 : Take width and length of a rectangle and find the area
# ----------------------------------------------------------------- #
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

print(f"Area of Rectange: {width*height}")

# Sample 3: BMI calculator
# Take height and weight as input and calculate the BMI
# BMI formula : weight (lb) * 703 / [height (in)]2
# ----------------------------------------------------------------- #

height = float(input("Enter your height in inches:"))
weight = float(input("Enter your weight in pounds:"))

BMI = (weight*703)/(height**2)

print(f"Your BMI is {(weight*703)/(height**2)}")

# ----------------------------------------------------------------- #

# Sample 4: input an integer between 0 and 1000 and adds all the digits in the integer. e.g. 261 => 2 + 6 + 1 = 9
# e.g. 261 => 2 + 6 + 1 = 9


# ----------------------------------------------------------------- #