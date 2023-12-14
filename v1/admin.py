from django.contrib import admin
from v1.models.users import User, Staff, Customer, UserEmailVerify
from v1.models.products import Product, Department, Cart, Category, Discount
from v1.models.orders import Order, OrderItem


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'customer_category', 'percentage', 'created_at')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'country', 'created_at')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price', 'created_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'price', 'created_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity', 'created_at', 'updated_at')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'staff', 'category', 'created_at', 'updated_at')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", 'email', 'is_staff')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("id", "email", 'first_name', 'last_name')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", 'email', 'is_email_verified', 'customer_category')


@admin.register(UserEmailVerify)
class UserEmailVerifyAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'code')
