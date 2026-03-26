from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    path('products/', ProductListCreateView.as_view()),

    path('orders/', OrderListView.as_view()),
    path('orders/create/', OrderCreateView.as_view()),
    path('orders/<int:pk>/', OrderUpdateView.as_view()),
]
