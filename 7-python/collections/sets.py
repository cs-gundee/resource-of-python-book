# set үүсгэх
colors = {'улаан', 'ногоон', 'шар'}
print(colors)       # {'улаан', 'шар', 'ногоон'}


# давталт
for x in colors:
    print(x)
    # ногоон
    # улаан
    # шар

print('улаан' in colors)    # True


# add()
colors.add('цэнхэр')
print(colors)       
# {'шар', 'ногоон', 'цэнхэр', 'улаан'}


# update()
colors.update(['цагаан', 'ягаан'])
print(colors)
# {'ягаан', 'шар', 'цэнхэр', 'улаан', 'ногоон', 'цагаан'}


# len()
print(len(colors))  # 6


# remove()
# устгахаас өмнө {'цагаан', 'ногоон', 'улаан', 'шар', 'ягаан', 'цэнхэр'}
colors.remove('цагаан')
print(colors)
# устгасны дараа {'ногоон', 'улаан', 'шар', 'ягаан', 'цэнхэр'}
# colors.remove('хар')    # Алдаа заана
                        # KeyError: 'хар'

# discard()
# устгахаас өмнө {'шар', 'улаан', 'ягаан', 'цэнхэр', 'ногоон'}
colors.discard('шар')
print(colors)
# устгасны дараа {'ягаан', 'ногоон', 'цэнхэр', 'улаан'}
colors.discard('хар')   # алдаа заахгүй


# pop()
# устгахаас өмнө {'ягаан', 'ногоон', 'цэнхэр', 'улаан'}
x = colors.pop()
print(colors)   # {'улаан', 'ногоон', 'ягаан'}
print(x)        # цэнхэр


# clear()
numbers = {5, 6, 7}
numbers.clear()
print(numbers)      # set()


# del
numbers = {8, 6, 7}
del numbers


# union()
set1 = {1, 5, 10}
set2 = {'улаан', 'ногоон'}
set3 = set1.union(set2)
print(set3)     # {1, 'ногоон', 5, 'улаан', 10}


# update()
set1.update(set2)
print(set1)     # {1, 5, 'улаан', 10, 'ногоон'}


# давхардал
sets = {1, 1, 2, 8}
print(sets)     # {8, 1, 2}
print(len(sets))    # 3


# байгуулагч функц
newset = set((5, 8, 'цагаан'))
print(newset)       # {8, 'цагаан', 5}
