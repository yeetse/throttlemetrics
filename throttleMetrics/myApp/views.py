from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "myApp/index.html", {})

def about(request):
    return render(request, "myApp/about.html", {})

def contact(request):
    return render(request, "myApp/contact.html", {})

def post1(request):
    return render(request, "myApp/post1.html", {})

def post2(request):
    return render(request, "myApp/post2.html", {})