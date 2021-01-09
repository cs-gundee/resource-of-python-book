print(100 > 88)     # True
print(100 < 88)     # False


print(bool("Hello"))    # True
x = 55
print(bool(x))          # True


print(bool(False))      # False
print(bool(None))       # False
print(bool(0))          # False
print(bool(""))         # False
print(bool(()))         # False
print(bool([]))         # False
print(bool({}))         # False

# функцийн буцаах утга 0 байх
def function():
    return 0

my_object = function()
print(bool(my_object))  # False


x = 500
print(isinstance(x, int))       # True
print(isinstance(x, float))     # False