from itertools import product

from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
   path('', index, name='index'),
   path('login/', LoginView.as_view(), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('accounts/profile/', profile, name='profile'),
   path('about/', about, name='about'),
   path('contacts/', contacts, name='contacts'),
   path('product/', product, name='product'),
]
