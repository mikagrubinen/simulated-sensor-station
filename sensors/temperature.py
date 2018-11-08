from . import sensor
import random

class Temperature(sensor.Sensor):

    def __init__(self):
        super(Temperature, self).__init__()
        self.__unit = 'degC'
        self.__temperature = None

    def get_temperature(self):
        ret = random.uniform(15, 35)
        return round(ret, 2)

    def get_unit(self):
        return self.__unit