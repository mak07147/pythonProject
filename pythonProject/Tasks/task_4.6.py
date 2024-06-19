""" Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix 10.0.24.0/24
AD/Metric 110/41
Next-Hop 10.0.13.3
Last update 3d18h
Outbound Interface FastEthernet0/0 """

ospf_route = "10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

a = ospf_route.split()

b = a.remove('via')
d_keys = ['Prefix','AD/Metric','Next-Hop','Last update','Outbound Interface']

c = dict.fromkeys(d_keys, a)

print(a)