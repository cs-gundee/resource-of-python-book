# арифметик операторууд
print(5+4)      # 9
print(5-4)      # 1
print(5*4)      # 20
print(5/4)      # 1.25
print(5%4)      # 1 үлдэгдэл
print(5**4)     # 625
print(5//4)     # 25


print(5==4)
print(5!=4)
print(5>4)
print(5<4)
print(5>=4)
print(5<=4)


print("\n===Logical===")
print(5 > 4 and 100 == 100) # True
print(4 > 5 and 5 < 9)  # False
print(4 > 5 or 5 < 9)  # True
print(5 < 4 or 9 > 100)   # False
print(not(5 < 10 and 5 < 100))  # False

# identify operators
print("\n===Identify===")
x = "утга1"
y = x
print(x is y)       # True
print(x is not y)   # False

y = "Шинэ утга"
print(x is y)       # False
print(x is not y)   # True


# membership operators
print("\n===Membership===")
txt = "Миний төрсөн нутаг Монголын сайхан орон"
print("нут" in txt)     # True
print("НУТАГ" in txt)   # False
print("my" not in txt)  # True