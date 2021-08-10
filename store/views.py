from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from .models import *
import random
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from .middlewares.auth import auth_middleware

# Create your views here.


def index(request):
    return render(request, "index.html")


class Products_Index(View):
    @method_decorator(auth_middleware)
    def post(self, request):
        product_id = request.POST.get('pro_id')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity-1
                else:
                    cart[product_id] = quantity+1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        return redirect('products')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        products = None
        catagory = Catagory.get_all_catagory
        catagory_id = request.GET.get('catagory')
        print(request.GET)
        if catagory_id:
            products = Product.get_product_by_catagory_id(catagory_id)
        else:
            products = Product.get_all_products
            print(products)
        return render(request, "products.html", {'all_pro': products, 'cat': catagory})


def about_us(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST['fn']
        email = request.POST['em']
        subject = request.POST['sub']
        message = request.POST['mes']

        user_message = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        user_message.save()
        messages.success(
            request, "We receive your message , our team reply you as soon as possible")
        return redirect('contact')
    else:
        return render(request, "contact.html")


def register(request):
    if request.method == "POST":
        get_otp = request.POST.get('otp')
        get_user = request.POST.get('useremail')
        if get_otp:
            usr = Customer.objects.get(email=get_user)
            if int(get_otp) == Customer.objects.filter(email=usr).last().otp:
                usr.is_active = True
                usr.is_verified = True
                usr.save()
                messages.success(request, "Account is created")
                return render(request, "authentication/login.html")
            else:
                messages.error(request, "OTP is wrong")
                return render(request, "authentication/register.html", {'otp': True, 'user': usr})

        email = request.POST['em']
        password = request.POST['ps']

        user = Customer.objects.filter(email=email)
        if user:
            messages.info(request, "Email alredy registered")
            return render(request, "authentication/register.html")
        else:
            user_otp = random.randint(100000, 999999)
            user = Customer.objects.create(
                email=email,
                password=password,
                otp=user_otp
            )
            user.save()
        subject = f"Welcome "
        message = f"Hi {user.email} , Your OTP for varificaion is {user_otp} , "
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, "authentication/register.html", {'otp': True, 'user': user})
    else:
        return render(request, "authentication/register.html")


def login(request):
    if request.method == 'POST':
        get_otp = request.POST.get('otp')
        get_user = request.POST.get('useremail')
        print(get_user)
        if get_otp:
            usr = Customer.objects.get(email=get_user)
            if int(get_otp) == Customer.objects.filter(email=usr).last().otp:
                usr.is_active = True
                usr.is_verified = True
                usr.save()
                messages.success(
                    request, 'Your account is successfully verified')
                return render(request, "index.html")
            else:
                messages.error(request, "Otp is wrong")
                return render(request, "authentication/register.html", {'otp': True, 'user': usr})

        email = request.POST['em']
        password = request.POST['ps']
        user = Customer.objects.filter(email=email).first()
        print(user)
        if user:
            if user.is_verified and user.password == password:
                request.session['firstname'] = user.firstname
                request.session['lastname'] = user.lastname
                request.session['email'] = user.email
                request.session['phone'] = user.phone_no
                request.session['id'] = user.id
                return redirect('index')
            elif user.password != password:
                messages.error(
                        request, 'Please enter correct password')
                return render(request, "authentication/login.html")
            elif not user.is_active:
                messages.info(request, "Please varify your account")
                user_otp = random.randint(100000, 999999)
                user.otp = user_otp
                user.save()
                subject = f"Welcome to DV creation"
                message = f"Hi {user.email} , Your OTP for varificaion is {user_otp} , (Note: OTP is only for 5 min)"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(subject, message, email_from, recipient_list)
                return render(request, "authentication/register.html", {'otp': True, 'user': user})
        else:
            messages.error(
                request, "Email not found ,Please register first")
            return render(request, "authentication/register.html")
    else:
        return render(request, "authentication/login.html")


def logout(request):
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    del request.session['phone']
    del request.session['id']
    cart = request.session.get('cart')
    if cart:
        del request.session['cart']
    return redirect('index')


def email_forgot_password(request):
    if request.method == "POST":
        get_otp = request.POST.get('otp')
        user_email = request.POST.get('useremail')

        if get_otp:
            get_user = Customer.objects.get(email=user_email)
            if int(get_otp) == Customer.objects.filter(email=get_user).last().otp:
                return render(request, "authentication/password_change.html", {'user': get_user})
            else:
                return render(request, "authentication/email_forgot_password.html", {'otp': True, 'user': get_user})

        email = request.POST['em']
        user = Customer.objects.get(email=email)
        if user:
            user_otp = random.randint(100000, 999999)
            user.otp = user_otp
            user.save()
            return render(request, "authentication/email_forgot_password.html", {'otp': True, 'user': user})
        else:
            return HttpResponse("ok")
    else:
        return render(request, "authentication/email_forgot_password.html",)


def change_password(request):
    if request.method == "POST":
        password = request.POST['ps']
        c_password = request.POST['cps']
        user_email = request.POST.get('useremail')
        print(user_email)

        user = Customer.objects.get(email=user_email)
        if user:
            if password == c_password:
                user.password = password
                user.save()
                return render(request, "authentication/login.html", {'user': user})
            else:
                return HttpResponse("oops")
        else:
            return render(request, "authentication/password_change.html", {'user': user})
    else:
        return render(request, "authentication/password_change.html")


def pagenotfound(request):
    return render(request, "404.html")


class Cart(View):
    def post(self, request):
        cart = request.session.get('cart')
        product_id = request.POST.get('pro_id')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity-1
                else:
                    cart[product_id] = quantity+1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        return redirect('cart')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        return render(request, "cart.html", {'products': products})


class orders(View):
    def post(self, request):
        c_order = request.POST.get('order_id')
        db_order = Order.get_orders(c_order)
        delete = request.POST.get('delete')
        if delete:
            db_order.delete()
        return redirect('orders')

    @method_decorator(auth_middleware)
    def get(self, request):
        user = request.session.get('id')
        get_order = Order.get_order_by_id(user)
        return render(request, "orders.html", {'ord': get_order})


def checkout(request):
    if request.method == "POST":
        address = request.POST['add']
        customer_id = request.session.get('id')
        country = request.POST['con']
        firstname = request.POST['fn']
        lastname = request.POST['ln']
        city = request.POST['ct']
        street = request.POST['st']
        state = request.POST['sta']
        zipcode = request.POST['zip']
        email = request.POST['em']
        phone = request.POST['pn']
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        for product in products:
            order = Order(user_id=Customer(id=customer_id),
                          product=product,
                          quantity=cart.get(str(product.id)),
                          price=product.price,
                          address=address,
                          phone=phone,
                          country=country,
                          firstname=firstname,
                          lastname=lastname,
                          city=city,
                          street=street,
                          state=state,
                          pincode=zipcode,
                          customer_email=email,
                          
                          )
            order.save()
            request.session['cart'] = {}
        return redirect('orders')
    else:
        try:
            ids = list(request.session.get('cart').keys())
            if ids:
                products = Product.get_product_by_id(ids)
                return render(request, "checkout.html", {'products': products})
            else:
                return render(request, "404.html")
        except:
            return render(request, "404.html")


def productview(request, id):
    product = Product.objects.filter(id=id)
    print(product)
    return render(request, "productview.html", {'product': product[0]})
