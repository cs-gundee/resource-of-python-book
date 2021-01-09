# tuple үүсгэх
mountains = ('Хэнтий', 'Хангай', 'Алтай')
print(mountains)        # ('Хэнтий', 'Хангай', 'Алтай')

# tuple()
mount = tuple(('Хэнтий', 'Хангай'))
print(mount)            # ('Хэнтий', 'Хангай')

# элементэд хандах
print(mountains[1])     # Хангай

# жагсаалт руу хөрвүүлж элементүүдийг өөрчлөх
list = list(mountains)
list.append('Соён')
mountains = tuple(list)

print(mountains)
# ('Хэнтий', 'Хангай', 'Алтай', 'Соён')

# count()
mountains = ('Хэнтий', 'Хангай', 'Алтай', 'Хангай')
print(mountains.count('Хангай'))    # 2
print(mountains.count('Хэнтий'))    # 1

# index()
print(mountains.index('Хэнтий'))    # 0