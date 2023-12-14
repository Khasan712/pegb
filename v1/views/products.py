from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import (
                                GenericViewSet,
                                ModelViewSet)
from v1.models.products import (
                                Cart,
                                Department,
                                Category,
                                Discount,
                                Product)
from v1.serializers.products import (
                                CartSerializer,
                                CreateDepartmentSerializer,
                                CategorySerializer,
                                DiscountSerializer,
                                ProductSerializer)
from v1.utils.permissions import (
                                IsCustomer,
                                IsStaff,
                                IsSuperUser)
from rest_framework.validators import ValidationError


class CartApi(ModelViewSet):
    queryset = Cart.objects.all()
    permission_classes = (IsCustomer,)
    serializer_class = CartSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['customer_id'] = self.request.user.id
        return context
    
    def get_queryset(self):
        return super().get_queryset().filter(customer_id=self.request.user.id)
    

class DiscountApi(ModelViewSet):
    queryset = Discount.objects.all()
    permission_classes = (IsSuperUser,)
    serializer_class = DiscountSerializer


class ProductApi(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = (IsStaff,)
    serializer_class = ProductSerializer

    def get_department(self):
        try:
            return Department.objects.select_related('staff', 'category').get(staff_id=self.request.user.id)
        except Department.DoesNotExist:
            raise ValidationError({
                'status': False,
                'error': "Department not found!!!"
            })

    def get_queryset(self):
        return super().get_queryset().filter(category_id=self.get_department().category.id)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['category_id'] = self.get_department().category.id
        return context


class CategoryApi(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class DepartmentApi(CreateModelMixin, GenericViewSet):
    queryset = Department.objects.all()

    def get_serializer_class(self):
        mehtod = self.request.method
        if mehtod == 'POST':
            return CreateDepartmentSerializer
