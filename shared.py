import pickle

cluster_database = "cluster_database"
node_database = "node_database"
sensor_database = "sensor_database"
street_list = "street_list"


b = []

cluster = {'cluster0' : {'id' : 0, 'state' : None, 'street' : None, 'node_list' : [], 'sensor_list' : []}}
node = {'node0' : {'id' : 0, 'state' : None, 'street' : None, 'cluster_id' : None, 'sensor_list' : []}}
sensor = {'sensor0' : {'id' : 0, 'state' : None, 'street' : None, 'cluster_id' : None, 'node_id' : None, 'sensor_type' : None}}


# print (a['c1']['id'])

# cluster_name = 'cluster0'
# if cluster_name is not None and cluster_name in cluster:
#     print("yes")

def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


# save_obj(cluster, cluster_database)
# save_obj(node, node_database)
# save_obj(sensor, sensor_database)

# c1 = load_obj(cluster_database)
# c2 = load_obj(node_database)
# c3 = load_obj(sensor_database)
#
# for v in c1.values():
#     print(v)
#
# print()
#
# for v in c2.values():
#     print(v)
#
# print()
#
# for v in c3.values():
#     print(v)


# c['c2'] = {'id' : None, "street" : "second St", 'nodes' : b}
# save_obj(c, "my_dict")
# c = load_obj("my_dict")
# d = {}
# d = c['c2']
#
# print(d)

