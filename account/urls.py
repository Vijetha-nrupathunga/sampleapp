from django.contrib import admin
from django.urls import path,include

from account import views

from home.views import home_view,about,contact,deletestudent,editstudent,createstudent
from home import views
urlpatterns = [
    #path('',home_view),
    path('home/',include('home.urls')),
    path('admin/',admin.site.urls),
    path('',views.home_view),
]