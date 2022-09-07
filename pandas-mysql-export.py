import mysql.connector
import pandas as pd
import os

connection = mysql.connector.connect(read_default_file='/home/kaki/.my.cnf')

current_path = os.getcwd()
file = 'movies.csv'
file_path = os.path.join(current_path, 'data_files', file)

print(file_path)

query = "select year" \
        ", title " \
        ", genre "\
        ", avg_vote "\
        "from `oscarval_sql_course`.`imdb_movies` " \
        "where year between 2005 and 2010"


df = pd.read_sql(query, connection)

yr_2005 = df['year'] == 2005


# print(df['year'].unique())

# print(df[yr_2005].head())

df[yr_2005].to_csv(file_path, index=False)


connection.close()


