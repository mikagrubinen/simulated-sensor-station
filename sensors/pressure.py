from . import sensor
import random

class Pressure(sensor.Sensor):

    def __init__(self):
        super(Pressure, self).__init__()
        self.__pressure = None
        self.__unit = 'mbar'

    def get_pressure(self):
        ret = random.uniform(950, 1015)
        return round(ret, 2)

    def get_unit(self):
        return self.__unit
