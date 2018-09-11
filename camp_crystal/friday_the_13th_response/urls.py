from django.urls import path

from . import jason

urlpatterns = [
    path('stock/', jason.stock, name='stock'),
    path('article/', jason.article, name='article')
]
