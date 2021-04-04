from django.urls import path
from rest_api.views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .serializers import *

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('brands/', BrandView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
