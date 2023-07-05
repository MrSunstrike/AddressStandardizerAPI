from adrf.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from api.serializers import AddressRequestsSerializer
from api.utils import async_save_serializer, standardization_address


@api_view(['POST'])
async def APIAddressView(request):
    """
    Это представление обрабатывает эндпоинт для стандартизации адресов.

    Параметры:
        request (HttpRequest): Объект HTTP-запроса, содержащий данные запроса.

    Возвращает:
        JSON-ответ с запросом пользователя, результатом стандартизации адреса и
        кодом состояния.
        Если запрос является допустимым, возвращается HTTP 200 OK с
        сериализованными данными.
        Если запрос недопустимый, возвращается HTTP 400 BAD REQUEST с ошибками
        сериализации.
    """
    user_request = request.data.get('request')
    result = await standardization_address(user_request)
    data = {'request': user_request, 'result': result}
    serializer = AddressRequestsSerializer(data=data)
    if serializer.is_valid():
        await async_save_serializer(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
