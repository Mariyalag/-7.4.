# print('Привет, ' + str(14) + 'мир!')
# print('Привет, ' + 'мир!')
# print('Меня зовут %s ' % 'Денис')
# print('Меня зовут %s, мне %d' % ('Денис', 14))
# print('Меня зовут %(name)s, мне %(year)s' % {'name': 'Денис', 'year': 14})
# print('Я учусь в {}'.format('Урбан'))
# print('Я учусь в {} {}'.format('Урбан', '-university'))
# print('Я учусь в  {0} {1} {0}'.format('Урбан', '-university'))
# print('Я учусь в  {title} {postfix} {title}'.format(title='Урбан', postfix='-university'))
# print(f'{'Urban' * 2} это лучший универсистет!')
# print(f'{'Urban' * 2} это лучший универсистет!')


# print('В команде Мастера кода участников: %s ' % '5!')

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 2153.31451
tasks_total = 82
time_avg = 350.4
challenge_result = 'победа команды Мастера кода!'

result = "В команде Мастера кода участников: %s !" % team1_num
result2 = "Итого сегодня в командах участников: %s и %d ! " % (team1_num,  team2_num)
result3 = 'Команда Волшебники данных решила задач: {}! '.format(score_2)
result4 = 'Волшебники данных решили задачи за {} с !'.format(team1_time)
result5 = (f'Команды решили {score_1} и {score_2} задач.')
result6 = (f'Результат битвы: {challenge_result} ')
result7 = (f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')


print(result)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)






# if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
#     result = 'Победа команды Мастера кода!'
# elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
#     result = 'Победа команды Волшебники Данных!'
# else:
#     result = 'Ничья!'
# print(challenge_result)