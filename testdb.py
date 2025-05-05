import psycopg2

try:
    conn = psycopg2.connect(
        dbname="kafkadb",
        user="kafkauser",
        password="kafkapassword",
        host="localhost",  
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM system_metrics LIMIT 5;")
    rows = cursor.fetchall()
    print("Connection successful. Sample rows:")
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

except Exception as e:
    print("Failed to connect or query:", e)
