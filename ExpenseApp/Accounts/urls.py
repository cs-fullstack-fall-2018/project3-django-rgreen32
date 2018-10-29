from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('deposit', views.deposit, name='deposit'),
    path('widthdraw', views.widthdraw, name='widthdraw'),
    path('logout1', views.logout, name='logout')


]
