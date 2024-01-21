from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from .serializers import DataSerializer, CategorySerializer, LoginSerializer, CreateBlogSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Data, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

class DataAPIView(generics.ListAPIView): # ბლოგების ფუნქციონალი, რომელიც აბრუნებს სრული ბლოგების სიას
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    filter_backends = [DjangoFilterBackend] # ფილტრავს კატეგორიების მიხედვით
    filterset_fields = ['categories']
    
class CreateAPIView(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = CreateBlogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs): # ახალი ბლოგის დამატების ფუნქციონალი
        return super().post(request, *args, **kwargs)

     
class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FilterId(generics.ListAPIView): # ფილტრაცია ID-ით
    serializer_class = DataSerializer

    def get_queryset(self): 
        id = self.kwargs["id"]
        queryset = Data.objects.filter(id=id)
        return queryset
    
class LoginAPIView(APIView): #დალოგინების ფუნქციონალი / აბრუნებს ტოკენს ან წერს რომ email არ არის ვალიდური
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            except User.DoesNotExist:
                return Response({'error': "The selected email is invalid."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

