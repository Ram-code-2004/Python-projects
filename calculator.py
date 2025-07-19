a = input("Your Name ")
print ("Hii",a)
print("welcome to my calculator")
def calculator():
    print("Simple Calculator")
    print("Select operation:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
if choice in ['1', '2', '3', '4']:

        if choice == '1':
            print(num1 + num2)

        elif choice == '2':
            print(num1 - num2)

        elif choice == '3':
            print(num1 * num2)

        elif choice == '4':
                print(num1/num2 )
else :
 print("error")
