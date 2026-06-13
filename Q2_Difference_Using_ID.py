a = 10
b = 10

print(id(a))
print(id(b))
print(id(a) == id(b))

a = [10]
b = [10]

print(id(a))
print(id(b))
print(id(a) == id(b))

# Output:
# 140710091162824
# 140710091162824
# True
# 2909338559808
# 2909340890688
# False