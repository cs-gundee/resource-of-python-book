import time, json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def posts(request):

    # Эхлэх ба дуусах цэгүүд
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Жагсаалтад пост үүсгэх
    data = []
    for i in range(start, end + 1):
        data.append(f"Бичвэр №{i}")

    # Response илгээх хугацааг зохиомлоор хойшлуулах
    time.sleep(1)

    # Постын жагсаалтыг буцаах
    return JsonResponse({
        "posts": data
    }, safe=False, json_dumps_params={'ensure_ascii':False})