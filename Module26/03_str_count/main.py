import os.path
from collections.abc import Iterable
from typing import Tuple


def get_count_str_py(*args, start_path: str = os.path.abspath(os.sep)) -> Iterable[Tuple[str, str]]:
    path = os.path.join(start_path, *args)
    for root, dirs, files in os.walk(path):
        for file in files:
            cur_path = os.path.join(root, file)
            if os.path.splitext(cur_path)[1] == '.py':
                len_cur_str_py = 0
                with open(cur_path, 'r', encoding='utf-8') as opened_file:
                    for cur_str in opened_file:
                        if not cur_str.strip().startswith(('\n', '#')):
                            len_cur_str_py += 1
                    yield file, len_cur_str_py


for count_str_py in get_count_str_py('Users', 'viki1', 'OneDrive', 'Рабочий стол',
                 'home_work', 'python_basic', 'Module25', '04_RPG_game'):
    print(f'{count_str_py[0]}: {count_str_py[1]}')
