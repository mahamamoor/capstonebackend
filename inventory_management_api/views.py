from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BrandsSerializer
from .models import Brands

class BrandsList(generics.ListCreateAPIView):
    queryset = Brands.objects.all().order_by('id')
    serializer_class = BrandsSerializer

class BrandsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brands.objects.all().order_by('id')
    serializer_class = BrandsSerializer
