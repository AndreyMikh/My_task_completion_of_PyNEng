'''
Задание 7.1b

Сделать копию скрипта задания 7.1a.

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/12'
    - значения: список команд, который надо выполнить на этом интерфейсе:
                          ['switchport mode access',
                           'switchport access vlan 10',
                           'switchport nonegotiate',
                           'spanning-tree portfast',
                           'spanning-tree bpduguard enable']


Проверить работу функции на примере словаря access_dict,
с генерацией конфигурации port-security и без.
'''

def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Функция возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    result = {}
    for intf in access:
        result[intf] = ['interface {}'.format(intf)]
        for line in access_template:
            if line.endswith('vlan'):
                result[intf].append('{} {}'.format(line, access[intf]))
            else:
                result[intf].append(line)
        if psecurity:
            for line in port_security:
                result[intf].append(line)

    return result


access_dict = {'FastEthernet0/12':10,
               'FastEthernet0/14':11,
               'FastEthernet0/16':17,
               'FastEthernet0/17':150}
print(generate_access_config(access_dict, True))
