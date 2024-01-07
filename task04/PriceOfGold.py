import json
import requests


class PriceOfGold:
    def __init__(self, date):
        self.json_file = open('path.json')
        self.json_data = json.load(self.json_file)
        self.date = date

    def gold_price(self):
        if self.date:
            url = f"http://api.nbp.pl/api/cenyzlota/{self.date}/"
        else:
            url = f"{self.json_data['path_api']}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
