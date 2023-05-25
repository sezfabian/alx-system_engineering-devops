#!/usr/bin/python3
import sys
import requests
import json


def todo(id):
    url = 'https://jsonplaceholder.typicode.com/users/' + str(id)
    url1 = 'https://jsonplaceholder.typicode.com/users/' + str(id) + '/todos'
    user = json.loads((requests.get(url)).text)
    tasks = json.loads((requests.get(url1)).text)
    count = 0
    for task in tasks:
        if task['completed'] is True:
            count += 1
    print("Employee {} is done with tasks ({:d}/{:d}):"
          .format(user['name'], count, len(tasks)))
    for task in tasks:
        if task['completed'] is True:
            print("\t {}".format(task['title']))


if __name__ == "__main__":
    todo(sys.argv[1])
