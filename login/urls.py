from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("login/<int:errCode>", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("changepassword/", views.changePassword, name="changePassword"),
]