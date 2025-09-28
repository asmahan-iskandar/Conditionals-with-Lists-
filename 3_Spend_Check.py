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