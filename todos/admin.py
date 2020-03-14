from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'todo', 'todo_date')
    list_display_links = ('id', 'title')


admin.site.register(Todo, TodoAdmin)