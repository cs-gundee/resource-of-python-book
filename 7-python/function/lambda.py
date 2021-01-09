# lambda аргументууд: илэрхийлэл



x = lambda a: a*a

for i in range(5, 7):
    print(x(i))
# Үр дүн:   25
#           36



# 2 аргументтай ламбда
y = lambda a, b: a + b

print(y(25, 30))        # 55
print(y(22.5, 100))     # 122.5



# lambda
def evenOrOdd(x):
    return lambda x: x> 0

value = evenOrOdd(-5)
print(value(-5))        # True

value = evenOrOdd(5)
print(value(5))         # False
