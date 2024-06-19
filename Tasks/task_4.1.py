# Используя подготовленную строку nat, получить новую строку, 
# в которой в имени интерфейса вместо FastEthernet написано GigabitEthernet. 
# Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

nat0 = nat.split()
nat1 = nat0[7].replace('Fast','Gigabit')
nat0[7] = nat1
nat2 = ' '.join(nat0)
print(nat2)
