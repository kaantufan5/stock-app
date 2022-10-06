from django.contrib import admin
from .models import (
    Category,
    Brand,
    Product,
    Stock,
    Firm
)
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Firm)