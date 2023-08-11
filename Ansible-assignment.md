# Ansible assignment
## Create and deploy your own service
### The development stage:
For the true enterprise grade system we will need Python3, Flask and emoji support. Why on Earth would we create stuff that does not support emoji?!

* the service listens at least on port 80
* the service accepts GET and POST methods
* the service should receive `JSON` object and return a string decorated with your favorite emoji in the following manner:
```sh
curl -XPOST -d'{"word":"evilmartian", "count": 3}' http://myvm.localhost/
💀evilmartian💀evilmartian💀evilmartian💀

curl -XPOST -d'{"word":"bomb", "count": 3}' http://myvm.localhost/

curl -XPOST -d'{"word":"mice", "count": 5}' http://myvm.localhost/
🐘mice🐘mice🐘mice🐘mice🐘mice🐘

curl -XPOST -d'{"word":"mouse", "count": 5}'
```
* bonus points for being creative when serving `/`

### Hints
* [installing flask](https://flask.palletsprojects.com/en/1.1.x/installation/#installation)
* [become a developer](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [or whatch some videos](https://www.youtube.com/watch?v=Tv6qXtc4Whs)
* [dealing with payloads](https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask)
* [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request.get_json)
* what would you expect to see when visiting a random unknown website?

### The operating stage:
* create an ansible playbook that deploys the service to the VM
* make sure all the components you need are installed and all the directories for the app are present
* configure systemd so that the application starts after reboot
* secure the VM so that our product is not stolen: allow connections only to the ports 22,80,443. Disable root login. Disable all authentication methods except 'public keys'.
* bonus points for SSL/HTTPS support with self-signed certificates
* bonus points for using ansible vault

### Hints
* task:verify
* iptables, sshd_config
* good luck! ¯\_(ツ)_/¯

=====================================================================================================



Решение

1.Сначала настроил связь черз публичный ключ с локалхостом. Потом отключил беспарольный вход.(vim /etc/ssh/sshd_congid) - раскоментировал и закоментировал нужные строки
2. Потом развернул и настроил ansible, конфига на убунту не было по умолчанию, поэтому создал общую папку /etc/ansible - куда положил нужные директории и файлы. 
hosts - прописал хосты, с которыми нужно будет устанавливать соединение и конфигурировать.
директория vargant/grops/ - прописал юзера, который будет заходить на хост и интерпритатор по умолчанию(питоновский).
папка playbooks - где пишуться плейбуки с основной конфигурационной инфой в формате yml(Очень чуствительный к пробелам язык)
Далее установил flask и виртуальную среду для исполнения приложения.
Потом установил соединение с 127.1, проверял, чинил, настраивал.
Потом самое сложное, написание самого приложения,  в соответсвии с заданием, так чтобы оно правильно работало.
Потом настройка файрвола по правилам в задаче, проверка.
Потом финальная проверка с запуском сервиса принимающего объект json и выдающий строку декорированную эмоджи
curl -X POST -H 'Content-Type:application/json' -d '{"word":"thumbs_up", "count": 5}'  http://localhost:80/service
Все ок. Бонусные задачи не выполнял. Может потом

Выводы - нужно изучать прям основательно yml и python, пригодятся очень в будущем.
























