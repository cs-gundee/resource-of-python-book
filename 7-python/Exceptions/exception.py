import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Оролтын төрөл тохирохгүй байна.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Тоог тэгд хуваах боломжгүй.")
    sys.exit(1)

print(f"{x}/{y} = {int(result)}")