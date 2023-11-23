import sys
from configs import *


class CassandraAdapter:
    clusters = clusters

    @staticmethod
    def disconnect(function):
        """
        Decorator function for disconnecting communication data
        from service to Cassandra database.
        :param function: Function parameter
        :return: Disconnect database
        """

        def wrapper(self, *args, **kwargs):
            result = function(self, *args, **kwargs)
            self.clusters.shutdown()
            return result

        return wrapper

    @disconnect
    def create_cluster(self, cluster_name, replication_class='SimpleStrategy', replication_factor=1):
        query = "CREATE KEYSPACE %s WITH replication = {'class': '%s', 'replication_factor': %s};" % (cluster_name, replication_class, replication_factor)
        session = self.clusters.connect()
        session.execute(query)
        return True

    @disconnect
    def create_table(self, *args, **kwargs):
        pass

    @disconnect
    def insert(self, *args, **kwargs):
        pass

    @disconnect
    def select(self, *args, **kwargs):
        pass

    @disconnect
    def delete(self, *args, **kwargs):
        pass


# get parameter args from command line
len_args = len(sys.argv)
cluster_name_parameter = True if sys.argv[1] == '--cluster-name' else False
cluster_name_value = sys.argv[2]
replication_class_value = 'SimpleStrategy'
replication_factor_value = 1

if 4 <= len_args <= 5:
    replication_class_parameter = True if sys.argv[3] == '--replication-class' else False
    replication_class_value = sys.argv[4]

if 6 <= len_args <= 7:
    replication_factor_parameter = True if sys.argv[5] == '--replication-factor' else False
    replication_factor_value = int(sys.argv[6])

# validation parameter args from command line
cassandra_adapter = CassandraAdapter()
cassandra_adapter.create_cluster(cluster_name=cluster_name_value,
                                 replication_class=replication_class_value,
                                 replication_factor=replication_factor_value)
