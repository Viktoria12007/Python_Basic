violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

total_duration = 0
count_music = int(input('Сколько песен выбрать? '))
for _ in range(count_music):
    name_music = input('Название ' + str(_ + 1) + ' песни: ')
    total_duration += violator_songs[name_music]
print('Общее время звучания песен:', round(total_duration, 2), 'минуты')
