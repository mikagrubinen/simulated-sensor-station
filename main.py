import nodes
import sensors
from flask import Flask, render_template, request
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template("student.html")


###############################################################
@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
###############################################################

street_list = ['first', 'second']
cluster_list = []


def add_cluster(number_of_clusters = None, street = ''):
    if number_of_clusters < 1:
        print('Error: Invalid input! Number of clusters must be greater than 0')
    else:
        for x in range(0, number_of_clusters):
            cluster_id = len(cluster_list) + 1
            cluster_name = 'cluster' + str(cluster_id)

            if street == '':
                cluster_name = nodes.cluster.Cluster(cluster_id)
                cluster_list.append(cluster_name)
            else:
                cluster_name = nodes.cluster.Cluster(cluster_id, street = street)
                cluster_list.append(cluster_name)


add_cluster(100, "santa clara")
print(cluster_list[0].get_id())
print(cluster_list[0].get_street())


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

