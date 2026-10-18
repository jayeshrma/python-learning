masala_spices=("clove", "lemon", "ginger") # packing
(spice1, spice2, spice3)=masala_spices

print(masala_spices)

a_ratio, b_ratio=2,1
a_ratio, b_ratio=b_ratio, a_ratio
print(a_ratio, b_ratio)

# A mixed data type tuple
user_profile = ("Alice", 28, True)

# CRITICAL: A single-item tuple REQUIRES a trailing comma
single_item = ("apple",) 
not_a_tuple = ("apple")  # This is just a string!

# Creating without parentheses (Tuple Packing)
person = "John", 30, "Engineer"

# membership -> Case sensitive
print("ginger" in masala_spices)
print("milk" in masala_spices)
