from django.urls import path

from mediflow.apps.users.views import (
    HomeView,
    LoginView,
    LogoutView,
    UserSearchView,
    UserCreateView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/search/', UserSearchView.as_view(), name='user_search'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
]
