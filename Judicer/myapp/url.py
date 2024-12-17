from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name="home"),
    path('login/',views.login_view,name="login"),
    path('register/',views.register,name="register"),
    path('dash/',views.dashboard,name="dashboard"),
    path('logout/',views.logout_view,name="logout"),
]