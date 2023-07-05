from api.views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()
# router_v1.register('address', APIAddressView, basename='address')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
