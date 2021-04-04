from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Campaigns)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartproduct)
admin.site.register(Order)