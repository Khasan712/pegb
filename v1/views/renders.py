from django.http import HttpResponse

from v1.models.users import User, UserEmailVerify


def user_verify_page(request, *args, **kwargs):
    data = request.GET
    code = data.get('code')
    email = data.get('email')
    if code and email:
        customer = User.objects.filter(email=email).first()
        if not customer:
            return HttpResponse("Email not found!!!")
        code_obj = UserEmailVerify.objects.select_related('customer').filter(code=code, customer_id=customer.id).first()
        if not code_obj:
            return HttpResponse("Please contact with administrator or reattempt!!!")
        code_obj.delete()
        customer.is_email_verified = True
        customer.save()
        return HttpResponse("Email verified successfully!!!")
    return HttpResponse("Error")
