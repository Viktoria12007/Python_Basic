import re
from typing import List

text: str = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

cars: List[str] = re.findall(r'\b\D\d{3}\D{2}\d{2,3}', text)
taxi: List[str] = re.findall(r'\b\D{2}\d{3}\d{2,3}', text)

print(f'Список номеров частных автомобилей: {cars}')
print(f'Список номеров такси: {taxi}')
