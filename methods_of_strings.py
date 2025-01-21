team1 = "Мастеры кода"
team2 = "Волшебники данных"
team1_num = 5  # колличество участников первой команды
team2_num = 6
score_1 = 40  # колличество баллов
score_2 = 42
team1_time = 18015.2  # затраченное время на задачи
team2_time = 19033.2

# %
print('В команде Мастера кода участников: %(team1_num)d, в команде Волшебники данных: %(team2_num)s' % {
    'team1_num': team1_num, 'team2_num': team2_num})
print('Итого, сегодня в командах участников:  %(team1_num)d и %(team2_num)d' % {'team1_num': team1_num,
                                                                                'team2_num': team2_num})

# format()
print('Команда Волшебников данных решила {score_2} задач'.format(score_2=score_2))
print('Волшебники данных на решение затратили время {team1_time}'.format(team1_time=team1_time))

# f-string
print(f'Команды решили {score_1} и {score_2} задач ')
print(f'Победила команда: {team1 if score_1 > score_2 else team2}')
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по : '
      f'{round(((team1_time / score_1) + (team2_time / score_2)) / 2), 2} сек на задачу')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'Победа команды {team1}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'Победа команды {team2}!'
else:
    result = f'Ничья!'
print(result)

print(round(2.023948, 2))
