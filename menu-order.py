menu = {
    'Pizza': 8.99,
    'Burger': 5.99,
    'Salad': 4.99,
    'Soda': 1.99,
    'Fries': 2.49,
    'Ice Cream': 3.49,
    'Coffee': 2.99,
    'Tea': 1.49,
    'Sandwich': 6.49,
}

print("Welcome to the Restaurant Menu!")
print("Pizza: $8.99, Burger: $5.99, Salad: $4.99, Soda: $1.99, Fries: $2.49, Ice Cream: $3.49, Coffee: $2.99, Tea: $1.49, Sandwich: $6.49")

order_total = 0
while True:
    item = input("Please enter the item you want to order (or type 'done' to finish): ").strip()
    if item.lower() == 'done':
        break
    elif item in menu:
        order_total += menu[item]
        print(f"Added {item} to your order. Current total: ${order_total:.2f}")
    else:
        print(f"Sorry, we don't have {item} on the menu.")