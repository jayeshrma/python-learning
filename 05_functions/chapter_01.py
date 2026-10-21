# Scope and Name Resolution
def serveIcecream():
    flavour="Chocolate"
    print(f"Inside: {flavour}")

flavour="Lemon"
serveIcecream()
print(f"Outside: {flavour}")