import requests
import xmltodict
from typing import Optional
from math import sqrt
from src.config import DRONE_URL as default_url
from src.services.pilot_service import pilot_service

class DroneService:
    """Class that finds the drones inside the NDZ"""

    def __init__(self, url=default_url, pilot_service=pilot_service) -> None:
        """Function, which initializes the class

        Arguments:
            url: The url for the drone xml
        """

        self.url = default_url
        self.radius = 100000
        self.center = 250000
        self.drones = None
        self.violators = {}
        self.pilot = pilot_service

    def get_drones(self) -> None:
        """Function, which gets the xml from the website and turns it into a dictionary
        """

        response = requests.get(self.url).text

        self.drones = xmltodict.parse(response)
        
        self._find_violations()

    def _find_violations(self):
        """Finds the drones that are in violaton of the NDZ
        """

        for drone in self.drones['report']['capture']['drone']:
            position_y = float(drone['positionY'])
            position_x = float(drone['positionX'])
            distance = self._is_inside_circle(position_x, position_y)
            if distance is not None:
                print(distance)
                serial_number = drone['serialNumber']
                print(serial_number)


    def _is_inside_circle(self, position_x, position_y) -> Optional[float]:
        """Checks if drone is inside the no fly zone

        Arguments:
            position_x: Drones x-position
            position_y: Drones y-position

        Returns:
            distance to the origin, if drone is in violation of the NDZ
        """

        if (position_x - self.center)**2 + (position_y - self.center)**2 <= self.radius**2:
            return sqrt((position_x-self.center)**2 + (position_y - self.center)**2)
