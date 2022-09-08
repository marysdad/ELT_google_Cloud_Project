from google.cloud import bigquery

client = bigquery.Client(project='bigquery-demo-361613')

sql = "select * from dataset1.movie_2005 limit 10"

query_job = client.query(sql)

results = query_job.result()

for r in results:
    print(r.year, r.title, r.genre, r.avg_vote)