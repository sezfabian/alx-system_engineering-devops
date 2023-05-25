#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import sys
import requests
import json


def todo(id):
    """
    Function accepts an integer as a parameter, which is the employee ID
    display on the standard output the employee
    TODO list progress in this exact format:
        First line: Employee EMPLOYEE_NAME is done with tasks
            (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
             EMPLOYEE_NAME: name of the employee
             NUMBER_OF_DONE_TASKS: number of completed tasks
             TOTAL_NUMBER_OF_TASKS: total number of tasks,
             which is the sum of completed and non-completed tasks
        Second and N next lines display the title of completed tasks:
            TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
    """
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
    """
    Allows You to Execute Code When the File Runs as a Script,
    but Not When It's Imported as a Module.
    """
    todo(sys.argv[1])
