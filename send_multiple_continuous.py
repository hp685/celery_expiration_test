from time_limit import send_multiple
from time import sleep
import random

for _ in xrange(10000):
    try:
        sleep(random.randint(1,4))
        send_multiple()
    except KeyboardInterrupt:
        break

