num1= float(input("ENTER Value 1: "))
operator= input("ENTER mathematical operator(+ ,-, /, *): ")
num2= float(input("ENTER Value 2: "))

if operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "+":
    result = num1 + num2
else:
    result = num1 - num2

print("The answer is: " + str(result))