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

    path("briyani",views.briyani,name='briyani'),
    path("briyani/<str:name>",views.briyaniview,name='briyani'),

    path("southindian",views.southindian,name='southindian'),
    path("northindian",views.northindian,name='northindian'),
    path("chinese",views.chinese,name='chinese'),
    path("italian",views.italian,name='italian'),
    path("desert",views.desert,name='desert'),
    path("mojito",views.mojito,name='mojito'),
    path("chaat",views.chaat,name='chaat'),

    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
