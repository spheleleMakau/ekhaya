from django.contrib import admin
from django.urls import path
from ekhaya import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qr-image/', views.generate_qr, name='qr_image'),
    path('', views.home, name='ekhaya_home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
