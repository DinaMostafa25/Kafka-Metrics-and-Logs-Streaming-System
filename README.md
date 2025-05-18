# *Kafka Metrics and Logs Streamer*

## **Project Overview**
Kafka Metrics and Logs Streamer is a real-time data streaming system designed to collect, publish, and process infrastructure metrics and load balancer logs using Apache Kafka. The project simulates a distributed environment where multiple servers continuously send resource consumption metrics (CPU, memory, disk) and load balancers send logs.<br>

## **Project Objectives**
This project aims to build a hands-on system that shows how infrastructure metrics and logs can be streamed, processed, and stored in real time. It's designed to simulate a real-world scenario where multiple servers and a load balancer are constantly generating data.<br>

&nbsp;&nbsp;&nbsp;&nbsp;The key objectives are:<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- To create a reliable Kafka-based pipeline for streaming server metrics and load balancer logs.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- To store resource metrics (CPU, memory, disk) in a PostgreSQL database for monitoring and further analysis.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- To set the foundation for a Spark Streaming system that can analyze and aggregate logs in real-time, storing the 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    results in Hadoop.<br>

## **Tech stack**
***Apache Kafka*** - Message broker for real-time data pipelines<br>
***Zookeeper*** - Kafka dependency for broker coordination<br>
***Java*** - Server and load balancer producers<br>
***Python*** - Kafka consumer for metrics processing<br>
***PostgreSQL*** - Relational database for metrics persistence<br>
***Docker & Docker Compose*** - Environment containerization<br>
***Apache Spark & HDFS*** - Real-time log aggregation and scalable storage<br>


 

