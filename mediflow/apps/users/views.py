from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, FormView, CreateView
from django.http.request import HttpRequest
from django.http import HttpResponse
from django.urls import reverse_lazy
from django import http
from typing import Any

from .models import UserModel
from .forms import UserForm, UserSearchForm


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


class UserSearchView(FormView):
    template_name = 'user_search.html'
    form_class = UserSearchForm

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        users = UserModel.objects.all()
        if 'query' in request.GET:
            query = request.GET.get('query')
            if query:
                users = users.filter(username__icontains=query)
        context = self.get_context_data(form=form, users=users)
        return self.render_to_response(context)


class UserCreateView(CreateView):
    model = UserModel
    form_class = UserForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('patient_create')


class LogoutView(LogoutView):

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mediflow'
        return context
