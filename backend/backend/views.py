from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def catch_all(request, path):
    print(path)
    return render(request, "index.html")
