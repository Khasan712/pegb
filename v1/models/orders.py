from django.db import models
from v1.models.users import Customer
from v1.utils.abstracts import BaseAbstractModel
from v1.utils.enums import OrderStatus


class Order(BaseAbstractModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    address = models.CharField(max_length=300)
    status = models.CharField(max_length=8, choices=OrderStatus.choices(), default=OrderStatus.choices()[0][0])

    def __str__(self) -> str:
        return f'{self.id} - {self.customer.email} - {self.country}'


class OrderItem(BaseAbstractModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey('v1.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self) -> str:
        return f'{self.id} - {self.product.name} - {self.quantity}'
