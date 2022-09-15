from django.contrib import admin
from .models import *

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
     date_hierarchy = 'pub_date'
     list_display = ['altText', 'pub_date', 'url']

admin.site.register(Slider,SliderAdmin)

class PlacesAdmin(admin.ModelAdmin):
     date_hierarchy = 'pub_date'
     list_display = ['title','about', 'pub_date']

admin.site.register(Places,PlacesAdmin)

class AuthoritiesAdmin(admin.ModelAdmin):
     list_display = ['name','designation','pub_date', ]

admin.site.register(Authorities,AuthoritiesAdmin)

class LatestnewsAdmin(admin.ModelAdmin):
     list_display = ['title','pub_date', 'link' ]

admin.site.register(Latestnews,LatestnewsAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)