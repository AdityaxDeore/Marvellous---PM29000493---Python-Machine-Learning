a = 10
b = 10
c = 20

print(id(a))
print(id(b))
print(id(c))
print(id(a) == id(b))
print(id(a) == id(c))

# Output:
# 140710091162824
# 140710091162824
# 140710091163144
# True
# False