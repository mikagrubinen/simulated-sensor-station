import nodes
import sensors
import do
import shared
import json
from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = 'random string'

# @app.route("/")
# def hello():
#     return render_template("student.html")

# @app.route('/')
# def student():
#     return render_template('student.html')
##########################################################################
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)

@app.route('/addcluster', methods = ['POST', 'GET'])
def addcluster():
    error = None
    if request.method == 'POST':
        number = int(request.form['number'])
        street = request.form['street']
        if number < 101:
            if do.add_cluster(number, street) == 0:
                flash('Clusters successfully added')
                return redirect(url_for('messages'))
        else:
            error = 'Entered number must be less than or equal to 100'

    return render_template("addcluster.html", error = error)

@app.route('/addnode', methods = ['POST', 'GET'])
def addnode():
    cluster_database = do.load_obj(shared.cluster_database)

    if request.method == 'POST':
        number = int(request.form['number'])
        cluster = request.form['cluster']
        street = request.form['street']
        if do.add_node(number, cluster, street) == 0:
            flash('Nodes successfully added')
            return redirect(url_for('messages'))
        elif do.add_node(number, cluster, street) == "Error: Invalid cluster ID!":
            flash("Error")
            return redirect(url_for('messages'))

    return render_template("addnode.html", cluster_database = cluster_database)

if __name__ == '__main__':
    app.run(debug = True)

######################## Working with clusters ############################
# Two ways to add cluster. With street name and w/o
# do.add_cluster(1, "second")

# do.add_cluster(100)

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
# list = [45]
# a = do.delete_list_of_nodes(list)
# print(a)
######################## Working with sensors ############################
# sensor_list = ['temp', 'pressure', 'light']
# a = do.add_sensors(2, None, sensor_list)
# print(a)

# a = do.delete_sensors( None, 4)
# print(a)

# list = [2,7]
# a = do.delete_list_of_sensors(list)
# print(a)
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
