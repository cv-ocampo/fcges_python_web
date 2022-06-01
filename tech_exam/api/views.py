from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Stock, Order
from .serializers import StockSerializer, OrderSerializer
from django.db.models import Sum

@api_view(['GET'])
def get_stocks(request):
    stocks = Stock.objects.all()
    stocks_serializer = StockSerializer(stocks, many=True)
    return Response(stocks_serializer.data)


@api_view(['POST'])
def add_stock(request):
    stocks_serializer = StockSerializer(data=request.data)
    if stocks_serializer.is_valid():
        stocks_serializer.save()
    return Response(stocks_serializer.data)


@api_view(['POST'])
def place_order(request):
    order_serializer = OrderSerializer(data=request.data)
    if order_serializer.is_valid():
        order_serializer.save()
    return Response(order_serializer.data)


@api_view(['GET'])
def show_orders(request):
    orders = Order.objects.all()
    orders_serializer = OrderSerializer(orders, many=True)
    return Response(orders_serializer.data)


@api_view(['GET'])
def total_invested(request):
    order_list = Order.objects.all()
    total_price = 0
    total_quantity = 0
    for item in order_list:
        total_price = total_price + item.price
        total_quantity = total_quantity + item.quantity
    ret = {'total_price' : total_price, 'total_quantity' : total_quantity}
    return Response(ret)