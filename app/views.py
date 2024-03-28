
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.template import loader
from .models import *
import json
from django.http import JsonResponse


def index(request):
    return render(request,"index.html")
def buy(request):
   return render(request,"buy.html")
def base(request):
    return render(request,"base.html")
def homi(request):
    return render(request,"homi.html")

def cart_page(request):
  if request.user.is_authenticated:
     cart=Cart.objects.filter(user=request.user)
     return render(request,"cart.html",{"cart":cart})
  else:
     return redirect("/")


def remove_cart(request,cid):
  cartitem=Cart.objects.get(id=cid)
  cartitem.delete()
  return redirect("/cart")
  

def add_to_cart(request):
 
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
      if request.user.is_authenticated:
         data=json.load(request)
         product_qty=data['product_qty']
         product_id=data['pid']
         
         
         #print(request.user.id)
         
     
         product_status=Sou.objects.get(id=product_id)
         if product_status:
            if Cart.objects.filter(user=request.user.id,product_id=product_id):
              return JsonResponse({'status':'Product already in cart'},status=200)
            else:
               if product_status.quantity>=product_qty:
                  Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                  return JsonResponse({'status':'Product added to cart'},status=200)
               else: 
                  return JsonResponse({'status':'Product stock not available'},status=200)
         
         product_status=Pro.objects.get(id=product_id)
         if product_status:
            if Cart.objects.filter(user=request.user.id,product_id=product_id):
              return JsonResponse({'status':'Product already in cart'},status=200)
            else:
               if product_status.quantity>=product_qty:
                  Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                  return JsonResponse({'status':'Product added to cart'},status=200)
               else: 
                  return JsonResponse({'status':'Product stock not available'},status=200)
        
        
         
               
      else:
         return JsonResponse({'status':'Login to Add cart'},status=200)
      
      
         
   else:
      return JsonResponse({'status':'Invalid Access'},status=200)
   

   
               
               
  
  


      
  
   

  
   
   


def briyani(request):
    category=Category.objects.filter(status=0)
    return render(request,"briyani.html",{"category":category})
def briyaniview(request,name):
  if(Category.objects.filter(status=0,name=name)):
    products=Pro.objects.filter(category__name=name)
    return render(request,"b1.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No such Category Found")
    return redirect('biryani')
  
def product_details(request,cname,pname):
  if(Category.objects.filter(name=cname,status=0)):
    if(Pro.objects.filter(name=pname,status=0)):
        products=Pro.objects.filter(name=pname,status=0).first()
        return render(request,"product_details.html",{"products":products})
    else:
     messages.error(request,"No such Category Found")
     return redirect('biryani')
      
  else:
    messages.error(request,"No such Category Found")
    return redirect('biryani')
      
     





    
def southindian(request):
    south=South.objects.filter(status=0)
    return render(request,"south indian.html",{"south":south})
def southindianview(request,name):
  if(South.objects.filter(status=0,name=name)):
    products=Sou.objects.filter(category__name=name)
    return render(request,"b2.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No such Category Found")
    return redirect('southindian')
def product_details1(request,cname,pname):
  if(South.objects.filter(name=cname,status=0)):
    if(Sou.objects.filter(name=pname,status=0)):
        products=Sou.objects.filter(name=pname,status=0).first()
        return render(request,"product_details1.html",{"products":products})
    else:
     messages.error(request,"No such Category Found")
     return redirect('southindian')
      
  else:
    messages.error(request,"No such Category Found")
    return redirect('southindian')
  

  


def northindian(request):
    north=North.objects.filter(status=0)
    return render(request,"north indian.html",{"north":north})
def northindianview(request,name):
  if(North.objects.filter(status=0,name=name)):
    products=Nor.objects.filter(category__name=name)
    return render(request,"b3.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No such Category Found")
    return redirect('north indian')
def product_details2(request,cname,pname):
  if(North.objects.filter(name=cname,status=0)):
    if(Nor.objects.filter(name=pname,status=0)):
        products=Nor.objects.filter(name=pname,status=0).first()
        return render(request,"product_details2.html",{"products":products})
    else:
     messages.error(request,"No such Category Found")
     return redirect('north indian')
      
  else:
    messages.error(request,"No such Category Found")
    return redirect('north indian')
  
  


def chinese(request):
    chinese=Chinese.objects.filter(status=0)
    return render(request,"chinese.html",{"chinese":chinese})
def chineseview(request,name):
  if(Chinese.objects.filter(status=0,name=name)):
    products=Chin.objects.filter(category__name=name)
    return render(request,"b4.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No such Category Found")
    return redirect('chinese')
def product_details3(request,cname,pname):
  if(Chinese.objects.filter(name=cname,status=0)):
    if(Chin.objects.filter(name=pname,status=0)):
        products=Chin.objects.filter(name=pname,status=0).first()
        return render(request,"product_details3.html",{"products":products})
    else:
     messages.error(request,"No such Category Found")
     return redirect('chinese')
      
  else:
    messages.error(request,"No such Category Found")
    return redirect('chinese')
  


