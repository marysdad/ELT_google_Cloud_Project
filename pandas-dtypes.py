import mysql.connector
import pandas as pd

connection = mysql.connector.connect(read_default_file='/home/kaki/.my.cnf')


query = "select year" \
        ", title " \
        ", genre "\
        ", avg_vote "\
        "from `oscarval_sql_course`.`imdb_movies` " \
        "limit 7"

df = pd.read_sql(query, connection)
print(df.dtypes)

connection.close()


