from django.contrib import admin
from . models import Task, Photo


class PhotoInline(admin.TabularInline):
    """
    Позволяет добавлять и редактировать фотографии, связанные с задачей, прямо из интерфейса админки.
    """
    model = Photo
    extra = 1  # Количество пустых полей для добавления новых фотографий
    fields = ('image',)  # Отображаем только поле image


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Настройка отображения задач в админке.
    """
    list_display = ('id', 'status', 'created_by', 'processed_by', 'comment', 'created_at', 'updated_at')
    list_filter = ('status', 'created_by', 'processed_by', 'created_at')
    search_fields = ('comment', 'created_by__username', 'processed_by__username')
    readonly_fields = ('created_at', 'updated_at')  # Поля только для чтения
    inlines = [PhotoInline]  # Подключение связанных фотографий


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """
    Отдельная регистрация модели Photo для прямого редактирования, если потребуется.
    """
    list_display = ('id', 'task', 'image')
    list_filter = ('task',)
    search_fields = ('task__id',)
