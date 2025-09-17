from django.shortcuts import render, redirect,get_object_or_404

from store.models import Product
from .models import Cart, CartItem

from django.http import HttpResponse

#Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_id = _cart_id(request)

    # Get or create a Cart
    cart, created = Cart.objects.get_or_create(cart_id=cart_id)

    # Get or create a CartItem
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)

    if not created:  # if the CartItem already existed
        cart_item.quantity += 1
        cart_item.save()

    return HttpResponse(cart_item.product)
    exit()
    return redirect('cart')

def cart(request):
    return render(request,'store/cart.html')




