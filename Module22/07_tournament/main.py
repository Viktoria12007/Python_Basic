min_scores = 80
participants = [{'surname': 'Ivanov', 'name': 'Serg', 'scores': '80'},
                {'surname': 'Sergeev', 'name': 'Petr', 'scores': '92'},
                {'surname': 'Petrov', 'name': 'Vasiliy', 'scores': '98'},
                {'surname': 'Vasiliev', 'name': 'Maxim', 'scores': '78'}]


def open_write(name, first_str, participants):
    file_w = open(name, 'w')
    file_w.write(''.join((first_str, '\n')))
    participants_str_arr = [' '.join(participant.values()) for index, participant in enumerate(participants)]
    for index, participant in enumerate(participants_str_arr):
        if 'second' in name:
            file_w.write(''.join((str(index + 1), ') ')))
        file_w.write(''.join((participant, '\n')))
    file_w.close()
    file_r = open(name, 'r')
    file_r.close()


def get_scores(item):
    return int(item['scores'])


def get_new_format_dict(item):
    new_format = {
        'name': ''.join((item['name'][0:1], '.')),
        'surname': item['surname'],
        'scores': item['scores'],
    }
    return new_format


def get_text_second_tour(participants):
    next_winners = list(filter(lambda x: int(x['scores']) > min_scores, participants))
    next_winners_new_format = list(map(get_new_format_dict, next_winners))
    next_winners_new_format.sort(reverse=True, key=get_scores)
    return next_winners_new_format


open_write('first_tour.txt', str(min_scores), participants)
next_participants = get_text_second_tour(participants)
open_write('second_tour.txt', str(len(next_participants)), next_participants)
