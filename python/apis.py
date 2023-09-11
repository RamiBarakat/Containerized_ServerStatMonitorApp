from flask import Flask, jsonify, g
import psutil
import mysql.connector
import datetime
import logging
import os

app = Flask(__name__)

# Configure the logging system
logging.basicConfig(filename='flask_app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_functions(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        logging.info(f"Function {function_name} started with args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Function {function_name} completed successfully. Result: {result}")
            return result
        except Exception as e:
            error_message = f"Function {function_name} failed with error: {str(e)}"
            logging.error(error_message, exc_info=True)
            raise e
    wrapper.__name__ = func.__name__
    return wrapper

cursor = None


'''
@log_functions
def connectDB():
    if 'db_cursor' not in g:
        conn = mysql.connector.connect(user='root', password='root', host='mysql', port="3306", database='db')
        g.db_cursor = conn.cursor(buffered=True)
    return g.db_cursor
''' 

@log_functions
def getEnv():
      return os.getenv('USER'), os.getenv('PASSWORD'), os.getenv('HOST'), os.getenv('PORT'), os.getenv('DATABASE')


@app.route("/", methods=['GET'])
@log_functions
def get_home():
    return "Welcome!"

@app.route('/cpu', methods=['GET'])
@log_functions
def get_cpu_stats():
       try:
           user, password, host, port, database = getEnv()
           conn = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database) 
           cursor = conn.cursor(buffered=True)
           cursor.execute("SELECT * FROM cpu;")
           result = cursor.fetchall()
           for row in result:
               print(row)
           data = [{"TIME": row[1], "PERCENTAGE OF USAGE%": row[2]} for row in result]
           return jsonify(data)
       
       except Exception as e:
           logging.error(str(e))
           return jsonify({"error" : str(e)})
        


@app.route('/mem', methods=['GET'])
@log_functions
def get_mem_stats():
    try:
        user, password, host, port, database = getEnv()
        conn = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database)
        cursor = conn.cursor(buffered=True)
        cursor.execute("SELECT * FROM mem;")
        result = cursor.fetchall()
        data = [{"TIME": row[1], "PERCENTAGE OF USAGE%": row[2]} for row in result]
        return jsonify(data)

    except Exception as e:
        logging.error(str(e))
        return jsonify({"error": str(e)})


@app.route('/disk', methods=['GET'])
@log_functions
def get_disk_stats():
    try:
        user, password, host, port, database = getEnv()
        conn = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database)
        cursor = conn.cursor(buffered=True)
        cursor.execute("SELECT * FROM disk;")
        result = cursor.fetchall()
        data = [{"TIME": row[1], "PERCENTAGE OF USAGE%": row[2]} for row in result]
        return jsonify(data)

    except Exception as e:
        logging.error(str(e))
        return jsonify({"error": str(e)})


@app.route('/cpu_now', methods=['GET'])
#@log_functions
def get_cpu_now():
    now = datetime.datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    cpu_usage = float(psutil.cpu_percent(5))
    return jsonify({current_time: cpu_usage})


@app.route('/mem_now', methods=['GET'])
@log_functions
def get_mem_now():
    now = datetime.datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    memory_usage = float(psutil.virtual_memory().percent)
    return jsonify({current_time: memory_usage})


@app.route('/disk_now', methods=['GET'])
@log_functions
def get_disk_now():
    now = datetime.datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    disk_usage = float(psutil.disk_usage('/')[3])
    return jsonify({current_time: disk_usage})




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
