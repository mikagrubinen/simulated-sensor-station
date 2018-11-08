from . import sensor
import random

class Humidity(sensor.Sensor):

    def __init__(self):
        super(Humidity, self).__init__()
        self.__unit = '%'
        self.__humidity = None

    def get_humidity(self):
        ret = random.uniform(10, 100)
        return round(ret, 2)

    def get_unit(self):
        return self.__unit