violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

flat_violator_songs = sum(violator_songs, [])
count_music = int(input('Сколько песен выбрать? '))
duration = 0
for count in range(count_music):
    name_music = input('Название ' + str(count + 1) + '-й песни: ')
    duration += flat_violator_songs[flat_violator_songs.index(name_music) + 1]
print('Общее время звучания песен:', round(duration, 2), 'минуты')
