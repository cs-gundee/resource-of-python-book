# for давталт
for i in [0, 1, 2, 3, 4]:
    print(i)


# lists
operators = ["Мобиком", "Скайтел", "Юнител", "Жи Мобайл"]
for operator in operators:
    print(operator)
""" Үр дүн: Мобиком
            Скайтел
            Юнител
            Жи Мобайл """


operator = "Моби"
for s in operator:
    print(s)
"""Үр дүн:  М
            о
            б
            и """

# range()
for i in range(5):
    print(i)

for i in range(3, 8):
    print(i)

for i in range(3, 14, 3):
    print(i)
""" Үр дүн: 3
            6
            9
            12 """




# break
weekdays = ['Даваа', 'Мягмар', 'Лхагва', 'Пүрэв', 'Баасан']
for day in weekdays:
    print(day)
    if day == 'Лхагва':
        break
""" Үр дүн: Даваа
            Мягмар
            Лхагва """



# continue
print('\ncontinue')
weekdays = ['Даваа', 'Мягмар', 'Лхагва', 'Пүрэв', 'Баасан']
for day in weekdays:
    if day == 'Лхагва':
        continue
    print(day)
""" Үр дүн: Даваа
            Мягмар
            Пүрэв
            Баасан """


# tuple
mountains = ('Хэнтий', 'Хангай', 'Алтай')
for mount in mountains:
    print(mount)
""" Үр дүн: Хэнтий
            Хангай
            Алтай """


# else
weekdays = ['Даваа', 'Мягмар', 'Лхагва', 'Пүрэв', 'Баасан']
for day in weekdays:
    print(day)
else:
    print('Давталт дууслаа')

""" Үр дүн: Даваа
            Мягмар
            Лхагва
            Пүрэв
            Баасан
            Давталт дууслаа """


# nested loop
colors = ['улаан', 'шар']
items = ['хавтас', 'үзэг', 'харандаа']

for color in colors:
    for item in items:
        print(f'{color} {item}')

""" Үр дүн: улаан хавтас
            улаан үзэг
            улаан харандаа
            шар хавтас
            шар үзэг
            шар харандаа """


# else
items = ['хавтас', 'үзэг', 'харандаа']
for item in items:
    pass