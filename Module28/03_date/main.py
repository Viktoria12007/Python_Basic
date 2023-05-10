class Date:
    _day = None
    _month = None
    _year = None

    def __str__(self) -> str:
        return f'День: {self._day}   Месяц: {self._month}   Год: {self._year}'

    @classmethod
    def from_string(cls, date_string: str) -> str | None:
        try:
            if cls.is_date_valid(date_string):
                d, m, y = date_string.split('-')
                cls._day = int(d)
                cls._month = int(m)
                cls._year = int(y)
                return cls.__str__(cls)
            else:
                print('Неверный формат даты!')
        except:
            print('Что-то пошло не так...')

    @classmethod
    def is_date_valid(cls, date_string: str) -> bool | None:
        try:
            d, m, y = date_string.split('-')
            return 0 < int(d) < 32 and 0 < int(m) < 13 and int(y) > 0
        except:
            print('Что-то пошло не так...')


date = Date.from_string('10-12-2077')
date2 = Date.from_string('05-12-2017')
print(date)
print(date2)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
