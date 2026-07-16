from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post modelini admin panelda boshqarish."""
    
    list_display = ["title", "author", "created", "updated"]
    list_filter = ["created", "author"]
    search_fields = ["title", "body"]
    ordering = ["-created"]
    date_hierarchy = "created"