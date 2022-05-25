
from rest_framework import serializers

from basket.models import Order
from product.models import Product


class OrderSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    count = serializers.IntegerField()

    def validate(self, attrs):
        data = {}
        try:
            product = Product.objects.get(pk=attrs['product'])
        except Product.DoesNotExists:
            raise serializers.ValidationError('Product not found')
        count = attrs['count']
        data['count'] = count
        data['product'] = product.pk
        return data

    def save(self, **kwargs):
        data = self.validated_data
        user = kwargs['user']
        product = Product.objects.get(pk=data['product'])
        Order.objects.create(
            product=product,
            user=user,
            count=data['count'],
        )

