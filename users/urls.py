from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, MainNoRolePageView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),  # Страница логина
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Страница выхода через модльное окно
    path('', MainNoRolePageView.as_view(), name='main_no_role_page'),  # Временная главная страница для юзера без ролей
]
