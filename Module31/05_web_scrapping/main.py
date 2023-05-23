import re
from typing import List
import requests


def get_h3_content(text: str) -> List[str]:
    return [item[1] for item in re.findall(r'(<h3>)(.+)(</h3>)', text)]


with open('examples.html', 'r') as f:
    text: str = f.read()
    print(get_h3_content(text))

result: object = requests.get('https://tproger.ru/translations/regular-expression-python/')
print(get_h3_content(result.text))
