import mysql.connector

connection = mysql.connector.connect(read_default_file='/home/kaki/.my.cnf')

connection.close()


