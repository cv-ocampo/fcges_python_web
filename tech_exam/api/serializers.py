from rest_framework import serializers
from base.models import Stock, Order

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        
        
        
class OrderSerializer(serializers.ModelSerializer):
    price = serializers.CharField(required=False,allow_blank=True)
    class Meta:
        model = Order
        fields = '__all__'