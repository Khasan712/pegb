from django.db import models
from django.contrib.auth.models import AbstractUser
from v1.utils.enums import CustomerCategory
from v1.utils.managers import StaffManager, CustomerManager, UserManager
from uuid import uuid4


class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=100)
    customer_category = models.CharField(max_length=6, choices=CustomerCategory.choices(), blank=True, null=True) 

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self) -> str:
        return f'{self.id} - {self.email}'


class Staff(User):
    objects = StaffManager()

    class Meta:
        proxy = True


class Customer(User):
    objects = CustomerManager()

    class Meta:
        proxy = True

    
class UserEmailVerify(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=300, default=uuid4)

    def __str__(self) -> str:
        return f'{self.customer.id} - {self.code}'