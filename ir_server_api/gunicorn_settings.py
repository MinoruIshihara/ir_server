wsgi_app = "wsgi"
#chdir = '/work/python/gunic/gu'
daemon = False
bind = "0.0.0.0:8000"
workers = 2

accesslog = "access.log"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

errorlog = "-"
loglevel = "info"
