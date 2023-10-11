from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Usluga
from .cart import Cart
from .forms import CartAddUslugaForm
from django.core.exceptions import PermissionDenied

@require_POST
def cart_add(request, usluga_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("Net dostupa")

    cart = Cart(request)
    usluga = get_object_or_404(Usluga, id=usluga_id)
    form = CartAddUslugaForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(usluga=usluga,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, usluga_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("Net dostupa")

    cart = Cart(request)
    usluga = get_object_or_404(Usluga, id=usluga_id)
    cart.remove(usluga)
    return redirect('cart:cart_detail')

def cart_detail(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("Net dostupa")
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})