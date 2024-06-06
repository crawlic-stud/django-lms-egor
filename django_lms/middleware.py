from django.http import HttpResponseForbidden

ALLOWED_IPS = ['95.55.95.113']  # Замените на ваш IP-адрес

class AdminRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.META['REMOTE_ADDR'] not in ALLOWED_IPS:
            return HttpResponseForbidden("Forbidden")
        return self.get_response(request)