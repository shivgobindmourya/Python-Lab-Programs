# Program: Multi-Store Inventory Management System

# Inventory records for different stores
store1 = { "Laptop": 10, "Mobile": 25, "Keyboard": 15, "Mouse": 30 }

store2 = { "Laptop": 5, "Mobile": 12, "Monitor": 8, "Mouse": 20 }

store3 = { "Laptop": 7, "Keyboard": 10, "Monitor": 12, "Headphones": 18 }


# Function 1: Display inventory of a store
def display_inventory(store, store_name):
    print(f"\n========== {store_name} INVENTORY ==========")

    if not store:
        print("Inventory is empty.")
        return

    for product, quantity in store.items():
        print(f"{product}: {quantity} units")


# Function 2: Safely check product availability
def check_product(store, product):
    if product in store:
        print(f"{product} is available: {store.get(product, 0)} units")
    else:
        print(f"{product} does not exist in this store.")


# Function 3: Add or update stock
def update_stock(store, product, quantity):
    if product in store:
        store.update({product: store.get(product, 0) + quantity})
        print(f"Stock updated! {product}: {store[product]} units")
    else:
        if quantity < 0:
            print("Cannot create a product with negative stock.")
            return

        store.update({product: quantity})
        print(f"New product added! {product}: {store[product]} units")


# Function 4: Merge inventories using dictionary comprehension
def merge_inventories(*stores):
    all_products = set()

    for store in stores:
        all_products.update(store.keys())

    merged_inventory = {
        product: sum(store.get(product, 0) for store in stores)
        for product in sorted(all_products)
    }

    return merged_inventory


# Function 5: Display low-stock products
def low_stock_products(store, threshold):
    low_stock = {
        product: quantity
        for product, quantity in store.items()
        if quantity < threshold
    }

    print(f"\n========== LOW STOCK (Below {threshold}) ==========")

    if low_stock:
        for product, quantity in low_stock.items():
            print(f"{product}: {quantity} units")
    else:
        print("No low-stock products found.")


# Function 6: Transfer stock between stores
def transfer_stock(source, destination, product, quantity):
    if quantity <= 0:
        print("Transfer quantity must be positive.")
        return

    if product not in source:
        print("Product does not exist in the source store.")
        return

    if source.get(product, 0) < quantity:
        print("Insufficient stock for transfer.")
        return

    source.update({product: source.get(product, 0) - quantity})
    destination.update({
        product: destination.get(product, 0) + quantity
    })

    print(f"Successfully transferred {quantity} units of {product}.")


# Main program
stores = { "Store 1": store1, "Store 2": store2, "Store 3": store3 }

while True:
    print("\n====== INVENTORY MANAGEMENT SYSTEM ======")
    print("1. Display Store Inventory")
    print("2. Check Product Availability")
    print("3. Add or Update Stock")
    print("4. Merge All Store Inventories")
    print("5. Display Low-Stock Products")
    print("6. Transfer Stock Between Stores")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        store_name = input("Enter store name (Store 1/Store 2/Store 3): ").strip()

        if store_name in stores:
            display_inventory(stores[store_name], store_name)
        else:
            print("Invalid store name.")

    elif choice == "2":
        store_name = input("Enter store name: ").strip()

        if store_name in stores:
            product = input("Enter product name: ").strip()
            check_product(stores[store_name], product)
        else:
            print("Invalid store name.")

    elif choice == "3":
        store_name = input("Enter store name: ").strip()

        if store_name not in stores:
            print("Invalid store name.")
            continue

        product = input("Enter product name: ").strip()

        try:
            quantity = int(input("Enter quantity to add: "))

            if not product:
                print("Product name cannot be empty.")
            elif quantity < 0:
                print("Quantity cannot be negative.")
            else:
                update_stock(stores[store_name], product, quantity)

        except ValueError:
            print("Please enter a valid integer quantity.")

    elif choice == "4":
        merged = merge_inventories(*stores.values())

        print("\n========== COMBINED INVENTORY ==========")

        for product, quantity in merged.items():
            print(f"{product}: {quantity} units")

    elif choice == "5":
        store_name = input("Enter store name: ").strip()

        if store_name not in stores:
            print("Invalid store name.")
            continue

        try:
            threshold = int(input("Enter low-stock threshold: "))

            if threshold < 0:
                print("Threshold cannot be negative.")
            else:
                low_stock_products(stores[store_name], threshold)

        except ValueError:
            print("Please enter a valid integer.")

    elif choice == "6":
        source_name = input("Enter source store name: ").strip()
        destination_name = input("Enter destination store name: ").strip()

        if source_name not in stores or destination_name not in stores:
            print("Invalid store name.")
        elif source_name == destination_name:
            print("Source and destination must be different.")
        else:
            product = input("Enter product name: ").strip()

            try:
                quantity = int(input("Enter quantity to transfer: "))

                transfer_stock(
                    stores[source_name],
                    stores[destination_name],
                    product,
                    quantity
                )

            except ValueError:
                print("Please enter a valid integer quantity.")

    elif choice == "7":
        print("Exiting Inventory Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please select from 1 to 7.")