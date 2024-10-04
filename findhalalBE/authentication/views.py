# authentication/views.py
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.middleware import csrf

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': csrf.get_token(request)})
