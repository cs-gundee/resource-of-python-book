# decorator function
def medeeleh(f):
    def hureelegch():
        print("Функц ажиллаж эхэллээ...")
        f()
        print("Функц ажиллаж дууслаа...")
    return hureelegch

@medeeleh
def function():
    print("Туршилтын функц")

function()

""" Үр дүн: Функц ажиллаж эхэллээ...
            Туршилтын функц
            Функц ажиллаж дууслаа... """