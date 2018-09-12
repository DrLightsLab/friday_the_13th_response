from django.http import JsonResponse
from django.conf import settings
import json

def stock(request):
    try:
        data = {}
        with open('./friday_the_13th_response/data/stock.json', 'rb') as file:
            data = json.load(file)
    except Exception as e:
        data = {'error' : str(e)}
    return JsonResponse(data)

def article(request):
    try:
        data = {}
        with open(settings.BASE_DIR, 'rb') as file:
            data = json.load(file)
    except Exception as e:
        data = {'error' : str(e)}
    return JsonResponse(data)