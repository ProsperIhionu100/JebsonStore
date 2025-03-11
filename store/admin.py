from django.contrib import admin

from . models import Product, Category, Brand, Current

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    prepopulated_fields = { 'slug' : ('name',)}    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    prepopulated_fields = { 'slug' : ('title',)}
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    
    prepopulated_fields = { 'slug' : ('title',)}

@admin.register(Current)
class CurrentAdmin(admin.ModelAdmin):
    
    prepopulated_fields = { 'slug' : ('title',)}