from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store_tasks_view, name='store_tasks'),
    path('operator/', views.operator_tasks_view, name='operator_tasks'),
    path('role-redirect/', views.role_based_redirect_view, name='role_redirect'),
]
