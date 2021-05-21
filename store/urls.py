from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import Products_Index
from .views import Cart  , orders
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('',views.index,name="index"),
    path('products/' ,  Products_Index.as_view() , name="products"),
    path('contact/' , views.contact , name="contact"),
    path('about/' , views.about_us , name="about"),
    path('index/' , views.index , name="index"),
    path('register/' , views.register , name="register"),
    path('login/' , views.login , name="login"),
    path('logout/' , views.logout , name="logout"),
    path('email_forgot_password/' , views.email_forgot_password , name="email_forgot_password"),
    path('change_password/' , views.change_password , name="change_password"),
    path('404/' , views.pagenotfound , name="404"),
    path('cart/' , auth_middleware(Cart.as_view()) , name="cart"),
    path('orders/' , auth_middleware(orders.as_view()) , name="orders"),
    path('check-out/' , auth_middleware(views.checkout) , name="checkout"),
    path('productview/<int:id>' , views.productview , name="productview"),
    # path('reset_password/', auth_views.PasswordResetView.as_view() , name="reset_password"),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view() , name="password_reset_confirm"),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view() , name="password_reset_complete"),
]


'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''