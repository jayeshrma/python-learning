# Global

dessertType="Cheesecake"

def cafe():
    
    def kitchen():
        global dessertType
        dessertType="Waffle"
    kitchen()
    
cafe()
print(f"After update: {dessertType}")