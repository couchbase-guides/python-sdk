from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery

# Connect to Couchbase
bucket = Bucket('couchbase://localhost/default')

# Upsert a document in the bucket
bucket.upsert("book1", {
  "isbn": "978-1-4919-1889-0",
  "name": "Minecraft Modding with Forge",
  "cost": 29.99
})

print(bucket.get("book1").value)

query = N1QLQuery("SELECT isbn, name, cost FROM `default`")
for row in bucket.n1ql_query(query):
    print(row)