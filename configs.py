from cassandra.cluster import Cluster


clusters = Cluster(['localhost'], port=9042)
product_session = clusters.connect('products')