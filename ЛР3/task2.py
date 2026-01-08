# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=','):
    participants_group1 = set(group1.split(delimiter))
    participants_group2 = set(group2.split(delimiter))
    common_participants = participants_group1.intersection(participants_group2)
    return sorted(common_participants)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group)
print(result)