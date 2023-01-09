from datetime import datetime
import time
import random

odds = range(1, 60, 2)

for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print(f'Текущая минута {time.strftime("%H:%M")} является нечетной.')
    else:
        print(f'Текущая минута {time.strftime("%H:%M")} является четной.')
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)
