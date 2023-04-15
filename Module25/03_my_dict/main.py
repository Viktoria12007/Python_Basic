class MyDict(dict):
    def get(self, key):
        return super().get(key, 0)


my_dict = MyDict()
my_dict['name'] = 'Vika'
print(my_dict.get('name'))
print(my_dict.get('city'))
