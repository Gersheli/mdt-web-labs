from django.contrib import admin
from .models import Usluga, Author, Genre, Client, Post


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Usluga)
class UslugaAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'author', 'description', 'genre', 'cost', 'status', 'purchase_count']
    list_filter = ['genre', 'author']
    # №def get_author(self, obj):
    # return "\n".join([p.name for p in obj.author.all()])


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth',
                    'email', 'phone_number']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
