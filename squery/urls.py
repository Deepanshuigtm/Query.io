from django.urls import path
from . import views

urlpatterns = [
    path("",views.startingpage, name = "starting-page"),
    path("query",views.querys, name = "querys"),
    path("FAQ",views.faq, name ="faq"),
    path("register_parent",views.register_parent,name="register_parent"),
    path("register_student",views.register_student,name="register_student"),
    path("register_admin",views.register_admin,name="register_admin"),
    path("login/", views.handlelogin, name="Login"),

]