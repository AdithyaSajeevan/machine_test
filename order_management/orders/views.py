from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product, Order
from .serializers import *
from .permissions import *


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class ProductListCreateView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class OrderCreateView(generics.CreateAPIView):

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class OrderListView(generics.ListAPIView):

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        if user.role == 'admin':
            return Order.objects.all()

        return Order.objects.filter(customer=user)


class OrderUpdateView(generics.RetrieveUpdateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
