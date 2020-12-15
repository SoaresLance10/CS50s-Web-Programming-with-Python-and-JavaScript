from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("EditProfile/<username>", views.profile, name="e_profile"),
    path("Profile/<username>", views.profile, name="profile"),
    path("NewPost/<username>", views.new_post, name="new")
]