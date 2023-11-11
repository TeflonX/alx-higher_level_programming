#!/usr/bin/python3
"""
Module

a script that adds all arguments to a Python list, and then
save them to a file
"""


from sys import argv
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file_name = "add_item.json"
try:
    my_list = load_from_json_file(file_name)
except (FileNotFoundError, json.JSONDecodeError):
    my_list = []

save_to_json_file(my_list + argv[1:], file_name)
