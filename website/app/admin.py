from django.contrib import admin

# Register your models here.
from .models import Category, SubCategory,Order

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Order)
