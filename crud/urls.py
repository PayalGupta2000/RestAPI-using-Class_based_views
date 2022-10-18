from django.urls import path
from . import views

urlpatterns = [
    path("",views.ProductAPI.as_view()),
    path("Product/<int:pk>/",views.ProductAPI.as_view()),
    path('categories',views.CategoryAPI.as_view()),
    path('categories/<int:pk>/',views.CategoryAPI.as_view()),
]
