
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
