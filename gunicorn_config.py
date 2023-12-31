# gunicorn_conf.py
from multiprocessing import cpu_count

bind = "127.0.0.1:8000"
timeout = 120

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/srv/fastapi/access_log'
errorlog =  '/srv/fastapi/error_log'