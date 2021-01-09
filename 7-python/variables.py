myvar = 2020 # хувьсагчийн утга бүхэл тоо
print(myvar)

myvar = "Hello" # одоо хувьсагчийн утга тэмдэгт төрөлтэй боллоо
print(myvar)


# Нэг мөрөнд олон хувьсагчийг тодорхойлж, утга олгох
x, y, z = "Тэнгэр", "Газар", "Ус"
print(x)
print(y)
print(z)


# Олон хувьсагчид ижил утга олгох
x = y = z = "Уул"
print(x)
print(y)
print(z)

"""
# глобал хувьсагч
x = "глобал"

def my_function():
    print(x)

my_function()

"""

"""
# глобал хувьсагч ба локал хувьсагч
x = "глобал хувьсагч"

def my_function():
    x = "локал хувьсагч"
    print(x)

my_function()
print(x)


# global түлхүүр үг ашиглах
def my_function():
    global x
    x = "глобал хувьсагч боллоо"

my_function()
print(x)

"""
# глобал хувьсагчийн утгыг солих
x = "глобал хувьсагч"

def my_function():
    global x
    x = "утга"

my_function()
print(x)