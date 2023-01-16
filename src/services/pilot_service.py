import requests
from src.config import PILOTS_URL as default_url

class PilotService:
    """Class that finds the information about pilots, who violate the NDZ"""

    def __init__(self, url=default_url) -> None:
        self.url = default_url

    def get_pilot_information(self, serial_number) -> dict:
        pilot_url = self.url + serial_number
        response = requests.get(pilot_url).json()
        pilot_information = {'name': response['firstName'] + " " + response['lastName'], 'email': response['email'], 'phoneNumber': response['phoneNumber']}
        return pilot_information

pilot_service = PilotService()
