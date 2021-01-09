# Модулийн тодорхой хэсгийг импортлох
""" from functions import square

for i in range(3,6):
    print(f"{i} -н квадрат: {square(i)}") """


# Модулийг бүхэлд нь импортлох
""" import functions

for i in range(3,6):
    print(f"{i} -н квадрат: {functions.square(i)}")
 """



# Модулийг дахин нэрлэх
import functions as f

for i in range(3,6):
    print(f"{i} -н квадрат: {f.square(i)}")