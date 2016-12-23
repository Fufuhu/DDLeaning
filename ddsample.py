""" This is the program """
import sys
import time
from datadog import initialize, api

ARGS = sys.argv

OPTIONS = {
    'api_key' : ARGS[1],
    'app_key' : ARGS[2]
}

initialize(**OPTIONS)

NOW = int(time.time())
QUERY = 'system.cpu.idle{*}by{host}'
RESULT = api.Metric.query(start=NOW - 3600, end=NOW, query=QUERY)
print(RESULT)
