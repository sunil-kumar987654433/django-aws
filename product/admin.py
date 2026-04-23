from django.contrib import admin

# Register your models here.
from product.models import Product

@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ("id", 'user', 'produt_name',)