from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.index, name= 'index'),
    path('addition', views.addition, name="addition"),
    path('substraction', views.substraction, name="substraction"),
    path('multiplication', views.multiplication, name="multiplication"),
    path('division', views.division, name="division"),
  
  ]
