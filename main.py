import nodes
import sensors
import do
import shared
from flask import Flask, render_template, request
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template("student.html")

##########################################################################
# @app.route('/')
# def student():
#    return render_template('student.html')
#
# @app.route('/result', methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)
#
# if __name__ == '__main__':
#    app.run(debug = True)
##########################################################################
# Two ways to add cluster. With street name and w/o
# do.add_cluster(1, "second")

# do.add_cluster(100)
##########################################################################
# Delete cluster. Two ways. Based on list or on street name
# Single. Send list with only one cluster id/ multiple, send list with multiple cluster id
# list = [1,2]
# a = do.delete_list_of_clusters(list)
# print(a)

# Multiple. Based on street
# do.delete_clusters_street('first')
######################## Working with nodes #############################
# a = do.add_node(3, 0)
# print(shared.node_list)
# print(a)

# delete nodes based on cluster id
# a = do.delete_nodes_cluster(0)
# print(a)

# Delete list of nodes
list = [45]
a = do.delete_list_of_nodes(list)
print(a)
##########################################################################
# new = sensors.sensor.Sensor()
# print(new.get_all_param())
# new.set_all_param(1, "active", "First St", 11)
# all_param = new.get_all_param()
# print(type(all_param))
# print(all_param['street'])
# print(new.get_state())
##########################################################################
# create temperature class instance
# temp1 = sensors.temperature.Temperature()
# print(temp1.get_temperature())

# set id for temperature instance by using inherited super class methods
# temp1.set_id(3)
# print(temp1.get_id())
##########################################################################
# create light class instance
# ligh = sensors.light.Light()
# print(ligh.get_light())
##########################################################################
# create pressure class instance
# pres = sensors.pressure.Pressure()
# print(pres.get_unit())
##########################################################################
# create instance of a Node class
# node1 = nodes.node.Node()
# my_list = [1,2,3,4]
# node1.set_sensor_list(my_list)
# a = node1.get_all_param()
# print(a['sensor_list'])
##########################################################################
