import json
from typing import List

diff_list: List[str] = ["services", "staff", "datetime"]
result: dict = {}


def compare_two_item(old_item: list | dict, new_item: list | dict, is_dict: bool) -> None:
    for index, key in enumerate(old_item):
        if is_dict:
            get_by_key_or_index(old_item, new_item, key)
        else:
            get_by_key_or_index(old_item, new_item, index)


def get_by_key_or_index(old_item: list | dict, new_item: list | dict, index_or_key: str | int) -> None:
    if index_or_key in diff_list:
        old_str: str = json.dumps(old_item[index_or_key])
        new_str: str = json.dumps(new_item[index_or_key])
        if old_str != new_str:
            result[index_or_key] = new_item[index_or_key]
    if isinstance(old_item[index_or_key], dict):
        compare_two_item(old_item[index_or_key], new_item[index_or_key], True)
    if isinstance(old_item[index_or_key], list):
        compare_two_item(old_item[index_or_key], new_item[index_or_key], False)


def compare_two_json(json_old: str, json_new: str) -> None:
    with open(json_old, 'r') as file:
        old_dict: dict = json.load(file)

    with open(json_new, 'r') as file:
        new_dict: dict = json.load(file)

    compare_two_item(old_dict, new_dict, True)

    with open('result.json', 'w') as file:
        file.write(json.dumps(result))

    print(result)


compare_two_json('json_old.json', 'json_new.json')
