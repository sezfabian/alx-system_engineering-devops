#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns information
about his/her TODO list progress and export data in the CSV format
"""
from csv import writer, QUOTE_ALL
import json
import requests
import sys


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
    filename = id + ".csv"
    with open(filename, "w", newline='') as csv_file:
        csv_wr = writer(csv_file, quoting=QUOTE_ALL)
        for task in tasks:
            csv_wr.writerow([int(id), user['name'],
                            task['completed'], task['title']])


if __name__ == "__main__":
    """
    Allows You to Execute Code When the File Runs as a Script,
    but Not When It's Imported as a Module.
    """
    todo(sys.argv[1])
