import pickle

cluster_database = "cluster_database"
node_database = "node_database"
street_list = "street_list"


b = []

cluster = {'cluster0' : {'id' : None, 'state' : None, 'street' : None, 'node_list' : [], 'sensor_list' : []}}
node = {'node0' : {'id' : None, 'state' : None, 'street' : None, 'cluster_id' : None, 'sensor_list' : []}}



# print (a['c1']['id'])


def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


# save_obj(cluster, cluster_database)
# c = load_obj(cluster_database)
c = load_obj(node_database)
print(c)
# c['c2'] = {'id' : None, "street" : "second St", 'nodes' : b}
# save_obj(c, "my_dict")
# c = load_obj("my_dict")
# d = {}
# d = c['c2']
#
# print(d)
