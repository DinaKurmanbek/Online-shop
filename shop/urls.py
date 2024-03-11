from django.urls import path

from shop import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_product, name='create_product'),
    path('detail/<int:product_id>/', views.detail, name='detail'),
    path('make_order/', views.make_order, name='make_order'),  # Add this line
]