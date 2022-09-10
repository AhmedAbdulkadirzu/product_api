from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer

from .models import Product

@api_view(['GET']) 
# Create your views here.


def apioverview(request):
	api_urls={
	'List':'/product_list',
	'Detail View':'product_detail/<int:id>',
	'Create':'/product_create/',
	'Update':'/product_update/<int:id>',
	'Delete':'/product_detail/<int:id>'
	}

	return Response(api_urls);

@api_view(['GET'])

def showAll(request):
	products = Product.objects.all()
	serializer = ProductSerializer(products, many=True)
	return Response(serializer.data)

@api_view(['GET'])

def ViewProduct(request, pk):
	products = Product.objects.get(id=pk)
	serializer = ProductSerializer(products, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
	serializer = ProductSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(request, pk):
	product = Product.objects.get(id=pk)
	serializer = ProductSerializer(instance=product, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['GET'])
def deleteProduct(request,pk):
	products = Product.objects.get(id=pk)
	products.delete()
	return Response('item delete success')

