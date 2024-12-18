from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('home')


class LogoutConfirmView(TemplateView):
    template_name = 'registration/logout.html'


def home_view(request):
    """
    Главная страница: проверяет авторизацию пользователя и перенаправляет
    на страницу, соответствующую его роли. Если пользователь не залогинен,
    перенаправляет на страницу логина.
    """
    if not request.user.is_authenticated:
        return redirect('login')  # Редирект на страницу логина

    # Если пользователь залогинен, проверяем его роль
    if request.user.role == 'store':
        return redirect('store_tasks')  # Редирект для роли 'store'
    elif request.user.role == 'operator':
        return redirect('operator_tasks')  # Редирект для роли 'operator'
    elif request.user.is_superuser:
        return redirect('admin/')
