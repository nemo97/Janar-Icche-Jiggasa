# diagram.py
from diagrams import Diagram,Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import ElasticacheForRedis
from diagrams.aws.compute import LambdaFunction as Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53,DirectConnect
from diagrams.onprem.network import Apache
from diagrams.aws.security import Cognito
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

from diagrams.aws.network import ELB
graph_attr = {
    "splines": "spline",
}

with (Diagram("Ohana Platform Overview",outformat="jpg", show=False,graph_attr=graph_attr,direction="LR")) as diag:
    customer = Person(
        name="US Internet User", description="User in the US"
    )

    customer_china = Person(
        name="China Internet User", description="User in the China"
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


        with Cluster("Spring Backend"):
            workerBackend = [EC2("worker1"), EC2("worker2")]


        #>>  >> Cluster("Spring Backend") EC2("")  >> RDS("userdb")
        customer >> dns >> lb >>  serverlessApi >> workerBackend
        serverlessApi >> auth 
        workerBackend >> auth
        workerBackend >> db
        workerBackend >> gems_db
        workerBackend >> vcsc_db        
        workerBackend >> ElasticacheForRedis("Redis Cache")
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
