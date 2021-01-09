# string буюу тэмдэгт мөр төрөл
хувьсагчийн_нэр = "утга"
# эсвэл
хувьсагчийн_нэр = 'утга'


my_str1 = "Миний нутаг"
my_str2 = 'Миний нутаг'


print(хувьсагчийн_нэр)
print(my_str2)
print(type(my_str1))
# <class 'str'>
print(type(my_str2))
#<class 'str'>


# олон мөр тэмдэгт
my_str = """Хэнтий, Хангай, Соёны өндөр сайхан нуруунууд
Хойд зүгийн чимэг болсон ой хөвч уулнууд
Мэнэн, Шарга, Номины өргөн их говиуд
Өмнө зүгийн манлай болсон элсэн манхан далайнууд"""

print(my_str)



# str бол массив
a = "Python"
print(a[3])     # h
print(a[5])     # n
#print(a[6])     # IndexError: string index out of range



# slicing
fullname = "Дашдоржийн Нацагдорж"
lastname = fullname[0:7]
print(lastname)        # Дашдорж



lastname = fullname[:7]
print(lastname)         # Дашдорж



value = fullname[5:]
print(value)            # ржийн Нацагдорж

print(fullname[:])      # Дашдоржийн Нацагдорж



# сөрөг индекс
firstname = fullname[-10:-1]
print(firstname)        # Нацагдорж



# тэмдэгт мөрийн урт
print(len(fullname))                # 20
print(len("Миний нутаг шүлэг"))     # 17



#string methods
line = "энэ бол МИНИЙ төрсөн нутаг"
print(line.capitalize())    
# Энэ бол миний төрсөн нутаг



line = """Энэ бол миний төрсөн нутаг
Энэ бол миний төрсөн нутаг"""
print(line.count("нутаг"))          # 2
print(line.count("нутаг", 0, 30))   # 1



line = """Энэ бол миний төрсөн нутаг
Энэ бол миний төрсөн нутаг"""
print(line.find("нутаг"))           # 21
print(line.find("нутаг", 30, 53))   # 48
print(line.find("нутаг", 0, 10))    # -1 Олдоогүй



line = """Энэ бол миний төрсөн нутаг
Энэ бол миний төрсөн нутаг"""
print(line.index("нутаг"))           # 21
print(line.index("нутаг", 30, 53))   # 48
# print(line.index("нутаг", 0, 10))    # ValueError: substring not found



line = "энэ бол МИНИЙ төрсөн нутаг"
print(line.lower())    
# энэ бол миний төрсөн нутаг
print(line.upper())
# ЭНЭ БОЛ МИНИЙ ТӨРСӨН НУТАГ



line = "энэ бол МИНИЙ төрсөн нутаг"
print(line.replace("МИНИЙ", "миний"))
# энэ бол миний төрсөн нутаг



line = "Энэ бол миний төрсөн нутаг"
print(line.split(" "))
# ['Энэ', 'бол', 'миний', 'төрсөн', 'нутаг']



line = "энэ бол МИНИЙ төрсөн нутаг"
line2 = line.replace("МИНИЙ", "миний")
print(line) # line хувьсагчийн утга өөрчлөгдөхгүй тул
print(line2) # энд line хувьсагчийн утга өөрчлөгдөж, хадгалагдсан
  


line = "Энэ бол миний төрсөн нутаг"
x = "бол" in line
print(x)        # True



line = "Энэ бол миний төрсөн нутаг"
x = "бол" not in line
print(x)        # False



line1 = "төрсөн нутаг"
print("Энэ бол миний " + line1)
# Энэ бол миний төрсөн нутаг

line2 = "Монголын сайхан орон"
print("Энэ бол миний " + line1 + " " + line2)
# Энэ бол миний төрсөн нутаг Монголын сайхан орон


poem = "Миний нутаг"
year = 1930
# print("Шүлгийн нэр: " + poem + "Зохиогдсон он: "+ year)
# TypeError: can only concatenate str (not "int") to str

print("Шүлгийн нэр: {} Зохиогдсон он: {}".format(poem, year))
# Шүлгийн нэр: Миний нутаг + Зохиогдсон он: 1930


# escape тэмдэгт
# txt = "Шүлгийн нэр: "Миний нутаг""      #SyntaxError: invalid syntax

txt = 'I\'m Mongolian.'
print(txt)          # I'm Mongolian.

txt = "Шүлгийн нэр: \"Миний нутаг\""  
print(txt)          # Шүлгийн нэр: "Миний нутаг"

txt = "Ташуу зураас \\"
print(txt)          # Ташуу зураас \

print("Шүлгийн нэр: {} \nЗохиогдсон он: {}".format(poem, year))
# Шүлгийн нэр: Миний нутаг
# Зохиогдсон он: 1930

