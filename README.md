# Data Pipeline Mini Project

### Introduction
In this mini project, the MySQL Python connector is leveraged in order to populate a MySQL database with ticket sales data sourced from a CSV file. The `db_connection_and_data_loader.py` file establishes a connection to a MySQL database, creates a `sales` table within the `ticket_sales` database. Once the table has been instantiated, the data from the CSV file is processed and inserted into the table.

After the data is loaded into the table, it is queried to return the most popular events based on the number of tickets sold.

## Getting Started

### Prerequisites
To establish a connection to MySQL using Python, it is necessary to install the MySQL Python connector in order to load and query the `sales` table within the `ticket_sales` database. This Python module can be installed by executing the following:
```
pip3 install mysql-connector-python
```

In order to establish a connection to MySQL database, replace the placeholder values for user, password, host and port within the `db_connection_and_data_loader.py` file (*see lines 12 through 15*) with the parameters matching your local instance of MySQL.