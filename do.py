import nodes
import shared

# Adds new clusters to a cluster list. Creates number of Cluster instances with id and street if provided
# @param cluster_list - list of all instances of the Cluster class
# @param number_of_clusters - defines number of new instances to be created
# @param street - street associated with cluster
def add_cluster(number_of_clusters = None, street = ''):
    if number_of_clusters < 1:
        print('Error: Invalid input! Number of clusters must be greater than 0')
    else:
        for x in range(0, number_of_clusters):
            cluster_id = len(shared.cluster_list)
            cluster_name = 'cluster' + str(cluster_id)
            cluster_instance = cluster_name

            if street == '':
                cluster_instance = nodes.cluster.Cluster(cluster_id)
                shared.cluster_list[cluster_name] = cluster_instance
            else:
                cluster_instance = nodes.cluster.Cluster(cluster_id, street = street)
                shared.cluster_list[cluster_name] = cluster_instance
                if street not in shared.street_list:
                    shared.street_list.append(street)


# Delete single cluster from cluster_list based on cluster id
def delete_single_cluster(cluster_id):
    cluster_name = 'cluster' + str(cluster_id)
    del shared.cluster_list[cluster_name]

# Delete all clusters from cluster_list based on street name
def delete_clusters_street(street):
    to_delete_list = []
    for x, y in shared.cluster_list.items():
        if y.get_street() == street:
            to_delete_list.append(x)

    for item in to_delete_list:
        del shared.cluster_list[item]

# Delete all clusters from cluster_list based on id range
def delete_clusters_range(x, y):
    print()