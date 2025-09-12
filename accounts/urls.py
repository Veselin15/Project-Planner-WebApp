from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy, include
from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="accounts/login.html", next_page='home'), name="login"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
]