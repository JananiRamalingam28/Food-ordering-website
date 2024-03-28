"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views
 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index,name='index'),
    path('',views.base,name='base'),
    path('homi',views.homi,name='homi'),
    path('buy',views.buy,name='buy'),

    path("briyani",views.briyani,name='briyani'),
    path("briyani/<str:name>",views.briyaniview,name='briyani'),
    path("briyani/<str:cname>/<str:pname>",views.product_details,name='product_details'),
    
    
    path("southindian",views.southindian,name='southindian'),
    path("southindian/<str:name>",views.southindianview,name='southindian'),
    path("southindian/<str:cname>/<str:pname>",views.product_details1,name='product_details1'),
   

    
    path("northindian",views.northindian,name='northindian'),
    path("northindian/<str:name>",views.northindianview,name='northindian'),
    path("northindian/<str:cname>/<str:pname>",views.product_details2,name='product_details2'),

    path("chinese",views.chinese,name='chinese'),
    path("chineseview/<str:name>",views.chineseview,name='chinese'),
   path("chinese/<str:cname>/<str:pname>",views.product_details3,name='product_details3'),


    

    



    path("desert",views.desert,name='desert'),
    path("desert/<str:name>",views.desertview,name='desert'),
    path("desert/<str:cname>/<str:pname>",views.product_details4,name='product_details4'),


    path("mojito",views.mojito,name='mojito'),
    path("mojito/<str:name>",views.mojitoview,name='mojito'),
    path("mojito/<str:cname>/<str:pname>",views.product_details5,name='product_details5'),

    path("italian",views.italian,name='italian'),
    path("italian/<str:name>",views.italianview,name='italian'),
    path("italian/<str:cname>/<str:pname>",views.product_details6,name='product_details6'),



   path("chaat",views.chaat,name='chaat'),
    path("chaat/<str:name>",views.chaatview,name='chaat'),
    path("chaat/<str:cname>/<str:pname>",views.product_details7,name='product_details7'),



    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    
    
    path('cart',views.cart_page,name='cart'),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('addtocart',views.add_to_cart,name='addtocart'),

   

    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),


    path("hh",views.hh,name="hh"),
    path("addData",views.addData,name="addData"),


    path("hhi",views.hhi,name="hhi"),
    path("addD",views.addD,name="addD"),

     path("hi",views.hi,name="hi"),
    path("add",views.add,name="add"),

   


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
