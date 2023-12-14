import mysql.connector
import csv
from credentials import *
from datetime import datetime

def get_db_connection():
    connection = None

    try:

        # Attempt to establish a connection to MySQL database
        connection = mysql.connector.connect(user = username,
                                            password = password,
                                            host = hostname,
                                            port = port)

    except Exception as error:
        print("Error while connecting to database for job tracker", error)
    
    return connection
    
    

def load_third_party(connection, file_path_csv):

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS ticket_sales")
    connection.database = "ticket_sales"

    print("Table: ticket_sales has been created\n")

    cursor.execute("CREATE TABLE IF NOT EXISTS sales (ticket_id INT\
                                                    , trans_date DATE\
                                                    , event_id INT\
                                                    , event_name VARCHAR(50)\
                                                    , event_date DATE\
                                                    , event_type VARCHAR(10)\
                                                    , event_city VARCHAR(20)\
                                                    , customer_id INT\
                                                    , price DECIMAL\
                                                    , num_tickets INT)")



    with open(file_path_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            
            """
            Given that the dates from the CSV file are formatted as MM/DD/YYYY,
            the 'trans_date' and 'event_date' columns must be converted to YYYY-MM-DD
            in order to be compatible with MySQL's DATE type format.
            """

            trans_date = datetime.strptime(row[1], '%m/%d/%Y').strftime('%Y-%m-%d')
            event_date = datetime.strptime(row[4], '%m/%d/%Y').strftime('%Y-%m-%d')

            # Specify which columns to insert into the 'sales' table
            sql = "INSERT INTO sales (ticket_id \
                                    , trans_date \
                                    , event_id \
                                    , event_name \
                                    , event_date \
                                    , event_type \
                                    , event_city \
                                    , customer_id \
                                    , price \
                                    , num_tickets) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            # Specify the set of values that are to be inserted into the 'sales' table
            # and replace the original 'trans_date' and 'event_date' values with MySQL compatible dates
            values = (row[0], trans_date, row[2], row[3], event_date, row[5], row[6], row[7], row[8], row[9])
            cursor.execute(sql, values)
            
            print(f"Inserted {values} into the 'sales' table")

            
    connection.commit()
    cursor.close()

    print(f"\nProcess completed. All rows have been inserted in the 'sales' table")

    return


load_third_party(get_db_connection(), file_path_csv)