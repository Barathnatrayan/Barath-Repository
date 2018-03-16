def add(num1,num2):
    """Adddition funcction"""
    return num1+num2

def sub(num1,num2):
    """Substractoin funcction"""
    return num1-num2

def mul(num1,num2):
    """Multiplication funcction"""
    return num1*num2

def div(num1,num2):
    """Division funcction"""
    return num1/num2

"""Display all the options available for calculation"""
print("Calculator")
print("1. Addition")
print("2. Substraction")
print("3. MMultiplication")
print("4. Division")


"""Get the input choice from the Client"""
choice = input("Enter choice")

"""Get the number input from the client"""
num1 = int(input("Enter Number1"))
num2 = int(input("Enter Number2"))

"""Check the choice using the If statement and call the respecctive functions"""
if choice == '1':
    print("Addition of ",num1,"and",num2,"is ",add(num1,num2))
elif choice == '2':
    print("Subtraction of ", num1, "and", num2, "is ", sub(num1, num2))
elif choice == '3':
    print("Multiploication of ", num1, "and", num2, "is ", mul(num1, num2))
elif choice == '4':
    print("Division of ", num1, "and", num2, "is ", div(num1, num2))
else:
    print("invalid input")