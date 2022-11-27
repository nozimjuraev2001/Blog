from django.contrib import admin
from .models import AuthorModel, PublisherModel, PostModel
# Register your models here.

@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', )

@admin.register(PublisherModel)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    list_display_links = ('id', )

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', )