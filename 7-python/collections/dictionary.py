# dictionary
mydictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
print(mydictionary)
# {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


# байгуулагч ашиглах
mydictionary = dict(key1 = "value1", key2 = "value2", key3 = "value3")
print(mydictionary)
#  {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


# элементэд хандах
countryCodes = {
    "976": "Монгол",
    "7": "Орос",
    "86": "Хятад",
    "49": "Герман"
}
print(countryCodes["7"])      # Орос

print(countryCodes.get("49"))   # Герман

countryCodes["49"] = "Germany"
print(countryCodes)
# {'976': 'Монгол', '7': 'Орос', '86': 'Хятад', '49': 'Germany'}


# давталтаар түлхүүрийг буцаах
# {'976': 'Монгол', '7': 'Орос', '86': 'Хятад', '49': 'Germany'}
for x in countryCodes:
    print(x)

# Үр дүн: 976
#           7
#          86
#          49


# давталтаар түлхүүрт харгалзах утгуудыг гаргаж авах
# {'976': 'Монгол', '7': 'Орос', '86': 'Хятад', '49': 'Germany'}
for x in countryCodes:
    print(countryCodes[x])

# Үр дүн: Монгол
#         Орос
#         Хятад
#         Germany


# values()
# {'976': 'Монгол', '7': 'Орос', '86': 'Хятад', '49': 'Germany'}
for x in countryCodes.values():
    print(x)

# Үр дүн:   Монгол
#           Орос
#           Хятад
#           Germany


# items()
# {'976': 'Монгол', '7': 'Орос', '86': 'Хятад', '49': 'Germany'}
for x, y  in countryCodes.items():
    print(x, y)
# Үр дүн:   976 Монгол
#           7 Орос
#           86 Хятад
#           49 Germany


# len()
# {'976': 'Монгол', '7': 'Орос', '86': 'Хятад', '49': 'Germany'}
print(len(countryCodes))    # 4


# шинэ элемент нэмэх
countryCodes["351"] = "Португал"
print(countryCodes)
# {'976': 'Монгол', '7': 'Орос', '86': 'Хятад', '49': 'Germany', '351': 'Португал'}


# pop()
# Устгахаас өмнө: {'976': 'Монгол', '7': 'Орос', '86': 'Хятад', '49': 'Germany', '351': 'Португал'}
countryCodes.pop("86")
print(countryCodes)
# Устгасны дараа: {'976': 'Монгол', '7': 'Орос', '49': 'Germany', '351': 'Португал'}


# popitem()
# Устгахаас өмнө: {'976': 'Монгол', '7': 'Орос', '49': 'Germany', '351': 'Португал'}
countryCodes.popitem()
print(countryCodes)
# Устгасны дараа: {'976': 'Монгол', '7': 'Орос', '49': 'Germany'}


# del
# Устгахаас өмнө: {'976': 'Монгол', '7': 'Орос', '49': 'Germany'}
del countryCodes["49"]
print(countryCodes)
# Устгасны дараа: {'976': 'Монгол', '7': 'Орос'}

# Толь бичгийг бүхэлд нь устгах
del countryCodes



# clear()
countryCode = {
    "974": "Катар",
    "65": "Сингапур"
}
countryCode.clear()
print(countryCode)      # {}


# copy()
countryCode = {
    "974": "Катар",
    "65": "Сингапур"
}
newCodes = countryCode.copy()
print(newCodes)     # {'974': 'Катар', '65': 'Сингапур'}


# nested dictionary
devices = {
    "iphone": {
        "brand": "Apple",
        "os": "ios"
    },
    "galaxy": {
        "brand": "Samsung",
        "os": "android"
    }
}
print(devices)
# {'iphone': {'brand': 'Apple', 'os': 'ios'}, 'galaxy': {'brand': 'Samsung', 'os': 'android'}}


# nested dictionary version 2
iphone = {
    "brand": "Apple",
    "os": "ios"
}
print(iphone)
# {'brand': 'Apple', 'os': 'ios'}

galaxy = {
    "brand": "Samsung",
    "os": "android"
}
print(galaxy)
# {'brand': 'Samsung', 'os': 'android'}

devices = {
    "iphone": iphone,
    "galaxy": galaxy
}
print(devices)
# {'iphone': {'brand': 'Apple', 'os': 'ios'}, 'galaxy': {'brand': 'Samsung', 'os': 'android'}}