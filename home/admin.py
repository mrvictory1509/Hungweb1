from django.contrib import admin
from .models import User, Category, Sex, Shoes, Cart, Product, Bill

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Description']
    list_filter = ['Name']
    search_fields = ['Name']
admin.site.register(Category, CategoryAdmin)
class SexAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Description']
    list_filter = ['Name']
    search_fields = ['Name']
admin.site.register(Sex, SexAdmin)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Price', 'SexID', 'CategoryID', 'NumberBuy', 'Color', 'Style', 'Made_in', 'Sales', 'New_Price', 'Image']
    list_filter = ['CategoryID']
    search_fields = ['CategoryID']
admin.site.register(Shoes, ShoesAdmin)
class CartAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Quantity', 'UserID']
    list_filter = ['Name']
    search_fields = ['Name']
admin.site.register(Cart, CartAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Quantity', 'ShoesID']
    list_filter = ['Quantity']
    search_fields = ['Quantity']
admin.site.register(Product, ProductAdmin)
class BillAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Date', 'ProductID', 'Total_price']
    list_filter = ['Name']
    search_fields = ['Name']
admin.site.register(Bill, BillAdmin)
