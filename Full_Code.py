#Part 1

# university student informaiton, student ID, name, age, grade
# if student ID is correct, grade above 85, student is eligible for a Grocery card of $50

# 1- student veriffication 
ID = "LU102025"
university_student_ID = input("Enter your university student ID: ")

# 2- boolean condition to check if the student ID is correct
if university_student_ID == ID:
    print("Access Granted")
elif university_student_ID != ID:
    print("Access Denied")
    exit()

Name = input("Enter your name: ")
Age = input("Enter your age: ")
grade = int(input("Enter your grade: "))

# 3- check if the student is eligible for a Grocery card
Grocery_card = 50
Grocery_card_Code= "LU50102025"

if grade >= 85:
    print("Student is eligible for a Grocery card")
    print("Hello " + Name + ", you are " + str(Age) + " of age and a university student in LU according to your ID " + str(university_student_ID)) 
    print("Your GPA is " + str(grade) + " Which makes me eligible for a Grocery card for the month of September")
    print("Please use the code " + Grocery_card_Code + " to redeem your Grocery card of $" + str(Grocery_card) + " at the LU stores")

else :
    print("Student is not eligible for a Grocery card")
    exit()

#Part 2


# the following is the shopping list the student needs to buy at one of the LU stores using the Grocery card

# 1 - shopping list items
shopping_list = [  
    "Pita Bread",
    "Onions",
    "Garlic",
    "Minced Meat",
    "Chicken Breast",
    "Mozzarella Cheese",
    "Tomatoes",
    "Pasta Sauce",
    "Strawberries" ,
    "Spinach",
    "Olive oil",
    ]

prices = [1, 0.5, 0.45, 4.5, 3, 2.75, 1, 1, 2, 1.5, 6]

# Displaying the shopping list

print("Shopping List:")

for i in range(len(shopping_list)):
    print("- " + shopping_list[i] + " : $" + str(prices[i]))

print(len(shopping_list), "items in total")

#selecting items form the list 

cart = []

for i in range(len(shopping_list)):
    item = shopping_list[i]

    Available = input("Is " + item + " available? (yes/no): ")
    if Available == "yes":
        cart.append(item)
        print("done " + item, "added to cart")

    elif Available == "no":
        print(item, "Sorry, not available in store")

# after finishing the shopping lsit cofnrimaiton - chekcign whats was added in the cart 

print("The following itemsare added to your cart:")
for item in cart:
    print("- " + item)

print("The following items are not added to cart:")
for i in shopping_list:
    if i not in cart:
        print("- " + i)

# adding and replacing the unavailble items in the shopping list 

for i in shopping_list:
    if i not in cart:
        index = shopping_list.index(i)
        shopping_list.pop(index)
        prices.pop(index)  

        new_item = input("Enter new item name: ")
        new_price = float(input("Enter new item price: "))
        shopping_list.append(new_item)
        prices.append(new_price)
        
final_shopping_list = cart + [new_item]
print("Your updated shopping list is:")
for i in range(len(shopping_list)):
    print("- " + shopping_list[i] + " : $" + str(prices[i]))


#Part 3

# the following is the Updated shopping list the student needs to buy 


Updated_shopping_list = {
    "Pita Bread": 1.5,
    "Onions": 1,
    "Garlic": 1,
    "Minced Meat": 4.5,
    "Chicken Breast": 3,
    "Mozzarella Cheese": 2.75,
    "Tomatoes": 1,
    "Pasta Sauce": 1,
    "Strawberries": 2,
    "Spinach": 1.5,
    "Milk": 4,
}

# ask user about each item
cart = {}

for item, price in Updated_shopping_list.items():
    qty = int(input("How many " + item + " do you want? (1 is the minimum): "))
    if qty > 1:
        cart[item] = qty

# calculate cost
total = 0
total_discount = 0
print("Your cart:")

for item, qty in cart.items():
    price = Updated_shopping_list[item]
    
    discount = 0
    discount_qty = 0
    if qty > 5:
        discount = 1
        discount_qty = qty - 5  
        total_discount += discount * discount_qty
        price -= discount  
    
    if discount_qty > 0:
        cost = (5 * Updated_shopping_list[item]) + (discount_qty * price)
        print("- " + item + " x " + str(qty) + " = $" + str(cost) + " (discount applied: $" + str(discount * discount_qty) + ")")
    else:
        cost = price * qty
        print("- " + item + " x " + str(qty) + " = $" + str(cost))
    
    total += cost

print("Total cost of the shopping list = $" + str(total))
print("Total discount applied = $" + str(total_discount))

# shopping card balance

card_balance = 50
cash_paid = 0  

if total > card_balance:
    extra = total - card_balance
    print("Your shopping card balance is only $" + str(card_balance))
    choice = input("Do you want to pay the extra $" + str(extra) + " in cash? (yes/no): ")
    if choice == "yes":
        cash_paid = extra
        print("Proceeding with payment...")
    else:
        print("Returning to main list. Please pick fewer items next time.")
else:
    print("Your card covers the total. Purchase successful!")

# print total

if total > 45:
    print("You spent a lot!")
elif 20 <= total <= 40:
    print("You spent an average amount.")
else:
    print("You spent a little!")

# New print to confirm total paid

if total > card_balance and cash_paid > 0:
    print("Total paid = $" + str(total) + " ($" + str(card_balance) + " with card and $" + str(cash_paid) + " in cash)")
else:
    print("Total paid = $" + str(total) + " (all with card)")
