from api.views import APIAddressView
from django.urls import path

urlpatterns = [
    path('v1/address/', APIAddressView),
]
