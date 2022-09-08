import mysql.connector
import pandas as pd
import os

connection = mysql.connector.connect(read_default_file='/home/kaki/.my.cnf')

current_path = os.getcwd()
file = 'movies_rating.csv'
file_path = os.path.join(current_path, 'data_files', file)

print(file_path)

query = "select year" \
        ", title " \
        ", genre "\
        ", avg_vote "\
        ", case " \
        " when avg_vote < 3 then 'bad' "\
        " when avg_vote < 6 then 'okay' "\
        "when avg_vote >= 6 then 'good' "\
        "end as movie_rating "\
        "from `oscarval_sql_course`.`imdb_movies` " \
        "where year between 2005 and 2010"


df = pd.read_sql(query, connection)

df.to_csv(file_path, index=False)


connection.close()


