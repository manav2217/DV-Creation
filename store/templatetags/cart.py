from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(pro , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == pro.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(pro , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == pro.id:
            return cart.get(id)
    return False

@register.filter(name='total_price')
def total_price(pro , cart):
    return pro.price * cart_quantity(pro , cart)

@register.filter(name='cart_total_price')
def cart_total_price(pro , cart):
    sum = 0;
    for p in pro:
        sum += total_price(p , cart)
    return sum  