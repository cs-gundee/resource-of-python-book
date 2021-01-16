from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

""" 
def index(request):
    # return HttpResponse("Сайн байна уу?")
    return HttpResponse("Сайн уу?") 
"""

def index(request):
    return render(request, "hello/index.html")

def byrussian(request):
    return HttpResponse("Здравствуйте!")

def bychinese(request):
    return HttpResponse("你好!")

"""
def greetings(request, language):
    if "mongolian" in language:
        return HttpResponse("Сайн байна уу?")
    elif "chinese" in language:
        return HttpResponse("你好!")
    elif "russian" in language:
        return HttpResponse("Здравствуйте!")
    else:
        return HttpResponse("Hello!") 
"""

def greetings(request, language):
    if "mongolian" in language:
        return render(request, "hello/greetings.html", {
        "value": "Сайн байна уу! Эх дэлхий минь!",
        "type": "Монгол"
    })
    elif "chinese" in language:
        return render(request, "hello/greetings.html", {
        "value": "你好！ 我的祖國！",
        "type": "Chinese"
    })
    elif "russian" in language:
        return render(request, "hello/greetings.html", {
        "value": "Здравствуйте! Моя родина!",
        "type": "Russian"
    })
    else:
        return render(request, "hello/greetings.html", {
        "value": "Hello! My motherland!",
        "type": "English"
    })