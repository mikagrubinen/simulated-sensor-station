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

            if street == '':
                cluster_name = nodes.cluster.Cluster(cluster_id)
                shared.cluster_list.append(cluster_name)
            else:
                cluster_name = nodes.cluster.Cluster(cluster_id, street = street)
                shared.cluster_list.append(cluster_name)

def delete_single_cluster(cluster_id):
    cluster_name = 'cluster' + str(cluster_id)
    shared.cluster_list.remove(cluster_name)