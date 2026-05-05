#!/usr/bin/env python3
"""Nginx logs stats"""

from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
collection = client.logs.nginx

# total logs
print(f"{collection.count_documents({})} logs")

# methods
print("Methods:")
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for m in methods:
    count = collection.count_documents({"method": m})
    print(f"\tmethod {m}: {count}")

# status check
count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{count} status check")
