# класс зарлах
class Car():
    # байгуулагч функц
    def __init__(self, brand, car, etype):
        self.brandName = brand
        self.carName = car
        self.engineType = etype


# объект үүсгэх
car1 = Car('Toyota', 'Lexus RX 350', 'Hybrid')
car2 = Car('Mersedes-Benz', 'GLE450', 'Hybrid')

# объектын мэдээллийг хэвлэж харах
print(f"Үйлдвэрлэгч: {car1.brandName}\nМашины нэр: {car1.carName}\nХөдөлгүүр: {car1.engineType}\n")
print(f"Үйлдвэрлэгч: {car2.brandName}\nМашины нэр: {car2.carName}\nХөдөлгүүр: {car2.engineType}")

""" Үр дүн: Үйлдвэрлэгч: Toyota
            Машины нэр: Lexus RX 350
            Хөдөлгүүр: Hybrid

            Үйлдвэрлэгч: Mersedes-Benz
            Машины нэр: GLE450
            Хөдөлгүүр: Hybrid """


class Flight():
    def __init__(self, bagtaamj):
        self.capacity = bagtaamj    # нислэгийн суудлын тоо
        self.passengers = []        # зорчигчийг хадгалах жагсаалт

    def open_seats(self):
        return self.capacity - len(self.passengers)

    def add_passenger(self, name):
        if not self.open_seats():     # self.open_seats == 0
            return False            # сул суудалгүй бол бүртгэл хийхгүй
        else:
            self.passengers.append(name)
            return True             # сул суудалтай бол бүртгэл хийнэ

# шинэ нислэгийн объект үүсгэх
mnToKorea = Flight(3)

print(f"Сул суудлын тоо: {mnToKorea.open_seats()}") # Сул суудлын тоо: 3

people = ["Бат", "Болор", "Урангуа", "Од"]
for person in people: 
    if mnToKorea.add_passenger(person):
        print(f"{person} таны бүртгэл амжилттай.")
    else:
        print(f"{person} таны бүртгэл амжилтгүй.")

""" Үр дүн: Бат таны бүртгэл амжилттай.
            Болор таны бүртгэл амжилттай.
            Урангуа таны бүртгэл амжилттай.
            Од таны бүртгэл амжилтгүй. """

print(f"Сул суудлын тоо: {mnToKorea.open_seats()}") # Сул суудлын тоо: 0

