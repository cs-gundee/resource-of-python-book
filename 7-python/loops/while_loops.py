i = 0
while i < 3:
    print(i)
    i += 1  # i = i + 1

""" Үр дүн: 0
            1
            2 """


# break
weekdays = ['Даваа', 'Мягмар', 'Лхагва', 'Пүрэв', 'Баасан']
i = 0
while i < len(weekdays):
    print(weekdays[i])
    i += 1
    if weekdays[i] == 'Мягмар':
        break
# Үр дүн: Даваа


# continue
print("\ncontinue")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
    

# else
weekdays = ['Даваа', 'Мягмар', 'Лхагва', 'Пүрэв', 'Баасан']
i = 0
while i < len(weekdays):
    print(weekdays[i])
    i += 1
else:
    print(f'Жагсаалтын урт: {len(weekdays)}')
""" Үр дүн: Даваа
            Мягмар
            Лхагва
            Пүрэв
            Баасан
            Жагсаалтын урт: 5 """