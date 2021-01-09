# list

жагсаалт = ['элемент1', 'элемент2', 'элемент3']
print(жагсаалт)
# ['элемент1', 'элемент2', 'элемент3']

newlist = list(('элемент1', 'элемент2'))
print(newlist)      # ['элемент1', 'элемент2']

weekdays = ['Даваа', 'Мягмар', 'Лхагва', 'Пүрэв', 'Баасан']
print(weekdays[0])      # Даваа
print(weekdays[4])      # Баасан

print(weekdays[-1])     # Баасан
print(weekdays[-3])     # Лхагва

# индексийн муж
newlist = weekdays[1:3]
print(newlist)      # ['Мягмар', 'Лхагва']

anotherlist = weekdays[-3:-1]
print(anotherlist)  # ['Лхагва', 'Пүрэв']

# элементийг өөрчлөх
#weekdays[0] = 'Monday'
#weekdays[3] = 'Thursday'
print(weekdays)     # ['Monday', 'Мягмар', 'Лхагва', 'Thursday', 'Баасан']    

# жагсаалтын урт
print(len(weekdays))    # 5
print(len(newlist))     # 2

# append()
weekdays.append("Бямба")
print(weekdays)
# ['Даваа', 'Мягмар', 'Лхагва', 'Пүрэв', 'Баасан', 'Бямба']

# insert()
weekdays.insert(1, 'Monday')
print(weekdays)
# ['Даваа', 'Monday', 'Мягмар', 'Лхагва', 'Пүрэв', 'Баасан', 'Бямба']

# remove()
weekdays.remove('Monday')
print(weekdays)
# ['Даваа', 'Мягмар', 'Лхагва', 'Пүрэв', 'Баасан', 'Бямба']

# pop()
weekdays.pop(-1)
print(weekdays)
# ['Даваа', 'Мягмар', 'Лхагва', 'Пүрэв', 'Баасан']

item = weekdays.pop()
print(weekdays)     # # ['Даваа', 'Мягмар', 'Лхагва', 'Пүрэв']
print(item)         # Баасан


# del keyword
del weekdays[0]
print(weekdays)     # ['Мягмар', 'Лхагва', 'Пүрэв']

# delete whole list
del weekdays

#clear()
weekends = ['Бямба', 'Ням']
weekends.clear()
print(weekends)     # []

# copy()
days = ['Даваа', 'Мягмар', 'Лхагва']
newdaylist = days.copy()
days.append('Пүрэв')
print(days)         # ['Даваа', 'Мягмар', 'Лхагва', 'Пүрэв']
print(newdaylist)   # ['Даваа', 'Мягмар', 'Лхагва']


# list()
anotherdaylist = list(newdaylist)
newdaylist.append('Thursday')
print(newdaylist)       # ['Даваа', 'Мягмар', 'Лхагва', 'Thursday']
print(anotherdaylist)   # ['Даваа', 'Мягмар', 'Лхагва']



# join + operator
list1 = ['Monday']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)        # ['Monday', 1, 2, 3]


# extend()
list1 = ['Monday']
list2 = [1, 2, 3]
list2.extend(list1)
print(list2)        # [1, 2, 3, 'Monday']

