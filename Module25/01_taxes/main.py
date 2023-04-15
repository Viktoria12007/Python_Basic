class Property:
    def __init__(self, worth):
        self.worth = worth

    def get_tax(self):
        return self.worth / self.worth


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        return self.worth / 500


def taxes():
    money = int(input('Сколько у вас денег? '))
    apartment_price = int(input('Сколько стоит квартира? '))
    car_price = int(input('Сколько стоит машина? '))
    country_house_price = int(input('Сколько стоит дача? '))
    apartment = Apartment(apartment_price)
    car = Car(car_price)
    country_house = CountryHouse(country_house_price)
    print('Налог на квартиру:', apartment.get_tax())
    print('Налог на машину:', car.get_tax())
    print('Налог на дачу:', country_house.get_tax())
    difference = money - apartment.get_tax() - car.get_tax() - country_house.get_tax()
    if difference < 0:
        print('Вам не хватает денег:', abs(difference))


taxes()
