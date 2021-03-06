"""
Задание 4.2c

В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.

Переделать скрипт из задания 4.2b таким образом, чтобы, при запросе параметра,
которого нет в словаре устройства, отображалось сообщение 'Такого параметра нет'.

> Попробуйте набрать неправильное име параметра или несуществующий параметр, чтобы увидеть как
ой будет результат. А затем выполняйте задание.

Если выбран существующий параметр,
вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
$ python task_4_2c.py
Enter device name: r1
Enter parameter name (ios,model,vendor,location,ip): io
Такого параметра нет
"""

london_co = {
    'r1' : {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
        },
    'r2' : {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
        },
    'sw1' : {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
        }
}

ask_device = input("Введите имя устройства: ")
try:
    device = london_co[ask_device]
except KeyError:
    print("Устройство не найдено.")
    exit()

ask_param = input("Введите имя параметра ({}): ".format(','.join(list(device.keys()))))
try:
    print(device[ask_param])
except KeyError:
    print("Такого параметра нет")


