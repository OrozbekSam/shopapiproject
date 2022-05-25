from django.contrib import admin

# Register your models here.
from product.models import Product, Category, NewProduct

admin.site.register(Product)
admin.site.register(NewProduct)
admin.site.register(Category)