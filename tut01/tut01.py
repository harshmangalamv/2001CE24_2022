import os
os.system("cls")

def factorial(x): ## factorial function declared 
	if x == 0:  ## when input is 0
		return 1
	if x<0: 	## when input is negative
		return -1
	return x*factorial(x-1) ## recurse

    

x = int(input("Enter the number whose factorial is to be found:\n")) ## taking input

print("The factorial of", x, "is:", factorial(x), ".") ## here is the output