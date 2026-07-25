a = 10
b = 10

print("id of a is :" , id(a))
print("id of b is :" , id(b))
print("Same id for int :" , id(a) == id(b))

a = [10]
b = [10]

print("id of a is :" , id(a))
print("id of b is :" , id(b))
print("Same id for list :" , id(a) == id(b))

# Output:
# id of a is : 140711215891656
# id of b is : 140711215891656
# Same id for int : True
# id of a is : 1425631438144
# id of b is : 1425634294400
# Same id for list : False