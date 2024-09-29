number_of_items = int(input("Enter Number of Items: "))
total_price = 0

while number_of_items <= 0:
    print("Invalid Number of Items!")
    number_of_items = int(input("Enter Number of Items: "))
for i in range(number_of_items):
    price_of_item = float(input("Enter Item Price: "))
    total_price = total_price + price_of_item
if total_price > 100:
    total_price = total_price * 0.9
print("Total price for" + str(number_of_items) + "is $" + str(total_price))
