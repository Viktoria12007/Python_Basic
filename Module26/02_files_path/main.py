import os.path
from collections.abc import Iterable


def gen_files_path(*args, start_path: str = os.path.abspath(os.sep)) -> Iterable[str]:
    catalog = input('Введите каталог: ')
    path = os.path.join(start_path, *args)
    for root, dirs, files in os.walk(path):
        if catalog in root:
            for file in files:
                yield os.path.join(root, file)
            break


for file_path in gen_files_path():
    print(file_path)
