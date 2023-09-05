from flask import Flask, jsonify
import psutil
import mysql.connector
import datetime
import logging


conn = mysql.connector.connect(user='root', password='root', host='mysql', port="3306", database='db')
print("DB connected")

cursor = conn.cursor(buffered=True)

logging.basicConfig(filename='app.log', level=logging.DEBUG)

logging.info('Flask application started.')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_home():
    return "Welcome"


@app.route('/cpu', methods=['GET'])
def get_cpu_stats():

    try:
        cursor.execute("SELECT * FROM cpu;")
        #usages = []
        result = cursor.fetchall()
        data = [{"column1": row[0], "column2": row[1]} for row in result]
        return jsonify(data)

    except Exception as e:
        return jsonify({"error":str(e)})





@app.route("/mem", methods=['GET'])
def get_mem_stats():
    cursor.execute("SELECT * FROM mem;")

    for row in cursor.fetchall():
        print(row)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
