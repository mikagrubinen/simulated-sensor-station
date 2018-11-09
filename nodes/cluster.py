
class Cluster:

    def __init__(self, id = None, state = None, street = None, node_list = [], sensor_list = []):
        self.__id = id
        self.__state = state
        self.__street = street
        self.__node_list = node_list
        self.__sensor_list = sensor_list

    def set_id(self, id):
        self.__id = id

    def set_state(self, state):
        self.__state = state

    def set_street(self,street):
        self.__street = street

    def set_cluster_id(self, node_list):
        self.__node_list = node_list

    def set_sensor_list(self, sensor_list):
        self.__sensor_list = sensor_list

    def set_all_param(self, id = None, state = None, street = None, node_list = [], sensor_list = []):
        self.__id = id
        self.__state = state
        self.__street = street
        self.__node_list = node_list
        self.__sensor_list = sensor_list

    def get_id(self):
        return self.__id

    def get_state(self):
        return self.__state

    def get_street(self):
        return self.__street

    def get_node_list(self):
        return self.__node_list

    def get_sensor_list(self):
        return self.__sensor_list

    def get_all_param(self):
        return {'id' : self.__id, 'state' : self.__state,
                'street' : self.__street, 'node_list' : self.__node_list,
                'sensor_list' : self.__sensor_list}