class MyDict(dict):
    """ Класс MyDict. Родитель: dict """
    def get(self, key):
        """
        Геттер для получения значения словаря по ключу

        :param key: передаётся ключ словаря
        :type: str
        :return: super().get(key, 0)
        :rtype: Optional[Any]
        """
        return super().get(key, 0)


my_dict = MyDict()
my_dict['name'] = 'Vika'
print(my_dict.get('name'))
print(my_dict.get('city'))
