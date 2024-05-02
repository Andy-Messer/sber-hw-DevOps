# In your_app/views.py
from django.http import JsonResponse
import datetime
from .models import URLVisit


def statistics(request):
    try:
        url_visits = URLVisit.objects.get(url='^time/')
    except:
        url_visits = URLVisit.objects.create(url='^time/')

    data = {'statistics': url_visits.visit_count}
    return JsonResponse(data)


def time(request):
    data = {'time': datetime.datetime.now()}
    return JsonResponse(data)
