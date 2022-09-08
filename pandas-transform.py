import mysql.connector
import pandas as pd
import os

connection = mysql.connector.connect(read_default_file='/home/kaki/.my.cnf')

current_path = os.getcwd()
file = 'city_housing.csv'
file_path = os.path.join(current_path, 'data_files', file)

print(file_path)

query = """
select * from oscarval_sql_course.city_house_prices
"""


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

# data transformation steps
df.set_index('Date', inplace=True)
df = df.stack().reset_index()

df.columns = ['date', 'city', 'price']

df.to_csv(file_path, index=False)


connection.close()


