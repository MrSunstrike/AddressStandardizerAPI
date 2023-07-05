from asgiref.sync import sync_to_async
from dadata import DadataAsync

from address_standardizer.settings import API_KEY_DADATA, SECRET_KEY_DADATA


async def standardization_address(address):
    """
    Стандартизирует указанный адрес, используя API Dadata.

    Аргументы:
        address (str): Адрес для стандартизации.

    Возвращает:
        dict: Результат стандартизации адреса, полученный из API Dadata.
    """
    async with DadataAsync(API_KEY_DADATA, SECRET_KEY_DADATA) as dadata:
        response = await dadata.clean('address', address)
        result = response['result']
        return result


@sync_to_async
def async_save_serializer(serializer):
    """
    Асинхронно сохраняет данные из сериализатора.

    Аргументы:
        serializer: Сериализатор, из которого нужно сохранить данные.
    """
    serializer.save()
