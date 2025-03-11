from django.db import models

from django.urls import reverse

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=250, db_index=True)
    
    slug = models.SlugField(max_length=250, unique=True)
    
    image = models.ImageField(upload_to='images/', null=True)
    
    
    class Meta:
        
        verbose_name_plural = 'categories'
        
    def __str__(self):
        
        return self.name
    
    def get_absolute_url(self):
        
        return reverse("category", args=[self.slug])
    
class Brand(models.Model):
    
    title = models.CharField(max_length=250)
    
    slug= models.SlugField(max_length=250, unique=True, null=True)
    
    def __str__(self):
        
        return self.title
    
class Current(models.Model):
    
    title = models.CharField(max_length=250)
    
    slug = models.SlugField(max_length=250, unique=True, null=True)
       
    def __str__(self):
        
        return self.title
    
class Product(models.Model):
    
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    
    title = models.CharField(max_length=250)
    
    brand = models.ForeignKey(Brand, related_name='product', on_delete=models.CASCADE, null=True)
    
    description = models.TextField(blank=True)
    
    slug = models.SlugField(max_length=255)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    current = models.ForeignKey(Current, related_name='product', on_delete=models.CASCADE, null=True)
    
    image = models.ImageField(upload_to='images/')
    
    
    class Meta:
        
        verbose_name_plural = 'products'
        
    def __str__(self):
        
        return self.title
    
    def get_absolute_url(self):
        
        return reverse("product_page", args=[self.slug])
    