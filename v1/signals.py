from django.db.models.signals import post_save
from django.dispatch import receiver
from v1.models.orders import Order
from v1.models.users import User
from v1.tasks import email_verify_task


@receiver(post_save, sender=User)
def user_signal(sender, instance, created, **kwargs):
    if created and instance.is_staff == False:
        email_verify_task.delay(
            instance.email, instance.first_name, instance.id
            )
        

@receiver(post_save, sender=Order)
def order_signal(sender, instance, created, **kwargs):
    if created:
        order_qty = Order.objects.filter(customer_id=instance.customer.id).count()
        customer = instance.customer
        if order_qty > 49 and customer.customer_category != 'gold':
            customer.customer_category = 'gold'
            customer.save()
        elif order_qty > 20 and customer.customer_category != 'silver':
            customer.customer_category = 'silver'
            customer.save()
