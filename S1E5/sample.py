# Example1: Input an integer greater than 1 and display it's multiplication table

# input_number = int(input("Enter an integer greater than 1: "))

# for num in range(1,11):
# 	print(f"{input_number} X {num} = {input_number * num}")
##########################################

# Example2: input an integer greater than 1 and check if it is a Prime Number
# Prime Number: A positive integer greater than 1 which has no other factors except 1 and the number itself 
# is called a prime number. 
# 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. 
# But 6 is not prime (it is composite) since, 2 x 3 = 6

input_integer = int(input("Enter an integer greater than 1:  "))

for num in range(2,input_integer):
	if input_integer % num == 0:
		print(f"{input_integer} is not a prime number as it is divisible by {num}.")
		break
else:
	print(f"{input_integer} is a prime number.")

print("This is outside of the loop.")