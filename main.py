# menu of restaurant
# menu={
#     'Pizza':750,
#     'Pasta':400,
#     'Zinger':450,
#     'Coffee':200,
#     'Brost':500,

# }
# # Greet
# print("Welcome to Abc Fast Food")
# print("Pizza:750\nPasta:400\nZinger:450\nCoffee:200\nBrost:500")

# order_total=0

# item_1 = input("Enter the name of item you want to order =")
# if item_1 in menu:
#     order_total += menu[item_1]
#     print(f"Your item {item_1} has been added to your Order")
# else:
#     print(f"Ordered item {item_1} is not available yet!")

#     another_order = input("Do you want to add another item?(Yes/No): " )

#     if another_order == "Yes":
#         item_2 = input("Enter the name of second item")
#         if item_2 in menu:
#             order_total +=menu[item_2]
#             print(f"Item {item_2} has been added to your order")
#         else:
#             print(f"Ordered item {item_2} is not available!")
#             print(f"The total amount of item to pay is{order_total}")



menu = {
    'Pizza': 750,
    'Pasta': 400,
    'Zinger': 450,
    'Coffee': 200,
    'Brost': 500,
}

# Greet
print("Welcome to ABC Fast Food")
print("Pizza:750\nPasta:400\nZinger:450\nCoffee:200\nBrost:500")

order_total = 0

# First item
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available!")

# Ask for a second item
another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")

# Display the total amount to pay
print(f"The total amount to pay is {order_total}")




