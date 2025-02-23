num1 = input("input x:")
num2 = input("input y:")
num1 = int(num1)
num2 = int(num2)
input_op = input("input operator:")
if input_op == "+":
    print(num1 + num2)
elif input_op == "-":
    print(num1 - num2) 
elif input_op == "*":
    print(num1 * num2)
elif input_op == "/":
    print(num1 / num2)
else:
    print("invalid operator")
"""The if-elif-else statement
 is used to compare the input operator
 with the operators +, -, *, and /."""