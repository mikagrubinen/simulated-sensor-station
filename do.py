import nodes
import shared
import pickle

############################## Working with Clusters ###############################

# Adds new clusters to a cluster_database. Creates number of Clusters to be added
# @param number_of_clusters - defines number of new clusters to be added
# @param street - street associated with cluster
def add_cluster(number_of_clusters = None, street = None):

    if number_of_clusters < 1:
        return "Error: Invalid input! Number of clusters must be greater than 0"
    else:
        cluster_database = load_obj(shared.cluster_database)
        street_list = load_obj(shared.street_list)

        for x in range(0, number_of_clusters):
            cluster_id = len(cluster_database)
            cluster_name = 'cluster' + str(cluster_id)
            cluster_database[cluster_name] = {'id' : cluster_id, 'state' : None, 'street' : street, 'node_list' : [], 'sensor_list' : []}

        if street not in street_list:
            street_list.append(street)

        save_obj(cluster_database, shared.cluster_database)
        save_obj(street_list, shared.street_list)


# Delete all clusters from cluster_database based on street name
def delete_clusters_street(street):

    cluster_database = load_obj(shared.cluster_database)
    street_list = load_obj(shared.street_list)

    if street not in street_list:
        return "no street"
    else:
        to_delete_list = []

        for x, y in cluster_database.items():
            if y['street'] == street:
                to_delete_list.append(x)

        for item in to_delete_list:
            del cluster_database[item]

        save_obj(cluster_database, shared.cluster_database)

# Delete all clusters from cluster_database based on id from a list received
def delete_list_of_clusters(list):

    return_list = []
    cluster_database = load_obj(shared.cluster_database)

    for item in list:
        cluster_name = 'cluster' + str(item)
        if cluster_name in cluster_database:
            del cluster_database[cluster_name]
        else:
            return_list.append(cluster_name)

    save_obj(cluster_database, shared.cluster_database)

    if not return_list:
        return "Clusters deleted"
    else:
        return "Clusters " + str(return_list) + " not deleted. Not in a system."


############################## Working with Nodes ###############################

# Add new nodes to node database.
def add_node(number_of_nodes = None, cluster_id = None, street = None,):

    if number_of_nodes < 1:
        return "Error: Invalid input! Number of nodes must be greater than 0!"
    else:
        cluster_database = load_obj(shared.cluster_database)
        cluster_name = 'cluster' + str(cluster_id)

        if cluster_name in cluster_database:

            node_database = load_obj(shared.node_database)
            node_to_cluster_list =[]

            for x in range(0, number_of_nodes):
                node_id = len(node_database)
                node_name = 'node' + str(node_id)
                node_database[node_name] = {'id' : node_id, 'state' : None, 'street' : street, 'cluster_id' : cluster_name, 'sensor_list' : []}
                node_to_cluster_list.append(node_name)


            cluster_database[cluster_name]["node_list"] = cluster_database[cluster_name]["node_list"] + node_to_cluster_list
            save_obj(node_database, shared.node_database)
            save_obj(cluster_database, shared.cluster_database)
        else:
            return "Error: Invalid cluster ID!"

# Delete all nodes connected to a cluster
def delete_nodes_cluster(cluster_id):

    cluster_database = load_obj(shared.cluster_database)
    cluster_name = 'cluster' + str(cluster_id)

    if cluster_name in cluster_database:
        nodes_to_delete = cluster_database[cluster_name]["node_list"]

        if not nodes_to_delete:
            return "This cluster has no nodes connected to it!"
        else:
            node_database = load_obj(shared.node_database)

            for item in nodes_to_delete:
                del node_database[item]

            cluster_database[cluster_name]["node_list"] = []
            save_obj(node_database, shared.node_database)
            save_obj(cluster_database, shared.cluster_database)
    else:
        return "Error: Invalid cluster ID!"

# Delete list of nodes
def delete_list_of_nodes(list):

    return_list = []
    node_database = load_obj(shared.node_database)
    cluster_database = load_obj(shared.cluster_database)

    for item in list:
        node_name = 'node' + str(item)

        if node_name in node_database:
            cluster_name = node_database[node_name]['cluster_id']
            cluster_database[cluster_name]['node_list'].remove(node_name)
            del node_database[node_name]
        else:
            return_list.append(node_name)

    save_obj(node_database, shared.node_database)
    save_obj(cluster_database, shared.cluster_database)

    if not return_list:
        return "Nodes deleted"
    else:
        return "Nodes " + str(return_list) + " not deleted. Not in a system."

############################## Working with Pickle ###############################

def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)