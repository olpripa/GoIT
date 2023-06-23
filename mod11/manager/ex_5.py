from contextlib import contextmanager
from datetime import datetime
from time import sleep


@contextmanager
def managed_resource(*args, **kwargs):
    log = ''
    timestamp = datetime.now().timestamp()
    msg = '{:<20}|{:^15}| OPEN \n'.format(timestamp, args[0])
    log += msg
    file_handler = open(*args, **kwargs)
    try:
        yield file_handler  # yield == return
    finally:
        diff = datetime.now().timestamp() - timestamp
        msg = '{:<20}|{:^15}| CLOSED {:>15}s \n'.format(datetime.now().timestamp(), args[0], diff)
        file_handler.close()
        log += msg
        print(log)

with managed_resource('new_file.txt', 'r') as f:
    print(f.read())

with managed_resource('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())
