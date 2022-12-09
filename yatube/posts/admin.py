from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pud_date', 'author')
    search_fields = ('text',)
    list_filter = ('pud_date',)
    empty_value_display = '-пусто-'
    
admin.site.register(Post, PostAdmin)
