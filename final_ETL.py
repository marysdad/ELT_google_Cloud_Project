#modules
import os
import mysql.connector
import pandas as pd
from google.cloud import bigquery

# file variables
current_path = os.getcwd()
load_file = 'mysql_export.csv'
load_file = os.path.join(current_path, load_file)


proj='bigquery-demo-361613'
dataset = 'dataset1'
target_table = 'annual_movie_summary'
table_id = f'{proj}.{dataset}.{target_table}'


# data connections
connection = mysql.connector.connect(read_default_file='/home/kaki/.my.cnf')
client = bigquery.Client(project=proj)


# create out SQL extract query
sql = """

select year, count(imdb_title_id) as movie_count,
avg(duration) as avg_movie_duration,
avg(avg_vote) as avg_rating,
from `oscarval_sql_course`.`imdb_movies`
group by 1

"""

# extract data
df = pd.read_sql(sql, connection)