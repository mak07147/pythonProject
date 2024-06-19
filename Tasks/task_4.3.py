""" Получить из строки config такой список VLANов: ['1', '3', '10', '20', '30', '100'] """

config = "switchport trunk allowed vlan 1,3,10,20,30,100"

result = config.split()[4].split(',')

print(result)