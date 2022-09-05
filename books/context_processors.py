import time
import requests
import json
from django.conf import settings


def time_processor(request):
    context = {}
    response = requests.post(settings.URL_TIME)
    unix_time = json.loads(response.text)['dataAns']
    unix_time_timezone = (unix_time/1000) + settings.TIMEZONE
    loc_time = time.localtime(unix_time_timezone)
    context['day'] = settings.WEEKDAYS[loc_time.tm_wday]
    context['time'] = time.strftime(settings.TIME_FORMAT, loc_time)
    return context
