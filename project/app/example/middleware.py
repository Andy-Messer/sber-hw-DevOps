from django.urls import resolve
from .models import URLVisit

class URLVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.method == 'GET':
            resolved_path = resolve(request.path_info).route
            URLVisit.objects.update_or_create(url=resolved_path)
            try:
                url_visits = URLVisit.objects.get(url=resolved_path)
            except:
                url_visits = URLVisit.objects.create(url=resolved_path)
            url_visits.visit_count += 1
            url_visits.save()
        return response