produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

for section in range(len(groceries)):
    for item in groceries[section]:
        print(item)