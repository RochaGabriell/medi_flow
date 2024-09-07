from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.http.request import HttpRequest
from django.http import HttpResponse
from django.urls import reverse_lazy
from django import http
from typing import Any


class HomeView(TemplateView):

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mediflow'
        return context


class LoginView(LoginView):

    template_name = 'auth/login.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return http.HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)


class LogoutView(LogoutView):

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mediflow'
        return context
