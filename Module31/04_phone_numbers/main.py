import re
from typing import List

phone_numbers: List[str] = ['9999999999', '999999-999', '99999x9999', '7800000000', '826458623102', '869855520',
                            '8632541777', 'c454545455']


def check_phone_numbers(phone_numbers: List[str]) -> None:
    for index, value in enumerate(phone_numbers):
        if re.match(r'^[8, 9]\d{9}$', value):
            print(f'{index + 1} номер: всё в порядке')
        else:
            print(f'{index + 1} номер: не подходит')


check_phone_numbers(phone_numbers)

