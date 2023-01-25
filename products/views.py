from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializers
from django.contrib.auth import get_user_model
User = get_user_model()



class ProductCreateView(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers
    permission_classes = (IsAuthenticated,)
  
  
   
   
class ProductListView(ListCreateAPIView):
    queryset = Product.objects.order_by('-publish')
    serializer_class = ProductSerializers
    


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


