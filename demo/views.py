from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'one/home.html')
def services(request):
    return render(request,'one/services.html')
def contact(request):
    return render(request,'one/contact.html')
def skill(request):
    return render(request,'one/skill.html')