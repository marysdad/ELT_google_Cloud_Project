import mysql.connector

connection = mysql.connector.connect(read_default_file='/home/kaki/.my.cnf')

cursor = connection.cursor()




query = "select year" \
        ", title " \
        ", genre "\
        "from `oscarval_sql_course`.`imdb_movies` " \
        "limit 7"

cursor.execute(query)

for (year, title, genre) in cursor:
    print(year, title, genre)


connection.close()


