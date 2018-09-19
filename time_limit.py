
from celery import Celery
import celery
import time
import threading
import kombu
import random

app = Celery(broker='amqp://', backend='amqp://')
app.conf.update(
    result_expires=10,
    broker_pool_limit=0,
)
app.conf.timezone = 'UTC'

@app.task
def foo():
    print 'hello world!'
    time.sleep(random.randint(60,120))



def send_task():
    
    t = foo.apply_async(expires=80, time_limit=75)
    try:
        t.get(timeout=80)
    except celery.exceptions.TaskRevokedError:
        print 'revoked'
    except celery.exceptions.TimeLimitExceeded:
        print 'time limit exceeded by task'


def send_multiple():
    
    threads = [threading.Thread(target=send_task) for _ in xrange(30)]
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
    
