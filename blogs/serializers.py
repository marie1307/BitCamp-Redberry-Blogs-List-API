from rest_framework import serializers
from .models import Data, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'text_color', 'background_color']

class DataSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    class Meta:
        model = Data
        fields = ['id', 'title', 'description', 'image', 'publish_date', 'categories', 'author']

class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()


