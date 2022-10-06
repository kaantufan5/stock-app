from django.urls import path, include
from rest_framework import routers
from .views import (
    StockView,
    BrandView,
    FirmView,
    CategoryView,
    ProductView
)

router = routers.DefaultRouter()

router.register("stocks", StockView)
router.register("brands", BrandView)
router.register("firms", FirmView)
router.register("categories", CategoryView)
router.register("products", ProductView)

urlpatterns = [ 
    
] 

urlpatterns += router.urls
