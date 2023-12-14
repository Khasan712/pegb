from rest_framework import serializers
from v1.models.products import Cart, Department, Category, Discount, Product


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'product', 'quantity')
    
        extra_kwargs = {
            "customer": {'write_only': True}   
        }
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['product'] = {
            "id": instance.product.id,
            "name": instance.product.name,
            "price": instance.product.price    
        }
        return res
    
    def create(self, validated_data):
        cart, _ = Cart.objects.get_or_create(product=validated_data['product'], customer_id=self.context['customer_id'])
        cart.quantity += validated_data['quantity']
        cart.save()
        return cart


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'category', 'customer_category', 'percentage')
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['category'] = {
            "id": instance.category.id,    
            "name": instance.category.name
        }
        return res


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['category'] = {
            "id": instance.category.id,    
            "name": instance.category.name    
        }
        return res

    def create(self, validated_data):
        validated_data.setdefault('category_id', self.context['category_id'])
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CreateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('staff', 'category', 'name')
