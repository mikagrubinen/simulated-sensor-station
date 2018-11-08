
class Node:

    def __init__(self, id = None, state = None, street = None, cluster_id = None, sensor_list = []):
        self.__id = id
        self.__state = state
        self.__street = street
        self.__cluster_id = cluster_id
        self.__sensor_list = sensor_list

    def get_in(self):
        return self.__id
