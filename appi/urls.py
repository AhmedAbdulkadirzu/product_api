from django.urls import path
from . import views

urlpatterns = [

	path('', views.apioverview, name='apioverview'),
	path('product_list', views.showAll, name='product_list'),
	path('product_detail/<int:pk>/', views.ViewProduct, name='product_detail'),
	path('product_create/', views.CreateProduct, name='CreateProduct'),
	path('product_update/<int:pk>', views.UpdateProduct, name='UpdateProduct'),
	path('product_delete/<int:pk>', views.deleteProduct, name='deleteProduct'),


]
