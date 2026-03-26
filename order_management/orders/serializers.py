from rest_framework import serializers
from .models import User, Product, Order, OrderItem
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            role='customer'
        )
        return user


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_by']


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'items', 'created_at', 'total_amount']
        read_only_fields = ['customer']

    def create(self, validated_data):

        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in items_data:
            product = item['product']
            quantity = item['quantity']

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

        return order

    def get_total_amount(self, obj):
        return obj.total_amount()
