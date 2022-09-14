#modules
import os
import mysql.connector
import pandas as pd
from google.cloud import bigquery

# file variables
current_path = os.getcwd()
load_file = 'mysql_export.csv'
load_file = os.path.join(current_path, load_file)


