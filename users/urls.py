from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, home_view

urlpatterns = [
    path('', home_view, name='home'),  # Главная страница
    path('login/', CustomLoginView.as_view(), name='login'),  # Страница логина
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Страница выхода через модльное окно
]
