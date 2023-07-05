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
