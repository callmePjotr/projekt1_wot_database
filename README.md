# projekt1_wot_database
Here we have a little GUI APP, which is capable of inserting Data into the NoSQL Database Apache Cassandra.
I am working with a docker Container which is the Host of the Cassandra Keyspace.
The App is made for the Insertion of Data, in order to have an overview over the Tanks you own in the strategic tank game World of Tanks (WoT)
In order to try this APP yourself you have to make a pull from my Docker hub

--> docker pull callmepjotr/cassandra
--> if you have docker desktop installed on your machine this command should create the same docker as I have on my Machine
--> in some cases I have experienced an issue, where the needed Keyspace wasn't created, in order to fix this you have to run following commands:


    --> CREATE KEYSPACE wot_database WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;
    --> run following command in cmd :
                                       docker run -it -d --name cassandra-database -p 9042:9042 callmepjotr/cassandra 
                                       (this exposes Port 9042 and creates a new container)
    --> run the new container
    --> execute test.py by using:
                                        python test.py (just drag and drop to desktop)
                           

after setting up your docker it will only run on localhost (Port 9042 or 7199)
in order to change that you'll have to make the following changes to your .yaml file
file should be located here: cd /etc/cassandra/cassandra.yaml

following changes need to be made to this file:
        start_rpc: true
        rpc_address: 0.0.0.0
        broadcast_rpc_address: [node-ip]
        listen_address: [node-ip]
        seed_provider:
            - class_name: ...
            - seeds: "[node-ip]"

