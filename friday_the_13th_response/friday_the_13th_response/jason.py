from django.http import JsonResponse
from django.conf import settings
import os
import json

def stock(request):
    try:
        data = {}
        with open(settings.STATIC_ROOT + '/data/stock.json', 'rb') as file:
            data = json.load(file)
    except Exception as e:
        data = {'error' : str(e)}
    return JsonResponse(data)

def article(request):
    try:
        data = {}
        with open(settings.STATIC_ROOT + '/data/article.json', 'rb') as file:
            data = json.load(file)
    except Exception as e:
        data = {'dir' : str(os.path.dirname(os.path.abspath(__file__))), 'error' : str(e), 'base_dir' : str(os.path.abspath(settings.STATIC_ROOT))}
    return JsonResponse(data)
