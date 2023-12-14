from django.urls import path
from v1.views.users import CustomerRegisterApi, StaffApi
from v1.views.renders import user_verify_page
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter
from v1.views.products import CategoryApi, DepartmentApi, ProductApi, DiscountApi, CartApi
from v1.views.orders import OrderApi


router = DefaultRouter()
router.register('category', CategoryApi)
router.register('department', DepartmentApi)
router.register('product', ProductApi)
router.register('discount', DiscountApi)
router.register('cart', CartApi)
router.register('order', OrderApi)


urlpatterns = [
    # User
    path('customer/register/', CustomerRegisterApi.as_view()),
    path('user/login/', TokenObtainPairView.as_view()),
    path('staff/register/', StaffApi.as_view()),
    
    # Verify page
    path('user-verify/', user_verify_page)
]+router.urls
