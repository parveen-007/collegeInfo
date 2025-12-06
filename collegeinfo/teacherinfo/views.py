from django.shortcuts import render
def landingpage(request):
    return render(request,'landingpage.html')
# Create your views here.
def login(request):
    return render(request,'login.html')