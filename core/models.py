import uuid
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from config.models import BaseModel

        
class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)  # SEO-friendly URL
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subcategories"
    )
    icon = models.ImageField(upload_to="categories/", null=True, blank=True)  
    class Meta:
        db_table = "category"
        ordering = ["name"]  # alphabetical by default
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
        
class Product(BaseModel):
    name = models.CharField(max_length=200)
    # for seo friendly url 
    slug = models.SlugField(unique=True)  
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=50, unique=True)  # Stock Keeping Unit
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.CharField(max_length=100, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, default="USD")

    stock = models.PositiveIntegerField(default=0)

    image = models.ImageField(upload_to="products/", null=True, blank=True)

    class Meta:
        db_table = 'product'
        ordering = ["-created_at"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name