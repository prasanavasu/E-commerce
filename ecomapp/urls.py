from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.store,name='store'),
    path('store/',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),

    path('update_item/',views.updateItem,name='update_item'),
    path('process_Order/',views.processOrder,name='process_Order'),

]