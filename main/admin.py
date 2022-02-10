from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug":("name",)}   

@admin.register(Cat)
class AdminCat(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug":("name",)} 

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ["name","price", "in_stock"]
    list_editable = ["price", "in_stock"]
    list_filter = ["price", "name", "category"]
    prepopulated_fields = {"slug":("name",)}