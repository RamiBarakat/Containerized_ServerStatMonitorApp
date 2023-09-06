import mysql.connector
import psutil
import logging

logging.basicConfig(filename='readstats.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

    return wrapper

@log_functions
def get_system_stats():
    cpu_usage = float(psutil.cpu_percent(5))
    memory_usage = float(psutil.virtual_memory().percent)
    disk_usage = float(psutil.disk_usage('/')[3])
    logging.info(f"CPU Usage: {cpu_usage}%")
    logging.info(f"Memory Usage: {memory_usage}%")
    logging.info(f"Disk Usage: {disk_usage}%")
    return cpu_usage, memory_usage, disk_usage

@log_functions
def connect_to_database():
    try:
        conn = mysql.connector.connect(user='root', password='root', host='mysql', port="3306", database='db')
        logging.info("Connected to the database")
        return conn
    except Exception as e:
        error_message = f"Database connection failed: {str(e)}"
        logging.error(error_message)
        raise e

@log_functions
def insert_data_into_table(conn, table_name, data):
    try:
        cursor = conn.cursor(buffered=True)
        cursor.execute(f"INSERT INTO {table_name} (value) VALUES (%s)", (data,))
        logging.info(f"Inserted data into {table_name} table")
        conn.commit()
        cursor.close()
    except Exception as e:
        error_message = f"Failed to insert data into {table_name} table: {str(e)}"
        logging.error(error_message)
        raise e

@log_functions
def main():
    cpu_usage, memory_usage, disk_usage = get_system_stats()
    conn = connect_to_database()

    insert_data_into_table(conn, "cpu", cpu_usage)
    insert_data_into_table(conn, "mem", memory_usage)
    insert_data_into_table(conn, "disk", disk_usage)

    conn.close()
    logging.info("Closed the database connection")

if __name__ == "__main__":
    main()
