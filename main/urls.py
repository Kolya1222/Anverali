from django.urls import  path
from main.views import *
urlpatterns = [
    path('',menu,name = 'index'),
    path('register/',register_view,name = 'register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('admins/',admin_view,name='admin'),
    path('employer/',employer_view,name='employer'),
    path('executor/',executor_view,name='executor'),
]
