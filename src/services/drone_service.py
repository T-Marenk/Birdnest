import requests
import xmltodict
from src.config import DRONE_URL as default_url

class DroneService:
    def __init__(self, url=default_url) -> None:
        self.url = default_url
        self.radius = 100000
        self.center = 250000
        self.drones = None

    def get_drones(self) -> None:
        response = requests.get(self.url).text

        self.drones = xmltodict.parse(response)
        
        self._find_violations()

    def _find_violations(self):
        for drone in self.drones['report']['capture']['drone']:
            position_y = float(drone['positionY'])
            position_x = float(drone['positionX'])
            if self._is_inside_circle(position_x, position_y):
                print(drone)

    def _is_inside_circle(self, position_x, position_y) -> bool:
        return (position_x - self.center)**2 + (position_y - self.center)**2 <= self.radius**2

