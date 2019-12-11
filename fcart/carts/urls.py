from django.urls import path
from carts import views
urlpatterns=[
    path('',views.home_view,name='home')
]