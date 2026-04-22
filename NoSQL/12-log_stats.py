#!/usr/bin/env python3

"""12-log_stats.py
"""

from pymongo import MongoClient


def main():
    """Entry point
    """

    client = MongoClient('mongodb://127.0.0.1:27017')
    print(f"{client.logs.nginx.count_documents({})} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        length = client.logs.nginx.count_documents({'method': method})
        print(f"\t{method} {length}")

    filters = {'method': 'GET', 'path': '/status'}
    status_len = client.logs.nginx.count_documents(filters)

    print(f"{status_len} status check")


if __name__ == '__main__':
    main()
