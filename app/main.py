from time import sleep
from unittest.mock import sentinel
from autoit import properties
from msilib.schema import Property
import autoit
from autoit import properties

data = []
with open('app/winlist.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        data.append(line.rstrip('\n'))

autoit.run(data[0])
autoit.win_wait_active(title=data[1])
sleep(10)
autoit.win_set_state(title=data[1], flag=properties.SW_MINIMIZE)
autoit.win_set_state(title=data[1], flag=properties.SW_RESTORE)

autoit.run(data[2])
sleep(5)
autoit.win_activate(title=data[3])
autoit.send(send_text="{TAB}{DOWN}{DOWN}{DOWN}{DOWN}{DOWN}{DOWN}{ENTER}")
autoit.win_set_state(title=data[3], flag=properties.SW_MINIMIZE)
autoit.win_set_state(title=data[4], flag=properties.SW_MINIMIZE)
