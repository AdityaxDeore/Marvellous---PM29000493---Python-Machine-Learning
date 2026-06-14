x = input("Enter a number:")

print("Type before casting :" , type(x))

y = int(x)

print("Type after int() :" , type(y))

z = float(x)

print("Type after float() :" , type(z))

# Output (Input: 25):
# Enter a number:Type before casting : <class 'str'>
# Type after int() : <class 'int'>
# Type after float() : <class 'float'>