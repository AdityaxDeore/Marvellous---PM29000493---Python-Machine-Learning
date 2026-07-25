a = 10
b = 10
c = 20

print("id of a is :" , id(a))
print("id of b is :" , id(b))
print("id of c is :" , id(c))
print("Same id for a and b :" , id(a) == id(b))
print("Same id for a and c :" , id(a) == id(c))

# Output:
# id of a is : 140711215891656
# id of b is : 140711215891656
# id of c is : 140711215891976
# Same id for a and b : True
# Same id for a and c : False