from itertools import product

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from shop.forms import CreateProductForm
from shop.models import Product, Category, Order


def index(request):  # PostListView
    products = Product.objects.all().order_by('price')
    context = {
        'all_products': products
    }

    return render(request, 'shop/index.html', context)


def detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'shop/details.html', {'product': product})
    except Product.DoesNotExist:
        return HttpResponse("Product does not exist.")


# class CreateProductForm:
#     pass



from django.core.exceptions import ValidationError
from django.http import HttpResponseBadRequest

def new_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)

        if form.is_valid():

            product = form.save(commit=False)
            product.save()

            return redirect("index")
        else:
            return HttpResponse('Error creating!')

        # GET
    context = {
        'form': CreateProductForm()
    }

    return render(request,
                  'shop/create_product.html',
                  context=context)


from django.shortcuts import render, redirect
from shop.forms import OrderForm
from shop.models import Product, SavedItems, Order


def make_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Create a new SavedItems instance for the user
            saved_items = SavedItems.objects.create(user=request.user)

            # Assign products to the saved items (assuming you have a session/cart mechanism)
            # For example, you can retrieve the selected products from the session or any other mechanism you have
            # And then assign them to the saved items

            # Once products are assigned, you can create the order
            order = Order.objects.create(user=request.user, saved_items=saved_items,
                                         total_amount=0)  # Assuming you calculate total_amount elsewhere
            return redirect("index")  # Redirect to index page after successful order creation
    else:
        form = OrderForm()

    context = {
        'form': form
    }
    return render(request, 'shop/make_order.html', context)
