import nodes
import shared
import pickle

###################################### Working with Clusters #######################################

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
        return 0


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


###################################### Working with Nodes #######################################

# Add new nodes to node database. Cluster id should be mandatory
def add_node(number_of_nodes = None, cluster_name = None, street = None,):

    if number_of_nodes < 1:
        return "Error: Invalid input! Number of nodes must be greater than 0!"
    else:
        cluster_database = load_obj(shared.cluster_database)
        # cluster_name = 'cluster' + str(cluster_id)

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
            return 0
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

###################################### Working with Sensors #######################################

# Add sensors to a cluster or to a node.
# @param list - list of types of sensors to be added (eg. ['temp', 'pressure'])
def add_sensors(cluster_id = None, node_id = None, list = []):

    if cluster_id is None and node_id is None:
        return "Error: Invalid input!"

    elif cluster_id is not None and node_id is not None:
        return "Error: Invalid input!"

    elif cluster_id is not None and node_id is None:

        cluster_database = load_obj(shared.cluster_database)
        cluster_name = 'cluster' + str(cluster_id)

        if cluster_name in cluster_database:

            if not list:
                return "Error: List of sensors is empty!"
            else:
                sensor_database = load_obj(shared.sensor_database)
                sensor_to_list = []

                for item in list:
                    sensor_id = len(sensor_database)
                    sensor_name = 'sensor' + str(sensor_id)
                    sensor_database[sensor_name] = {'id' : sensor_id, 'state' : None, 'street' : None, 'cluster_id' : cluster_name, 'node_id' : node_id, 'sensor_type' : item}
                    sensor_to_list.append(sensor_name)

                cluster_database[cluster_name]["sensor_list"] = cluster_database[cluster_name]["sensor_list"] + sensor_to_list
                save_obj(sensor_database, shared.sensor_database)
                save_obj(cluster_database, shared.cluster_database)
        else:
            return "Error: Invalid cluster ID!"

    elif cluster_id is None and node_id is not None:

        node_database = load_obj(shared.node_database)
        node_name = 'node' + str(node_id)

        if node_name in node_database:

            if not list:
                return "Error: List of sensors is empty!"
            else:
                sensor_database = load_obj(shared.sensor_database)
                sensor_to_list = []

                for item in list:
                    sensor_id = len(sensor_database)
                    sensor_name = 'sensor' + str(sensor_id)
                    sensor_database[sensor_name] = {'id' : sensor_id, 'state' : None, 'street' : None, 'cluster_id' : cluster_id, 'node_id' : node_name, 'sensor_type' : item}
                    sensor_to_list.append(sensor_name)

                node_database[node_name]["sensor_list"] = node_database[node_name]["sensor_list"] + sensor_to_list
                save_obj(sensor_database, shared.sensor_database)
                save_obj(node_database, shared.node_database)
        else:
            return "Error: Invalid node ID!"

# Delete all sensors connected to cluster or a node
def delete_sensors(cluster_id = None, node_id = None):

    if cluster_id is None and node_id is None:
        return "Error: Invalid input!"

    elif cluster_id is not None and node_id is not None:
        return "Error: Invalid input!"

    elif cluster_id is not None and node_id is None:

        cluster_database = load_obj(shared.cluster_database)
        cluster_name = 'cluster' + str(cluster_id)

        if cluster_name in cluster_database:
            sensors_to_delete = cluster_database[cluster_name]['sensor_list']

            if not sensors_to_delete:
                return "This cluster has no sensors connected to it!"
            else:
                delete_sensors_helper(sensors_to_delete)
                cluster_database[cluster_name]["sensor_list"] = []
                save_obj(cluster_database, shared.cluster_database)
        else:
            return "Error: Invalid cluster ID!"

    elif cluster_id is None and node_id is not None:

        node_database = load_obj(shared.node_database)
        node_name = 'node' + str(node_id)

        if node_name in node_database:
            sensors_to_delete = node_database[node_name]['sensor_list']

            if not sensors_to_delete:
                return "This node has no sensors connected to it!"
            else:
                delete_sensors_helper(sensors_to_delete)
                node_database[node_name]["sensor_list"] = []
                save_obj(node_database, shared.node_database)
        else:
            return "Error: Invalid node ID!"

# Delete sensors all from in a list
def delete_list_of_sensors(list = []):

    if not list:
        return "Error: List of sensors can't be empty!"
    else:
        return_list = []
        sensor_database = load_obj(shared.sensor_database)
        node_database = load_obj(shared.node_database)
        cluster_database = load_obj(shared.cluster_database)

        for item in list:
            sensor_name = 'sensor' + str(item)

            if sensor_name in sensor_database:

                cluster_name = sensor_database[sensor_name]['cluster_id']
                node_name = sensor_database[sensor_name]['node_id']

                if cluster_name is not None and cluster_name in cluster_database:
                    cluster_database[cluster_name]['sensor_list'].remove(sensor_name)
                if node_name is not None and node_name in node_database:
                    node_database[node_name]['sensor_list'].remove(sensor_name)

                del sensor_database[sensor_name]
            else:
                return_list.append(sensor_name)

        save_obj(sensor_database, shared.sensor_database)
        save_obj(node_database, shared.node_database)
        save_obj(cluster_database, shared.cluster_database)

        if not return_list:
            return "Sensors deleted"
        else:
            return "Sensors " + str(return_list) + " not deleted. Not in a system."

# Helper function to delete sensors
# @param sensors_to_delete - list of sensors to be deleted
def delete_sensors_helper(sensors_to_delete):

    sensor_database = load_obj(shared.sensor_database)

    for item in sensors_to_delete:
        del sensor_database[item]

    save_obj(sensor_database, shared.sensor_database)

###################################### Working with Pickle #######################################

def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)