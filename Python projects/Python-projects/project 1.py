Menu = { 'Pizza': 120,
         'Pasta' : 80,
         'Coffee' : 50,
         'Tea' : 30,
         'Burger': 100,    
 }

print("welcome to my resturant")
print("Here is the menu\nPizza:RS 120\nPasta:RS 80\nCofee:RS 50\nTea:RS 30\nBurger:RS 100")
Total_order = 0

item_1 = input("Enter the item you want to order: ")  
if item_1 in Menu:
    Total_order += Menu[item_1]
    print(f"Your order for {item_1} has been added. Total so far: RS {Total_order}")
else:
    print("Item not found in the menu.")  

Another_order = input("Do you want to order another item? (yes/no): ").strip().lower()
if Another_order == 'yes':
    item_2 = input("Enter the next item you want to order: ")
    if item_2 in Menu:
        Total_order += Menu[item_2]
        print(f"Your order for {item_2} has been added. Total so far: RS {Total_order}")
    elif item_2 == 'no':
        print(f"Thank you for your order! Your total is RS {Total_order}.")
    else:
        print("Item not found in the menu.")
print(f"Thank you for your order! Your total amount to pay is RS {Total_order}.")