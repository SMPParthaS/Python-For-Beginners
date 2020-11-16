# Sample 1: Input a number from the user and print whether it is positive or negative
# var_num = int(input("Enter your number:"))

# if var_num > 0:
# 	print(f"{var_num} is positive.")
# elif var_num == 0:
# 	print(f"{var_num} is 0.")
# else:
# 	print(f"{var_num} is Negative.")

# Sample 2: Input angles of a triangle and print if it's a valid triangle
# angle1 = float(input("Enter 1st angle: "))
# angle2 = float(input("Enter 2nd angle: "))
# angle3 = float(input("Enter 3rd angle: "))

# if (angle1 > 0 and angle2 > 0 and angle3 > 0 and angle1 + angle2 + angle3 == 180):
# 	print("This is a valid Triangle.")
# else:
# 	print("This is a not valid Triangle.")

# Sample 3: Input height and weight and classify BMI: 
# Good(less than equals 25), Overweight(between 25 and 30), and Obese(greater than equals 30).
height = float(input("Enter your height in inches:"))
weight = float(input("Enter your weight in pounds:"))

BMI = (weight*703)/(height**2)
print(f"BMI is {BMI}")

if height > 0 and weight > 0:
	if BMI <= 25:
		print("BMI is Good.")
	elif BMI > 25 and BMI < 30:
		print("BMI is Overweight.")
	else:
		print("BMI is Obese.")
else:
	print("Enter positive values for height and weight.")

# Sample 4: Input Basic Salary of an employee and calculate gross salary as per the below calculation.
'''
Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary > 30000 : HRA = 30%, DA = 95%

Gross Salary = Basic Salary + HRA + DA
'''

basic_salary = int(input("Enter your Basic Salary"))

hra = 0
da = 0
gross_salary = 0

if basic_salary > 0:
    if basic_salary <= 10000:
        hra = .2
        da = .8
    elif basic_salary > 10000 and basic_salary <= 20000: 
        hra = .25
        da = .9
    else:
        hra = .3
        da = .95

    gross_salary = basic_salary + basic_salary * hra + basic_salary * da


# Practice 1: Input three numbers from the user and print the greatest number
# Practice 2: Input a year and print if the year is a leap year or not a leap year