def desert(request):
    desert=Desert.objects.filter(status=0)
    return render(request,"desert.html",{"desert":desert})
def desertview(request,name):
  if(Desert.objects.filter(status=0,name=name)):
    products=Des.objects.filter(category__name=name)
    return render(request,"b5.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No such Category Found")
    return redirect('desert')
def product_details4(request,cname,pname):
  if(Desert.objects.filter(name=cname,status=0)):
    if(Des.objects.filter(name=pname,status=0)):
        products=Des.objects.filter(name=pname,status=0).first()
        return render(request,"product_details4.html",{"products":products})
    else:
     messages.error(request,"No such Category Found")
     return redirect('desert')
      
  else:
    messages.error(request,"No such Category Found")
    return redirect('desert')



def mojito(request):
    mojito=Mojito.objects.filter(status=0)
    return render(request,"mojito.html",{"mojito":mojito})
def mojitoview(request,name):
  if(Mojito.objects.filter(status=0,name=name)):
    products=Moji.objects.filter(category__name=name)
    return render(request,"b6.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No such Category Found")
    return redirect('mojito')
def product_details5(request,cname,pname):
  if(Mojito.objects.filter(name=cname,status=0)):
    if(Moji.objects.filter(name=pname,status=0)):
        products=Moji.objects.filter(name=pname,status=0).first()
        return render(request,"product_details5.html",{"products":products})
    else:
     messages.error(request,"No such Category Found")
     return redirect('mojito')
      
  else:
    messages.error(request,"No such Category Found")
    return redirect('mojito')
  
def italian(request):
    italian=Italian.objects.filter(status=0)
    return render(request,"Italian.html",{"italian":italian})
def italianview(request,name):
  if(Italian.objects.filter(status=0,name=name)):
    products=Ital.objects.filter(category__name=name)
    return render(request,"b7.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No such Category Found")
    return redirect('italian')
def product_details6(request,cname,pname):
  if(Italian.objects.filter(name=cname,status=0)):
    if(Ital.objects.filter(name=pname,status=0)):
        products=Ital.objects.filter(name=pname,status=0).first()
        return render(request,"product_details6.html",{"products":products})
    else:
     messages.error(request,"No such Category Found")
     return redirect('italian')
      
  else:
    messages.error(request,"No such Category Found")
    return redirect('italian')


  





def chaat(request):
    chaat=Chaat.objects.filter(status=0)
    return render(request,"chaat.html",{"chaat":chaat})
def chaatview(request,name):
  if(Chaat.objects.filter(status=0,name=name)):
    products=Cha.objects.filter(category__name=name)
    return render(request,"b8.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No such Category Found")
    return redirect('chaat')
def product_details7(request,cname,pname):
  if(Chaat.objects.filter(name=cname,status=0)):
    if(Cha.objects.filter(name=pname,status=0)):
        products=Cha.objects.filter(name=pname,status=0).first()
        return render(request,"product_details7.html",{"products":products})
    else:
     messages.error(request,"No such Category Found")
     return redirect('chaat')
      
  else:
    messages.error(request,"No such Category Found")
    return redirect('chaat')

  

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

def hh(request):
   mydata=Datas.objects.all()
   if(mydata!=""):
       return render(request,"base.html",{"datas":mydata})
   else:
      return render(request,"base.html")
   
def addData(request):
   if request.method=="POST":
      message=request.POST["Message"]
      obj=Datas()
      obj.Message=message
      obj.save()
      mydata=Datas.objects.all()
      return redirect("hh")
   return render(request,"base.html")

def hhi(request):
   mydata=Data.objects.all()
   if(mydata!=""):
       return render(request,"base.html",{"datas":mydata})
   else:
      return render(request,"base.html")
   
def addD(request):
   if request.method=="POST":
      photos=request.POST["Photos"]
      obj=Data()
      obj.Photos=photos
      obj.save()
      mydata=Data.objects.all()
      return redirect("hhi")
   return render(request,"base.html")

def hi(request):
   mydata=Dat.objects.all()
   if(mydata!=""):
       return render(request,"base.html",{"datas":mydata})
   else:
      return render(request,"base.html")

def add(request):
   if request.method=="POST":
      issue=request.POST["Issue"]
      obj=Dat()
      obj.Issue=issue
      obj.save()
      mydata=Dat.objects.all()
      return redirect("hi")
   return render(request,"base.html")


def favviewpage(request):
  if request.user.is_authenticated:
    fav=Favourite.objects.filter(user=request.user)
    return render(request,"fav.html",{"fav":fav})
  else:
    return redirect("/")
 
def remove_fav(request,fid):
  item=Favourite.objects.get(id=fid)
  item.delete()
  return redirect("/favviewpage")

def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']
      product_status=Pro.objects.get(id=product_id)
      if product_status:
         if Favourite.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Favourite'}, status=200)
         else:
          Favourite.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Product Added to Favourite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
   
 