from django.urls import path

from app.views import *

urlpatterns = [
    path('balaji/', balaji, name='balaji')
    ]
