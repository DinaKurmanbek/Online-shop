from django.db.migrations import serializer
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from shop.models import Product, SavedItems, Order
from shop.serializers import ProductSerializer, OrderSerializer


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'pk'

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'pk'

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()

    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        # name = serializer.validated_data.get('name')
        # description = serializer.validated_data.get('description', None)
        # if description == "":
        #     description = name

        serializer.save(quantity = 1, description = description)


class ProductCreateView(generics.CreateAPIView):

    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        # name = serializer.validated_data.get('name')
        # description = serializer.validated_data.get('description', None)
        # if description == "":
        #     description = name

        serializer.save(quantity = 1, description = description)

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



@api_view(['GET'])
def choices(request):

    type_choices = dict(Product.TYPE)
    print(type_choices)

    return Response({"choices": type_choices})


class ProductCRUDView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    """
    Retrieve - Чтение одной записи по айди - GET
    List - чтение списка записей - GET
    Create - создание
    Destroy - Удаление
    Update - обновление по айди

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):  # keyword arguments
        print("kwargs: ", kwargs)
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # kwargs['partial'] = True
        #return self.update(request, *args, **kwargs)
        return self.partial_update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()


from rest_framework import generics, mixins
from shop.models import Product
from shop.serializers import ProductSerializer

class ProductUpdateView(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)











class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        saved_items = SavedItems.objects.filter(user=request.user).first()
        if saved_items:
            total_amount = sum(item.product.price * item.quantity for item in saved_items.saveditem_set.all())
            serializer = self.get_serializer(data={'saved_items': saved_items.pk, 'total_amount': total_amount, 'user': request.user.pk})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            saved_items.delete()  # Clear saved items after placing the order
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': 'No items in your cart to place an order!'}, status=status.HTTP_400_BAD_REQUEST)








# @api_view(['GET', 'POST'])
# def index(request):
#
#     if request.method == 'POST':
#         print(request.POST)
#         # print(request.body)
#         instance = ProductSerializer(data = request.POST)
#
#         if instance.is_valid(raise_exception=True):
#             instance.save()
#             # product = instance.save(commit=False)
#             # product.save()
#             return Response(instance.data, status = status.HTTP_201_CREATED)
#         # return  Response({"detail": "Error", "status": status.HTTP_400_BAD_REQUEST})
#
#
#     elif request.method == 'GET':
#         product_id = request.GET.get("product_id")
#         product = Product.objects.get(pk = product_id)
#         data = {}
#         if product:
#             # data = model_to_dict(product)
#             # data = model_to_dict(product, fields = ['name'])
#             instance = ProductSerializer(product)
#         # return HttpResponse("HelloWorld", content_type="application/json")
#             return Response(instance.data)
#
#


# @api_view(['POST'])
# def make_order(request):
#     if request.method == 'POST':
#         saved_items = SavedItems.objects.filter(user=request.user).first()
#         if saved_items:
#             total_amount = sum(item.product.price * item.quantity for item in saved_items.saveditem_set.all())
#             serializer = OrderSerializer(data={'saved_items': saved_items.pk, 'total_amount': total_amount, 'user': request.user.pk})
#             if serializer.is_valid():
#                 serializer.save()
#                 saved_items.delete()  # Clear saved items after placing the order
#                 return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#             return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return JsonResponse({'detail': 'No items in your cart to place an order!'}, status=status.HTTP_400_BAD_REQUEST)


