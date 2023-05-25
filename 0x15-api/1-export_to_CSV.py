#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns information
about his/her TODO list progress
"""
from csv import writer, QUOTE_ALL
import requests
from sys import argv


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    user_id = int(argv[1])
    filename = argv[1] + ".csv"

    user_name = (requests.get(user_url)).json().get("username")
    tasks = requests.get(tasks_url)

    with open(filename, "w", newline='') as csv_file:
        csv_wr = writer(csv_file, quoting=QUOTE_ALL)
        for task in tasks.json():
            if (task.get("userId") == user_id):
                title = task.get("title")
                status = task.get("completed")
                csv_wr.writerow([str(user_id), user_name, status, title])