
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.template import loader
from .models import *

def index(request):
    return render(request,"index.html")
def base(request):
    return render(request,"base.html")
def homi(request):
    return render(request,"homi.html")

def briyani(request):
    category=Category.objects.filter(status=0)
    return render(request,"briyani.html",{"category":category})
def briyaniview(request,name):
  if(Category.objects.filter(status=0,name=name)):
    products=Pro.objects.filter(category__name=name)
    return render(request,"b1.html",{"products":products})
  else:
    messages.warning(request,"No such Category Found")
    return redirect('biryani')



    
def southindian(request):
    south=South.objects.filter(status=0)
    return render(request,"south indian.html",{"south":south})
def northindian(request):
    north=North.objects.filter(status=0)
    return render(request,"north indian.html",{"north":north})
def chinese(request):
    chinese=Chinese.objects.filter(status=0)
    return render(request,"chinese.html",{"chinese":chinese})
def italian(request):
    italian=Italian.objects.filter(status=0)
    return render(request,"Italian.html",{"italian":italian})
def desert(request):
    desert=Desert.objects.filter(status=0)
    return render(request,"desert.html",{"desert":desert})
def mojito(request):
    mojito=Mojito.objects.filter(status=0)
    return render(request,"mojito.html",{"mojito":mojito})
def chaat(request):
    chaat=Chaat.objects.filter(status=0)
    return render(request,"chaat.html",{"chaat":chaat})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log innow!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)
#def login(request):
    return render(request,"login.html")
def logout(request):
    return render(request,"logout.html")



# Create your views here.
