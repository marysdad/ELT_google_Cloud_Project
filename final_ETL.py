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

