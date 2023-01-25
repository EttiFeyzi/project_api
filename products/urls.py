from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetail

urlpatterns = [
    path('new/', ProductCreateView.as_view(), name='create_view'),
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),

]

