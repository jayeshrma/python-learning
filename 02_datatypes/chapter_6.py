chaiProp="Aromatic and Bold"
# Always remember that the last number is not inclusive
# Remember string[ start : end_before : step_size ]

print(chaiProp[0:8])
print(chaiProp[0:8:2])

# Pythonic way
print(f"First Word: {chaiProp[:8]}")
print(f"Last Word: {chaiProp[12:]}")
print(f"Reverse string: {chaiProp[::-1]}")

# Encoding and Decoding

label_text="Héy"
encoded_text=label_text.encode("utf-8")

print(label_text,encoded_text)

decoded_text=encoded_text.decode("utf-8")