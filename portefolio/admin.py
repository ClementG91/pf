from django.contrib import admin
from portefolio.models import Photo, Blog

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'date_created', 'uploader')

admin.site.register(Photo, PhotoAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')

admin.site.register(Blog, BlogAdmin)