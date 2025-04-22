# diagram.py
from diagrams import Diagram,Cluster,Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import ElasticacheForRedis
from diagrams.aws.compute import LambdaFunction as Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53,DirectConnect
from diagrams.onprem.network import Apache
from diagrams.onprem.queue import Kafka
from diagrams.onprem.database import MongoDB
from diagrams.aws.security import Cognito
from diagrams.onprem.client import Users
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

from diagrams.aws.network import ELB
graph_attr = {
    "splines": "True",
}

with (Diagram("Ohana Platform Overview v2",outformat="jpg", show=False,graph_attr=graph_attr,direction="LR")) as diag:
    customer = Users(
        "US Internet User"
    )

    customer_china = Users(
        "China Internet User"
    )

    with SystemBoundary("US AWS Region") as us:
        dns = Route53("dns")
        lb  =  ELB("lb")
        db  =  RDS("GatesDB")
        gems_db  =  RDS("GemsDB")
        vcsc_db  =  RDS("VcscDB")
        #serverlessNode = Lambda("User NodeJS")
        serverlessApi = Lambda("API NodeJS")
        auth = Cognito("oAuth 2 Service")

        
        kafkaCluster = Kafka("Kafka Cluster")

        processingApi = Lambda("Processing Lambda")

        
        mongoCluster = MongoDB("Mongo Cluster")

        with Cluster("Spring Backend"):
            workerBackend = [EC2("worker1..3")]


        #>>  >> Cluster("Spring Backend") EC2("")  >> RDS("userdb")
        customer >> dns >> lb >>  serverlessApi >> workerBackend 
        serverlessApi >> auth 
        workerBackend >> auth
        workerBackend >> db >> Edge(label="CDC(booking) - debezium" , style="dashed",color="darkred") >> kafkaCluster
        workerBackend >> gems_db >> Edge(label="CDC(container) - debezium" , style="dashed",color="darkred") >> kafkaCluster
        workerBackend >> vcsc_db        
        workerBackend >> ElasticacheForRedis("Redis Cache")
        workerBackend >> Edge(color="darkgreen",label="GET /*Dashboard") >> mongoCluster
        
        kafkaCluster >> processingApi >> mongoCluster
        ##processingApi >> gems_db
        ##processingApi >> db
        ##processingApi >> vcsc_db
        gems_db << Edge(label="FETCH" , style="dashed",color="darkred") << processingApi
        db << Edge(label="FETCH" , style="dashed",color="darkred") << processingApi
        vcsc_db << Edge(label="FETCH" , style="dashed",color="darkred") << processingApi

        #>> workerBackend >> db

    with SystemBoundary("China AWS Region") as china:
        dns_china = Route53("China dns")
        #dns_US = Route53("US dns")
        #serverlessApi = Lambda("API NodeJS")

        with Cluster("China Proxy"):
             workerBackend = [Apache("worker1"), Apache("worker2")]


        #>>  >> Cluster("Spring Backend") EC2("")  >> RDS("userdb")
        #dns >> lb >>  serverlessApi >> workerBackend >> db
        #>> workerBackend >> db    


    customer_china >> dns_china >> workerBackend >>  DirectConnect("Forward all requests to US with Private Tunnel") >> dns
    #workerBackend >> dns
    #china  ->  dns
