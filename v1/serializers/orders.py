from rest_framework import serializers, validators
from v1.models.orders import Order, OrderItem
from django.db import transaction

from v1.models.products import Cart, Discount


class OrderProductsSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.product.id
    
    def get_name(self, obj):
        return obj.product.name
    
    def get_quantity(self, obj):
        return obj.quantity
    
    def get_price(self, obj):
        return obj.price


class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer', 'country', 'address', 'status')
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['customer'] = {
            "id": instance.customer.id,
            "first_name": instance.customer.first_name,
            "email": instance.customer.email,
        }
        res['products'] = OrderProductsSerializer(instance.order_items.all(), many=True).data
        return res


class OrderSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=300)
    carts_id = serializers.ListField(allow_empty=False)

    def create(self, validated_data):
        country = validated_data['country']
        address = validated_data['address']
        carts_id = validated_data['carts_id']
        customer_id = self.context['customer_id']
        customer_category = self.context['customer_category']

        with transaction.atomic():
            try:
                order = Order.objects.create(customer_id=customer_id, country=country, address=address)
                order_items_list = []
                for cart_id in carts_id:
                    cart = Cart.objects.select_related('customer', 'product').get(id=cart_id, customer_id=customer_id)
                    discount = Discount.objects.select_related('category').filter(
                        category_id=cart.product.category.id, customer_category=customer_category
                    ).last()

                    order_item = OrderItem(
                        order=order,
                        product=cart.product,
                        quantity=cart.quantity   
                    )
                    price = cart.product.price
                    if discount:
                        order_item.price = round(price - (price*discount.percentage/100), 2)
                    else:
                        order_item.price = price
                    order_items_list.append(order_item)
                    # cart.delete()
                OrderItem.objects.bulk_create(order_items_list)

            except Cart.DoesNotExist:
                raise validators.ValidationError({
                    "status": False,
                    "error": f"Cart not found!!!"    
                })
        return order
    

    def to_representation(self, instance):
        return OrderGetSerializer(instance).data

