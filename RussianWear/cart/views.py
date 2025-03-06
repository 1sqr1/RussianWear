from django.shortcuts import render, redirect, \
    get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product, Size
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        size_id = request.POST.get('size')
        size = Size.objects.get(id=size_id) if size_id else None
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'],
                 size=size)
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
