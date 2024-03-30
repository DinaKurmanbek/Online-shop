# urls.py

from django.urls import path
from shop import views



urlpatterns = [
    path('', views.ProductListCreateView.as_view()),
    path('type-choices/', views.choices),

    path('all/', views.ProductCRUDView.as_view()),
    path('all/<int:pk>/', views.ProductCRUDView.as_view()),
    path('<int:pk>/', views.ProductUpdateView.as_view(), name='update'),


    path('<int:pk>/',views.ProductDetailView.as_view(),name = 'detail' ),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete'),


    #path('make_order/', views.make_order, name='make_order'),
    path('make_order/', views.OrderCreateView.as_view(), name='make_order'),


]
