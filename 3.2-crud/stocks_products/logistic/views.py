from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

from rest_framework import filters


class MyFilterBackend(DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        if request.query_params.get('product'):
            return {
                "data": {'positions__product__id': request.query_params.get('product')},
                "queryset": queryset,
                "request": request,
            }
        return {
            "data": request.query_params,
            "queryset": queryset,
            "request": request,
        }



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['description', ]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [MyFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['positions__product__id', ]
    search_fields = ['positions__product__title', 'positions__product__description']
