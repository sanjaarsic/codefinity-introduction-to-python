shelf = ("apples", "oranges","bananas", "apples", "grapes", "apples", "bananas")

# Count apples
apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")

# Find first banana index
banana_index = shelf.index("bananas")
print(f"First Banana Index: {banana_index}")

# Check apple stock
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

# Count grapes and check stock
grape_count = shelf.count("grapes")
if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

# Check for oranges
if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print(f"Oranges are at index: {orange_index}")
else:
    print("Oranges are out of stock.")