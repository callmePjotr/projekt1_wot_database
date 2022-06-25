from cassandra.cluster import Cluster

clstr=Cluster(['127.0.0.1'], port=9042)
clstr = Cluster()
session = clstr.connect("wot_database")


session.execute("CREATE TABLE full_tank_list_td (nation text, tier int, id timeuuid, name text, PRIMARY KEY(nation,tier)) WITH CLUSTERING ORDER BY (tier ASC);")
session.execute("CREATE TABLE full_tank_list_arty (nation text, tier int, id timeuuid, name text, PRIMARY KEY(nation,tier)) WITH CLUSTERING ORDER BY (tier ASC);")
session.execute("CREATE TABLE full_tank_list_light (nation text, tier int, id timeuuid, name text, PRIMARY KEY(nation,tier)) WITH CLUSTERING ORDER BY (tier ASC);")
session.execute("CREATE TABLE full_tank_list_medium (nation text, tier int, id timeuuid, name text, PRIMARY KEY(nation,tier)) WITH CLUSTERING ORDER BY (tier ASC);")
session.execute("CREATE TABLE full_tank_list_heavy (nation text, tier int, id timeuuid, name text, PRIMARY KEY(nation,tier)) WITH CLUSTERING ORDER BY (tier ASC);")