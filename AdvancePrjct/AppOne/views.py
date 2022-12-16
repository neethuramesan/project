from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return render(request,'index.html')

def welcome(request):
    return render(request,'welcome.html')

#----------------------------------
# -----------
def apptwohome(request):
    return render(request,'home.html')
