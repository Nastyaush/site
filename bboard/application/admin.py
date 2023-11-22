from django.contrib import admin

# Register your models here.
from .models import Application, Category

admin.site.register(Application)
admin.site.register(Category)
