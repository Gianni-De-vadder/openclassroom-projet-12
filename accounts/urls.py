from django.urls import path
from accounts.views import RegistrationView, LoginView

app_name = "accounts"

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
