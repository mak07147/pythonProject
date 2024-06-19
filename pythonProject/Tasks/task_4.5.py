""" Из строк command1 и command2 получить список VLANов, которые есть и в команде
command1 и в команде command2 (пересечение). 
В данном случае, результатом должен быть такой список: ['1', '3', '8']. 
Полученный список result вывести на стандартный поток вывода (stdout) с помощью print."""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
res_comand1 = command1.split(" ")[4].split(",")
res_comand2 = command2.split(" ")[4].split(",")
result = sorted(list(set(res_comand1).intersection(res_comand2)))
print(result)
