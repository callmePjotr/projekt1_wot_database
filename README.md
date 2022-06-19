# projekt1_wot_database
Here we have a little GUI APP, which is capable of inserting Data into the NoSQL Database Apache Cassandra.
I am working with a docker Container which is the Host of the Cassandra Keyspace.
The App is made for the Insertion of Data, in order to have an overview over the Tanks you own in the strategic tank game World of Tanks (WoT)
In order to try this APP yourself you have to make a pull from my Docker hub

--> docker pull callmepjotr/cassandra
--> if you have docker desktop installed on your machine this command should create the same docker as I have on my Machine
--> in some cases I have experienced an issue, where the needed Keyspace wasnt created, in order to fix this you have to run following commands:

    --> CREATE KEYSPACE wot_database WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;
    --> CREATE TABLE wot_database.full_tank_list_heavy (nation text, tier int, id timeuuid, name text, PRIMARY KEY (nation, tier) WITH CLUSTERING ORDER BY (tier ASC)
    --> CREATE TABLE wot_database.full_tank_list_medium (nation text, tier int, id timeuuid, name text, PRIMARY KEY (nation, tier) WITH CLUSTERING ORDER BY (tier ASC)
    --> CREATE TABLE wot_database.full_tank_list_light (nation text, tier int, id timeuuid, name text, PRIMARY KEY (nation, tier) WITH CLUSTERING ORDER BY (tier ASC)
    --> CREATE TABLE wot_database.full_tank_list_td (nation text, tier int, id timeuuid, name text, PRIMARY KEY (nation, tier) WITH CLUSTERING ORDER BY (tier ASC)
    --> CREATE TABLE wot_database.full_tank_list_arty (nation text, tier int, id timeuuid, name text, PRIMARY KEY (nation, tier) WITH CLUSTERING ORDER BY (tier ASC)
