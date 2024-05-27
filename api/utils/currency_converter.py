import requests

class CurrencyConverter:
    def __init__(self):
        self.base_url = 'https://mindicador.cl/api'

    def get_exchange_rate(self, currency_code):
        url = f"{self.base_url}/{currency_code}"
        response = requests.get(url)
        data = response.json()
        return data['serie'][0]['valor']  # Obtener el valor más reciente

    def convert(self, base_currency, target_currency, amount):
        if base_currency == 'CLP':
            base_rate = 1
        else:
            base_rate = self.get_exchange_rate(base_currency)

        target_rate = self.get_exchange_rate(target_currency)
        return (amount / base_rate) * target_rate