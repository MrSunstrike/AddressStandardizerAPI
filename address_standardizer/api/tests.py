from django.test import Client, TestCase


class Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.data = {"request": "мск сухонска 11/-89"}

    def test_successful_request_response(self):
        '''Проверка кода ответа при корректном запросе'''
        response = self.client.post('/api/v1/address/', self.data)

        self.assertEqual(response.status_code, 200,
                         'При корректном запросе код ответа должен быть 200')

    def test_response_data_contains_keys(self):
        '''Проверка структуры ответа API-приложения'''
        response = self.client.post('/api/v1/address/', self.data)

        self.assertIn('request', response.data,
                      'В ответ не передан запрос пользователя')
        self.assertIn('result', response.data,
                      'В ответ не передан результат работы приложения')

    def test_response_data_type_string(self):
        '''Проверка типов передаваемых данных в ответе'''
        response = self.client.post('/api/v1/address/', self.data)

        self.assertIsInstance(response.data['request'], str,
                              'Формат данных ключа "request" не соответствует '
                              'типу "Строка"')
        self.assertIsInstance(response.data['result'], str,
                              'Формат данных ключа "result" не соответствует '
                              'типу "Строка"')

    def test_exceeding_character_limit(self):
        '''Проверка кода ответа при превышении допустимой длины запроса'''
        big_data = {
            "request": "рос федерация сам обл смоленский район ул. пушкина "
            "дом колотушкина квартира 55"
        }
        response = self.client.post('/api/v1/address/', big_data)
        self.assertEqual(response.status_code, 400,
                         'Если запрос превышает 60 символов, код ответа '
                         'должен быть 400')

    def test_get_request_method_not_allowed(self):
        '''Проверка кода ответа при недопустимых методах запросах'''
        # Проверка GET-запроса
        response = self.client.get('/api/v1/address/')
        self.assertEqual(response.status_code, 405,
                         'При GET-запросе, код ответа должен быть 405')

        # Проверка HEAD-запроса
        response = self.client.head('/api/v1/address/')
        self.assertEqual(response.status_code, 405,
                         'При HEAD-запросе, код ответа должен быть 405')

        # Проверка PUT-запроса
        response = self.client.put('/api/v1/address/')
        self.assertEqual(response.status_code, 405,
                         'При PUT-запросе, код ответа должен быть 405')

        # Проверка PATCH-запроса
        response = self.client.patch('/api/v1/address/')
        self.assertEqual(response.status_code, 405,
                         'При PATCH-запросе, код ответа должен быть 405')

        # Проверка DELETE-запроса
        response = self.client.delete('/api/v1/address/')
        self.assertEqual(response.status_code, 405,
                         'При DELETE-запросе, код ответа должен быть 405')
