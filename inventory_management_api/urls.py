from django.urls import path
from . import views

urlpatterns = [
    path('api/brands', views.BrandsList.as_view(), name='brands_list'), 
    path('api/brands/<int:pk>', views.BrandsDetail.as_view(), name='brands_detail'),
]
