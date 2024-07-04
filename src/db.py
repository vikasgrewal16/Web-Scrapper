import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Vikas@1737',
            database='website_info'
        )
        self.cursor = self.connection.cursor()

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Update credentials if needed
            password='Vikas@1737',  # Update credentials if needed
            database='website_info'  # Update database name if needed
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None


    def create_tables(self):
        create_website_table = """
            CREATE TABLE IF NOT EXISTS websites (
                id INT AUTO_INCREMENT PRIMARY KEY,
                url VARCHAR(255) NOT NULL UNIQUE,
                category VARCHAR(255),
                language VARCHAR(255),
                cms_mvc VARCHAR(255),
                contact_email VARCHAR(255),
                contact_address VARCHAR(255),
                contact_number VARCHAR(255),
                UNIQUE (url)
            )
        """
        self.cursor.execute(create_website_table)
        self.connection.commit()

    def insert_data(self, data):
        insert_query = """
            INSERT INTO websites (url, category, language, cms_mvc, contact_email, contact_address, contact_number)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_query, data)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
