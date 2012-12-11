licence: gpl2
author: arek@goodcode.co.uk

run it:
celery -A folder_scan worker --loglevel=info &
python web.py


then browse to:
http://127.0.0.1:5000/ or http://127.0.0.1:5000/ for file list 


post filename:'filename' to http://127.0.0.1:5000/file_info/ for file info
