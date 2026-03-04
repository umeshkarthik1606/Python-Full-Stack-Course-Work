data = {
    1: {'Product': 'Rice', 'Price': 70},
    2: {'Product': 'Wheat flour', 'Price': 120},
    4: {'Product': 'Sugar', 'Price': 80},
    5: {'Product': 'Cooking Oil', 'Price': 90},
    6: {'Product': 'Soaps', 'Price': 85},
    7: {'Product': 'Milk', 'Price': 60},
    8: {'Product': 'Egg (12 Pieces)', 'Price': 120},
    9: {'Product': 'Bread', 'Price': 40},
    10: {'Product': 'Salt', 'Price': 30},
}
print('S.No'.ljust(7), 'Product Name'.ljust(20), 'Price'.ljust(10))
for i in data:
    print(str(i).ljust(7), data[i]['Product'].ljust(20), str(data[i]['Price']).ljust(10))

print("\nAvailable product numbers:", list(data.keys()))
indexes = list(map(int, input('Enter the S.No of the products you want to buy: ').split()))

print("\n" + "Bill".center(30, '-'))
total_bill = 0
for i in set(indexes):
    if i not in data:
        print(f"Invalid product number skipped: {i}")
        continue

    qty = indexes.count(i)
    price = data[i]['Price']
    amount = price * qty

    print(f"{data[i]['Product']} {price} * {qty} = {amount}")
    total_bill += amount

print('-' * 30)
print(f"Total Bill: {total_bill}")
