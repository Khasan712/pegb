from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from v1.models.orders import Order
from v1.serializers.orders import OrderGetSerializer, OrderSerializer
from v1.utils.permissions import IsCustomer


class OrderApi(CreateModelMixin,
               ListModelMixin,
               RetrieveModelMixin,
               GenericViewSet):
    queryset = Order.objects.all()
    permission_classes = (IsCustomer,)

    def get_queryset(self):
        return super().get_queryset().select_related('customer').filter(customer_id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderSerializer
        else:
            return OrderGetSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['customer_id'] = self.request.user.id
        context['customer_category'] = self.request.user.customer_category
        return context
