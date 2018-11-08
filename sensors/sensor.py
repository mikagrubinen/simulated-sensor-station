
class Sensor:

    def __init__(self, id = None, state = None, street = None, node_id = None):
        self.__id = id
        self.__state = state
        self.__street = street
        self.__node_id = node_id

    def set_id(self, id):
        self.__id = id

    def set_state(self, state):
        self.__state = state

    def set_street(self,street):
        self.__street = street

    def set_node_id(self, node_id):
        self.__node_id = node_id

    def set_all_param(self, id, state, street, node_id):
        self.__id = id
        self.__state = state
        self.__street = street
        self.__node_id = node_id

    def get_id(self):
        return self.__id

    def get_state(self):
        return self.__state

    def get_street(self):
        return self.__street

    def get_node_id(self):
        return self.__node_id

    def get_all_param(self):
        return {'id' : self.__id, 'state' : self.__state, 'street' : self.__street, "node_id" : self.__node_id}
