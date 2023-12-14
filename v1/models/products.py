from django.db import models
from v1.utils.abstracts import BaseAbstractModel
from v1.models.users import Staff, Customer
from v1.utils.enums import CustomerCategory


class Category(BaseAbstractModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.id} - {self.name}'
    

class Department(BaseAbstractModel):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE, related_name='department_staff')
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name='department_category')
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.id} - {self.name}'


class Product(BaseAbstractModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self) -> str:
        return f'{self.id} - {self.name} - {self.category.name}'


class Cart(BaseAbstractModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.id} - {self.product.name}'


class Discount(BaseAbstractModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    customer_category = models.CharField(max_length=6, choices=CustomerCategory.choices())
    percentage = models.FloatField()
    