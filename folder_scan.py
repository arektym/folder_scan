from celery import Celery
from db import save_in_db
import os

celery = Celery('folder_scan', broker='amqp://guest@localhost//')

def scan(path):
    '''path must end with / and must be a directory.'''
    assert path[-1] == '/'
    for file_  in os.listdir(path):
        file_stat = os.stat("%s%s" % (path, file_))
        save_in_db(name=file_, path=path, size=file_stat.st_size, perms=file_stat.st_mode,
                   time_c=file_stat.st_ctime, time_m=file_stat.st_mtime)

@celery.task
def scan_folder(*args, **kwargs):
   scan('/home/arek/')    
   return 'done'

if __name__ == "__main__":
    celery = Celery('', backend='redis://localhost', broker='amqp://')
    #scan_folder.apply_async((0, 0))
    scan_folder()
