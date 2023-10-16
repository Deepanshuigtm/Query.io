from django.urls import path
from . import views

urlpatterns = [
    path("",views.startingpage, name = "starting-page"),
    path("query",views.querys, name = "querys"),
    path("FAQ",views.faq, name ="faq"),
    path("register_parent",views.register_parent,name="register_parent"),
    path("register_student",views.register_student,name="register_student"),
    path("register_admin",views.register_admin,name="register_admin"),
    path("signup/",views.signup, name='signup'),
    path("login/", views.handlelogin, name="Login"),
    path('create_post/', views.create_post, name='create_post'),
    path("logout/", views.handlelogout, name="Logout"),
    path("admin-dashboard/", views.adminDashboard, name = "admin_dash"),
    path("parent/", views.parent, name = "parent"),
    path('<int:post_id>/like/', views.like, name='like'),

    # path('vote/<int:post_id>/', views.like, name='vote_post'),


]