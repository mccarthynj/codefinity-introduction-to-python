# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started.")

for item in range(len(inventory)):
    a = list(inventory.keys())
    
    print(f"Processing {a[item]}")
    current_stock = inventory.get(a[item])[0]
    min_req_stock = inventory.get(a[item])[1]
    restock_qty = inventory.get(a[item])[2]
    sale_status = inventory.get(a[item])[3]
    while current_stock < min_req_stock:
        current_stock += restock_qty
        if current_stock > discount_threshold:
            sale_status = True
    inventory.update({a[item]: (current_stock, min_req_stock, restock_qty, sale_status)})

print("Processing completed.")