from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home,name="home"),
    path("sign-up",views.sign_up,name="sign-up"),
    path("logout", views.LogOut, name="logout"),
    path("createpost", views.createpost, name="createpost"),
    # path("activate/<uidb64>/<token>",views.activateview,name="activate")
    
    
]
