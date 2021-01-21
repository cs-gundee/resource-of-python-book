from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")
    
def login_view(request):
    if request.method == "POST":
        # Формын өгөгдлөөс нэвтрэх нэр, нууц үгийг авах
        username = request.POST["username"]
        password = request.POST["password"]

        # Нэвтрэх нэр, нууц үг зөв бол өгөгдлийн санд байгаа User объектыг буцаана. 
        user = authenticate(request, username=username, password=password)
        # Хэрэглэгч олдсон бол index хуудас руу чиглүүлэх
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # Хэрэглэгч олдоогүй бол нэвтрэх хуудсыг дахин харуулах ба message хувьсагчийг дамжуулна.
        else:
            return render(request, "users/login.html", {
                "message": "Зөвшөөрөлгүй нэвтрэх оролдлого байна."
            })          
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Хэрэглэгч веб хуудаснаас гарлаа."
    })