from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('Title','Created_at')

admin.site.register(Category,CategoryAdmin) 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category','job_title','Description','Description2','Description3','image',)
    fields = ('title','category','job_title','Description','Description2','Description3','image',)

admin.site.register(Post,PostAdmin) 
