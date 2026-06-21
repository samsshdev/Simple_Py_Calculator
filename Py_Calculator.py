print("You're most welcome to Py-Calc!")
print("Please Choose any one operation by entering corresponding number from the list below: ")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder\n6. Exponentiation\n")
op = int(input("Enter corresponding number: "))

if(op <= 6 and op >= 1):
	if(op == 1):
		print("\n--- Addition ---\n")
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print("\n")
		print(f"{num1} + {num2} = {num1+num2}")
	elif(op == 2):
		print("\n--- Subtraction ---\n")
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print("\n")
		print(f"{num1} - {num2} = {num1-num2}")
	elif(op == 3):
		print("\n--- Multiplication ---\n")
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print("\n")
		print(f"{num1} * {num2} = {num1*num2}")
	elif(op == 4):
		print("\n--- Division ---\n")
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print("\n")
		if(num2 == 0):
			print("Division by zero can not be performed as it is undefined.")
		else:
			print(f"{num1} / {num2} = {num1/num2}")
	elif(op == 5):
		print("\n--- Remainder ---\n")
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print("\n")
		if(num2 == 0):
			print("Division by zero can not be performed as it is undefined.")
		else:
			print(f"{num1} % {num2} = {num1%num2}")
	elif(op == 6):
		print("\n--- Exponentiation ---\n")
		num1 = int(input("Enter the number: "))
		num2 = int(input("Enter the power: "))
		print("\n")
		print(f"{num1} ** {num2} = {num1**num2}")
else:
	print("Invalid Input!")
