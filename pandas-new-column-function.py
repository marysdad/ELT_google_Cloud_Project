import mysql.connector
import pandas as pd
import os

connection = mysql.connector.connect(read_default_file='/home/kaki/.my.cnf')

current_path = os.getcwd()
file = 'movies_watchability.csv'
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
        ", duration " \
        "from `oscarval_sql_course`.`imdb_movies` " \
        "where year between 2005 and 2010"


# create duration  label function
def movie_duration(duration):
    if duration < 60:
        return 'short movie'
    elif duration < 90:
        return 'average length movie'
    elif duration < 5000:
        return 'really long movie'
    else:
        return 'No data'

df = pd.read_sql(query, connection)

df['watchability'] = df['duration'].apply(movie_duration)

df.to_csv(file_path, index=False)


connection.close()


