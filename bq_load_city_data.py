from google.cloud import bigquery
import os

client = bigquery.Client(project='bigquery-demo-361613')

target_table = 'bigquery-demo-361613.dataset1.city_housing'

job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True
)

# file variables
current_path = os.getcwd()
file = 'city_housing.csv'
file_path = os.path.join(current_path, file)

with open(file_path, 'rb') as source_file:
    load_job = client.load_table_from_file(
        source_file,
        target_table,
        job_config=job_config
    )

load_job.result()

destination_table = client.get_table(target_table)

print(f"You have {destination_table.num_rows} rows in your table")