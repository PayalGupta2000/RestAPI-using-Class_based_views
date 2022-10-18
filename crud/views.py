from django.shortcuts import render
import pkg_resources
from .serializers import *
from .models import *
from django.views.decorators.csrf  import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class ProductAPI(APIView):
    def get(self,request,pk=None):
        id=pk
        if id is not None:
            pro=Product.objects.get(id=id)
            serializer=ProductSerializer(pro)
            return Response(serializer.data)

        pro=Product.objects.all()
        serializer=ProductSerializer(pro,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Your data added successfully.",status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        id=pk
        pro=Product.objects.get(pk=id)
        serializer=ProductSerializer(pro,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        id=pk
        pro=Product.onjects.get(pk=id)
        serializer=ProductSerializer(pro,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Partial data updated ")
        return Response(serializer.errors)
    def delete(self,request,pk):
        id=pk
        pro=Product.objects.get(pk=id)
        pro.delete()
        return Response("data deleted")

    
class CategoryAPI(ProductAPI,APIView):
    def get(self,request,pk=None):
        id=pk
        if id is not None:
            pro=Product.objects.filter(id=id)
            CategorySerializer=ProductSerializer(pro,many=True)
            return Response(CategorySerializer.data)

        cat=Category.objects.all()
        serializer=CategorySerializer(cat,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg="category successfully added."
            return Response(msg,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        id=pk
        cat=Category.objects.get(pk=id)
        serializer=CategorySerializer(cat,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        id=pk
        cat=Category.objects.get(pk=id)
        serializer=CategorySerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg="Category Partial Updated."
            return Response(msg)
        return Response(serializer.errors)

    def delete(self,request,pk):
        id=pk
        cat=Category.objects.get(pk=id)
        cat.delete()
        return Response("Category Deleted.")