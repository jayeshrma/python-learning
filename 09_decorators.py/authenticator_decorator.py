from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(role):
        if role!="admin":
            print("Access Denied")
            return None
        else:
            return func(role)
    return wrapper

@require_admin
def accessInventory(role):
    print("Access given!")
    
accessInventory("admin")