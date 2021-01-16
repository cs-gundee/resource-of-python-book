from django.shortcuts import render
from django import forms

# шинээр импортлох
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

# Сешн ашиглах тул глобал хувьсагч хэрэггүй боллоо.
# tasks = ["Даалгавар 1", "Даалгавар 2", "Даалгавар 3"]

def index(request):
    # Сешнд "tasks" түлхүүр байгаа эсэхийг шалгах
    if "tasks" not in request.session:
        # Байхгүй бол шинэ жагсаалт үүсгэх
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
        # "tasks": tasks
    })

"""
def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
"""

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Шинэ зүйл нэмэх")
    # priority = forms.IntegerField(label="Эрэмбэ", min_value=1, max_value=3)

# шинэ зүйл нэмэх
def add(request):

    # хүсэлт нь POST бол
    if request.method == "POST":

        # Хэрэглэгчийн илгээсэн өгөгдлийг авч, form хувьсагчид хадгалах
        form = NewTaskForm(request.POST)

        # (server-side) Илгээсэн өгөгдөл зөв эсэх
        if form.is_valid():

            # Өгөгдлийг цэвэрлэх
            task = form.cleaned_data["task"]
            
            # Шинэ хийх зүйлийг tasks жагсаалт руу нэмэх
            #tasks.append(task)
            request.session["tasks"] += [task]

            # Хэрэглэгчид index хуудсыг харуулах замчлал
            return HttpResponseRedirect(reverse("tasks:index"))
        
        else:            
            # Form зөвшөөрөгдөхгүй бол add.html хуудсыг одоо байгаа өгөгдлийн хамт дахин үзүүлэх
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })