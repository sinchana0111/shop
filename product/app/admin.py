from django.contrib import admin
from .models import *

@admin.register(SizeCategory)
class SizeCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
   

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product_category_id', 'category_name', 'parent_category', 'size_category','slug')
    

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=['brand_id','brand_name','brand_description']
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'brand', 'product_category')
    


@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    list_display = ('colour_id', 'colour_name')
   
@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('product_item_id', 'product', 'colour', 'original_price', 'sale_price','image1','image2','image3','slug')
   

@admin.register(SizeOption)
class SizeOptionAdmin(admin.ModelAdmin):
    list_display = ('size_id', 'size_name', 'sort_order', 'size_category')
    
@admin.register(ProductVariation)
class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ('variation_id', 'product_item', 'size', 'qty_in_stock')
    

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image_id', 'product_item', 'image_filename')

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'full_name', 'username', 'email', 'phone_number')
   
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user','street_address','apartment_address','country','pincode','address_type','default')
   
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'timestamp')
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'productitem', 'quantity', 'size', 'ordered')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','start_date','ordered_date','ordered','being_delivered','received','refund_requested','refund_granted')
   