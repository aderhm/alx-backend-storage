#!/usr/bin/env python3
""" Module: Nginx logs stored in MongoDB """

from pymongo import MongoClient


if __name__ == "__main__":
    """Provides some stats about Nginx logs stored in MongoDB
    """
    my_mongo = MongoClient('mongodb://127.0.0.1:27017')

    logs = my_mongo.logs.nginx

    count_logs = logs.count_documents({})
    print("{} logs".format(count_logs))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count_methods = logs.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count_methods))

    count_get = logs.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(count_get))
