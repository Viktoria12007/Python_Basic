import os
from typing import IO


class File:
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    def __enter__(self) -> IO:
        if not os.path.exists(self._file_name):
            self._file = open(self._file_name, 'w', encoding='utf-8')
            return self._file
        else:
            self._file = open(self._file_name, encoding='utf-8')
            return self._file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self._file.close()
        if exc_type is FileExistsError or exc_type is FileNotFoundError:
            return True


with File('test.txt') as file:
    test_str = 'Что-то происходит2...'
    print(test_str)
    # file.write(test_str)
    # raise TypeError('Ошибка для теста!')
    # raise FileExistsError('Ошибка для теста!')
    print(file.read())
