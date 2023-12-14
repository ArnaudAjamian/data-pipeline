from db_connection_and_data_loader import *

def query_popular_tickets(connection):

    # Get the most popular event
    sql_statement = f"""SELECT event_name, SUM(num_tickets)
                    FROM ticket_sales.sales
                    GROUP BY event_name
                    ORDER BY SUM(num_tickets) DESC"""
    
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()


    print(f"\nHere are the most popular events:")
    for record in records:
        print(f"- {record[0]}")

query_popular_tickets(get_db_connection())