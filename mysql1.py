import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",       # or your database host
    user="test",   # replace with your username
    password="test123",  # replace with your password
    database="test"   # replace with your database
)

cursor = connection.cursor()

# SQL command to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(50),
    hire_date DATE
)
"""

# Execute the command
cursor.execute(create_table_query)

print("Table created successfully!")

# Clean up
cursor.close()
connection.close()
