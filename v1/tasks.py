from django.core.mail import EmailMessage
from celery import shared_task
from v1.models.users import UserEmailVerify


@shared_task()
def email_verify_task(email: str, first_name: str, customer_id: int):
    code = UserEmailVerify.objects.create(customer_id=customer_id).code
    link = f'http://127.0.0.1:8000/user-verify/?code={code}&email={email}'
    message = f"Hi {first_name}, please verify your email, by pressing this link {link}"
    subject = "Verify email"
    email = EmailMessage(
        body=message,
        subject=subject,
        to=[email],
    )
    email.send()