#Part B Type convert the detactive Number
def safe_int(text):
    try:
        return int(float(text))
    except ValueError:
        return None
for sample in["42","-8","3.9","abc",""]:
    print(repr(sample),"->", safe_int(sample))
#Part C Ask the user for two numbers with input(), convert them with safe_int() and print their sum, or a friendly message if one of them is not a number.
print("===========================================")

number1=input("Enter the first Number:")
number2=input("Enter the Seconde Number:")

num1 = safe_int(number1)
num2 = safe_int(number2)

if num1 is not None and num2 is not None:
    Totalnumber = num1 + num2
    print(f"This is the result of summation:{Totalnumber}")
else :
    print("Err : One of Both your number have the problem.")