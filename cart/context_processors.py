def cart_processor(request):
    """Add cart info to all templates"""
    if request.user.is_authenticated:
        try:
            cart = request.user.cart
            return {
                'user_cart': cart,
                'cart_items_count': cart.total_items
            }
        except:
            return {'user_cart': None, 'cart_items_count': 0}
    return {'user_cart': None, 'cart_items_count': 0}
