import nodes
import sensors
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

new = sensors.sensor.Sensor()
print(new.get_all_param())

# new.set_all_param(1, "active", "First St", 11)
#
# all_param = new.get_all_param()
#
# print(type(all_param))
#
# print(all_param['street'])
#
# print(new.get_state())

# create temp class instance
new1 = sensors.temperature.Temperature()
print(new1.get_temperature())
# set id for temp instance by using inherited super class methods
new1.set_id(3)
print(new1.get_id())

lig = sensors.light.Light()
print(lig.get_light())

pres = sensors.pressure.Pressure()
print(pres.get_unit())

print("############")
# create instance of a Node class
node1 = nodes.node.Node()
my_list = [1,2,3,4]
#node1.set_sensor_list(my_list)
a = node1.get_all_param()
print(a['sensor_list'])

