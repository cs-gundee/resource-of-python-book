cars = [
    {"name": "R8 LMS", "mark": "Audi"},
    {"name": "G22", "mark": "BMW"},
    {"name": "Chiron", "mark": "Bugatti"}
]

""" def car_name(car):
    return car["name"] """

# cars.sort(key=car_name)

cars.sort(key=lambda car: car["mark"])
print(cars)
# Үр дүн: [{'name': 'R8 LMS', 'mark': 'Audi'}, 
#           {'name': 'G22', 'mark': 'BMW'}, 
#           {'name': 'Chiron', 'mark': 'Bugatti'}]
