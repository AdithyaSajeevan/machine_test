from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [

    path('register/', RegisterView.as_view()),

    path('login/', TokenObtainPairView.as_view()),

    path('products/', ProductListCreateView.as_view()),

    path('orders/', OrderCreateView.as_view()),
    path('orders/list/', OrderListView.as_view()),

    path('orders/<int:pk>/', OrderUpdateView.as_view()),

]
