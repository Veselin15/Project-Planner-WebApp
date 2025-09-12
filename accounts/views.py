from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserRegisterForm, UserLoginForm

UserModel = get_user_model()

class RegisterView(CreateView):
    model = UserModel
    form_class = UserRegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        if response.status_code in [301, 302]:
            login(self.request, self.object)
        return response