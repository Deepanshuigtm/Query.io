from django.urls import path
from . import views

urlpatterns = [
    path("",views.startingpage, name = "starting-page"),
    path("query",views.querys, name = "querys"),
    path("FAQ",views.faq, name ="faq"),
    path("feedback",views.feedback, name ="feedback"),
    path("register_parent",views.register_parent,name="register_parent"),
    path("register_student",views.register_student,name="register_student"),
    path("register_admin",views.register_admin,name="register_admin"),
    path("signup/",views.signup, name='signup'),
    path("login/", views.handlelogin, name="Login"),
    path("adminlogin/", views.handlelogin_admin, name="adminlogin"),
    path('create_post/', views.create_post, name='create_post'),
    path("logout/", views.handlelogout, name="Logout"),
    path("admin-dashboard/", views.adminDashboard, name = "admin_dash"),
    path("parent/", views.parent, name = "parent"),
    path("rewards/", views.rewards, name = "rewards"),
    path("repeaterform/", views.repeaterform, name = "repeater_form"),
    path("parent/parent_graph", views.parent_graph, name = "parent_graph"),
    path('<int:post_id>/like/', views.like, name='like'),
    path('<int:post_id>/post_details/', views.post_details, name='post_details'),
    path('<int:user_id>/admin_rewards/', views.admin_rewards, name='admin_rewards'),

    # path('vote/<int:post_id>/', views.like, name='vote_post'),

]