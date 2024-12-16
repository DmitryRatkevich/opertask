from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class MainNoRolePageView(TemplateView):
    template_name = 'main_no_role_page.html'


class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('main_no_role_page')


class LogoutConfirmView(TemplateView):
    template_name = 'registration/logout.html'
