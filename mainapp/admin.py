from django.contrib import admin
from .models import Contact, Product, ProductCategory

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Contact)