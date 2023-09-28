from django.contrib import admin
from .models.product import Product
from .models.category import Category

# the product admin will help to display in the admin name and quantity 
class ProductAdmin (admin.ModelAdmin):
    list_display=('name','category','quantity')
    # when we filter we must use , at the end to say it is turple else we use []to say is a list
    list_filter=('category',)
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)