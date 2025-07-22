print("Welcome to the Discount Calculator!")
amount =int(input("Enter the amount: "))
if amount < 0:
    print("Invalid amount. Please enter a positive number.")
elif amount >= 10000:
    discount = 0.3
elif amount >= 5000:
    discount = 0.2
elif amount >= 1000:
    discount = 0.1
else:
    discount = 0

final_amount = amount - (amount * discount)
print(f"Your original amount was: {amount}")
print(f"Your discount is: {discount * 100}%")
print(f"your discount amount is: {amount * discount}")
print(f"After the  discount your amount is: {final_amount}")

