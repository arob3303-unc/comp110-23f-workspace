"""Dictionary Practice in Class!"""

# Create Dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# Add a new key and value
ice_cream["mint"] = 3

# Remove a key and value
ice_cream.pop("mint")

# Access a value
print(f"There are {ice_cream['chocolate']} orders of chocolate.")

# Modify a key value
ice_cream["vanilla"] += 2

# length of ice cream dict
print(len(ice_cream))

# Print
print(ice_cream)

# Conditional statement to check if key value is in dictionary
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint.")
else:
    print("no orders of mint!")

if "chocolate" in ice_cream:
    print(f"There are {ice_cream['chocolate']} orders of chocolate.")
else:
    print("no orders of chocolate!")

# For Loop Practice
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")
    