from kafka import KafkaConsumer
import psycopg2
import json

# Kafka configurations
KAFKA_SERVER ='localhost:9092'  
KAFKA_TOPIC = 'metrics-topic'

# PostgreSQL configurations
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'kafkadb'
DB_USER = 'kafkauser'
DB_PASSWORD = 'kafkapassword'

# Connect to PostgreSQL
def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Insert data into the database
def insert_metrics_data(cpu, mem, disk):
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO system_metrics (cpu, mem, disk) VALUES (%s, %s, %s)",
                (cpu, mem, disk)
            )
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Error inserting data into database: {e}")
        finally:
            conn.close()

# Kafka Consumer setup
def consume_messages():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=[KAFKA_SERVER],
        group_id='metrics-group',
        auto_offset_reset='earliest',  # Start reading at the earliest message
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    # for message in consumer:
    #     # Assuming message format: {"id": <id>, "cpu": <cpu>, "mem": <mem>, "disk": <disk>}
    #     data = message.value.decode('utf-8')  # Decode byte message
    #     print(f"Received message: {data}")
        
    #     # Parse JSON message
    #     try:
    #         metrics = json.loads(data)
    #         cpu = metrics['cpu']
    #         mem = metrics['mem']
    #         disk = metrics['disk']
    #         insert_metrics_data(cpu, mem, disk)
    #     except Exception as e:
    #         print(f"Error processing message: {e}")


    for message in consumer:
        metrics = message.value  # Already parsed JSON
        print(f"Received message: {metrics}")
        try:
            insert_metrics_data(metrics['cpu'], metrics['mem'], metrics['disk'])
        except Exception as e:
            print(f"Error processing message: {e}")

if __name__ == '__main__':
    consume_messages()
