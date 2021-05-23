from .common import *

SECRET_KEY = 'development-secret-key'

DEBUG = True

ALLOWED_HOSTS = ['*']

# 搜索设置
#ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR="no"
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://elasticsearch_local:9200/'
