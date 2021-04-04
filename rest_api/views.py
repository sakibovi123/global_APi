from django.http import response
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ProductView(APIView):

    def get(self, request):
        products = Product.objects.all()
        data = []

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class CategoryView(APIView):

    def get(self, request):
        cats = Category.objects.all()
        data = []

        serializer = CategorySerializer(cats, many=True)

        return Response(serializer.data)


class BrandView(APIView):
    def get(self, request):
        brands = Brand.objects.all()

        data = []

        serializer = BrandSerializer(brands, many=True)

        return Response(serializer.data)

class CampaignsView(APIView):

    def get(self, request):
        camps = Campaigns.objects.all()

        data = []

        serializer = CampaignSerializer(camps, many=True)

        return Response(serializer.data)