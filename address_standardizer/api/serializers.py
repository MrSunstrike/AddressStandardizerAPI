from rest_framework import serializers
from api.models import AddressStandardization


class AddressRequestsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели AddressStandardization.

    Поля:
        - request: поле запроса.
        - result: поле результата (только для чтения).
    """
    class Meta:
        model = AddressStandardization
        fields = ['request', 'result']
