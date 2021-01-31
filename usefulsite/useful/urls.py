from django.urls import path
from . import views


urlpatterns = [
    # здесь должен быть path(), который
    # при обращении к странице /useful/
    # вызовет функцию useful_function_list() из views.py
    # # [примечание] при include запрошенный URL в присоединяемом файле
    # указывается не полностью
    path('', views.useful_functions_list),
    path('ReplaceIt', views.replaceit),
    path('Magic', views.magic),
]
