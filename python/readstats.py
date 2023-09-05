import mysql.connector
import psutil


cpu_usage = float(psutil.cpu_percent(5))
memory_usage = float(psutil.virtual_memory().percent)
disk_usage =  float(psutil.disk_usage('/')[3])


print(cpu_usage)
print(memory_usage)
print(disk_usage)



conn = mysql.connector.connect(user='root', password='root', host='mysql', port="3306", database='db')
print("DB connected")


cursor = conn.cursor(buffered=True)

cursor.execute("SHOW TABLES;")
print("man o man")


data_to_insert = (cpu_usage,)
print(data_to_insert)
cursor.execute('INSERT INTO cpu (value) VALUES (%s)', data_to_insert)


data_to_insert = (memory_usage,)
cursor.execute('INSERT INTO mem (value) VALUES (%s)', data_to_insert)


data_to_insert = (disk_usage,)
cursor.execute('INSERT INTO disk (value) VALUES (%s)', data_to_insert)

cursor.execute("SELECT * FROM cpu;")

# Fetch and print the results (optional)
for row in cursor.fetchall():
    print(row)
    print("mer")

conn.commit()
conn.close()
