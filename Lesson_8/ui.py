from script import input_data, print_data, delete_data, put_data

def ui():
    cmd = ''
    while cmd != 'q':
        cmd = interface()


def interface():
    print('Доброго времени суток! Вы попали на специальную программу от нашей группы! Что же мы можем делать?\n'
          '1. Записать данные(в 2-ух форматах)\n'
          '2. Удалить данные\n'
          '3. Изменить данные\n'
          '4. Вывести данные\n')
    command = input("Введите номер операции: ")
    if command == 'q':
        return command

    while int(command) < 1 or int(command) > 4:
        print('Попробуйте ещё раз выбрать правильную команду')
        command = int(input("Введите номер операции: "))

    if int(command) == 1:
        input_data()
    elif int(command) == 2:
        delete_data()
    elif int(command) == 3:
        put_data()
    elif int(command) == 4:
        print_data()

    return command
