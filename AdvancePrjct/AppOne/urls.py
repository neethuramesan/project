
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    path('welcome',views.welcome,name='welcome'),
    path('apptwohome',views.apptwohome,name='apptwohome')

]
