from . import sensor
import random

class Light(sensor.Sensor):

    def __init__(self):
        super(Light, self).__init__()
        self.__light = None
        self.__unit = 'lux'

    def get_light(self):
        ret = random.uniform(0, 100000)
        return round(ret, 2)

    def get_unit(self):
        return self.__unit