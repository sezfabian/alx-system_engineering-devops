#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns information
about his/her TODO list progress and export data in the JSON format
"""
import json
import requests
import sys


def todo(id):
    user_dict = {}
    user_list = []
    user_url = "https://jsonplaceholder.typicode.com/users/" + id
    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    user_id = int(id)
    filename = id + ".json"

    user_name = (requests.get(user_url)).json().get("username")
    tasks = requests.get(tasks_url)

    with open(filename, "w", encoding='utf-8') as f:
        for task in tasks.json():
            if (task.get("userId") == user_id):
                title = task.get("title")
                status = task.get("completed")
                user_dict = {"task": title, "completed": status,
                             "username": user_name}
                user_list.append(user_dict)
        f.write(json.dumps({id: user_list}))


if __name__ == "__main__":
    """
    Allows You to Execute Code When the File Runs as a Script,
    but Not When It's Imported as a Module.
    """
    todo(sys.argv[1])
