grocery_inventory = {
    "Milk":("Dairy", 3.50, 8),
    "Eggs":("Dairy", 5.50, 30),
    "Bread":("Bakery", 2.99, 15),
    "Apples":("Produce",1.50, 50)
}

eggs_price = grocery_inventory["Eggs"][1]
eggs_stock = grocery_inventory["Eggs"][2]
print("Eggs price:", grocery_inventory["Eggs"][1])
grocery_inventory["Eggs"] = ("Dairy", eggs_price - 1, eggs_stock)
if grocery_inventory["Eggs"][1] < 5:
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable")


grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

milk_stock = grocery_inventory["Milk"][2]

if milk_stock < 10:
   print("milk needs to be restocked. increasing stock by 20 units.")
   grocery_inventory["Milk"] = (
       grocery_inventory["Milk"][0],
       grocery_inventory["Milk"][1],
       milk_stock + 20
   )
else:
   print("milk has sufficient stock.")

print("Updated inventory:", grocery_inventory)

