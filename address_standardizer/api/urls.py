from django.urls import path

from api.views import APIAddressView

urlpatterns = [
    path('v1/address/', APIAddressView),
]
