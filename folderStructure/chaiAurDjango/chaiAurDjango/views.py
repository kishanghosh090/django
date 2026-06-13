from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    data = {
        "status": "success",
        "message": "Data retrieved successfully",
        "user": {
            "name": "kishan",
            "role": "Developer"
        }
    }
    return JsonResponse(data)

def about(request):
    return JsonResponse({"name": "chai aur code about"})

def contact(request):
    return JsonResponse({"name": "chai aur code contact"})


def template(request):
    return render(request,"index.html")