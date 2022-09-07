import mysql.connector
import pandas as pd

connection = mysql.connector.connect(read_default_file='/home/kaki/.my.cnf')


query = "select year" \
        ", title " \
        ", genre "\
        ", avg_vote "\
        "from `oscarval_sql_course`.`imdb_movies` " \
        "where year between 2005 and 2006"


df = pd.read_sql(query, connection)

yr_2005 = df['year'] == 2005

# print(df['year'].unique())

print(df[yr_2005].head())

connection.close()


