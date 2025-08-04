from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from cart.models import Cart, CartItem


@login_required
def add_to_cart(request, content_type_id, object_id):
    # Get the product
    content_type = get_object_or_404(ContentType, id=content_type_id)
    product = get_object_or_404(content_type.model_class(), id=object_id)

    # Get or create user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Get or create cart item
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=content_type,
        object_id=object_id,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'{product} added to cart!')
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def cart_detail(request):
    try:
        cart = request.user.cart
    except Cart.DoesNotExist:
        cart = None

    return render(request, 'cart/cart-detail.html', {'cart': cart})


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = str(cart_item.product)
    cart_item.delete()

    messages.success(request, f'{product_name} removed from cart!')
    return redirect('cart-detail')


@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart-detail')


@login_required
def clear_cart(request):
    try:
        cart = request.user.cart
        cart.items.all().delete()
        messages.success(request, 'Cart cleared!')
    except Cart.DoesNotExist:
        pass

    return redirect('cart-detail')


@login_required
def checkout(request):
    try:
        cart = request.user.cart
        if not cart.items.exists():
            messages.warning(request, 'Your cart is empty!')
            return redirect('cart-detail')

        # Store order info for success page
        total_items = cart.total_items
        total_price = cart.total_price

        # Clear the cart (simulate purchase)
        cart.items.all().delete()

        # Success message
        messages.success(request,
                         f'🎉 Purchase successful! You bought {total_items} items for €{total_price}. Thank you for your order!')

        return redirect('checkout-success')

    except Cart.DoesNotExist:
        messages.warning(request, 'Your cart is empty!')
        return redirect('cart-detail')


def checkout_success(request):
    return render(request, 'cart/checkout-success.html')
