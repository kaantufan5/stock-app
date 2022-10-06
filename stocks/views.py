from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissions
from .models import Stock

from .models import (
    Category,
    Brand,
    Product,
    Firm,
    Stock
)
from .serializers import (
    CategorySerializer,
    BrandSerializers,
    ProductSerializers,
    FirmSerializers,
    StockSerializers
)

class CategoryView(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    

class BrandView(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    

class ProductView(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'category', 'brand']
    search_fields = ['name', 'category', 'brand']
   

class FirmView(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Firm.objects.all()
    serializer_class = FirmSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    

class StockView(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Stock.objects.all()
    serializer_class = StockSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user', 'firm', 'product']

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


    




    