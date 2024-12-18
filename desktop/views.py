from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def store_tasks_view(request):
    """
    View для отображения задач пользователя с ролью store.
    """
    if request.user.role != 'store':
        return redirect('role_redirect')  # Перенаправляем, если роль не store

    tasks = Task.objects.filter(created_by=request.user)
    return render(request, 'desktop/store_tasks.html', {'tasks': tasks})


@login_required
def operator_tasks_view(request):
    """
    View для отображения задач для пользователей с ролью operator.
    """
    if request.user.role != 'operator':
        return redirect('role_redirect')  # Перенаправляем, если роль не operator

    tasks = Task.objects.all()
    return render(request, 'desktop/operator_tasks.html', {'tasks': tasks})


@login_required
def role_based_redirect_view(request):
    """
    Редирект после логина в зависимости от роли пользователя.
    """
    if request.user.role == 'store':
        return redirect('store_tasks')
    elif request.user.role == 'operator':
        return redirect('operator_tasks')
    elif request.user.is_superuser:
        return redirect('admin/')
