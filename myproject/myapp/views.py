from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def service_details(request):
    return render(request,'service_details.html')

def starter_page(request):
    return render(request,'starter_page.html')

# def admin(request):
    