from django.urls import path
from ecommerceapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('handlerequest/', views.handlerequest, name='handlerequest'),
    path('profile/', views.profile, name='profile'),
]
