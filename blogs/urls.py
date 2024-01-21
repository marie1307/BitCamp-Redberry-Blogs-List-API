
from django.urls import path
from .views import DataAPIView, FilterId, CategoryAPIView, LoginAPIView, CreateAPIView

urlpatterns = [
    path('blogs/', DataAPIView.as_view(), name="blogs"), 
    path('blogs/create/', CreateAPIView.as_view()),
    path('blogs/<int:id>/', FilterId.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),    
]
