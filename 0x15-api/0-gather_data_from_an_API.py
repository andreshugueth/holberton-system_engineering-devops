#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + user_id)
    todo_keys = {"userId": user_id}
    tasks = requests.get("{}todos".format(url), params=todo_keys)
    number_of_tasks = len(tasks.json())
    employee_name = user.json().get("name")
    done_tasks = 0

    for task in tasks.json():
        if task.get("completed"):
            done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          done_tasks, number_of_tasks))

    for task in tasks.json():
        if task.get("completed"):
            print("\t ", end="")
            print(task.get("title"))
