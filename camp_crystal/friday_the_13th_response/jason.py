from django.http import JsonResponse
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
        with open('./friday_the_13th_response/data/article.json', 'rb') as file:
            data = json.load(file)
    except Exception as e:
        data = {'error' : str(e)}
    return JsonResponse(data)