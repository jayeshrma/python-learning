class A:
    label="From A"

class B(A):
    label="From B"
    
class C(A):
    label="From C"
    
class D(C,B):
    pass 

temp=D()
print(D.label)
print(D.__mro__)