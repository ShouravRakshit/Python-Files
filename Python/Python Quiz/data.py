import requests


# This class only for getting data from the api.

class Data:

    def __init__(self):
        # Parameters required for this api.
        self.parameters = {
            "amount": 10,
            "type": "boolean"
        }

    def question_list(self):
        response = requests.get(url="https://opentdb.com/api.php", params=self.parameters)
        response.raise_for_status()
        json_data = response.json()
        return json_data
