from django.shortcuts import render
from .models import functions_db
#from django.core.context_processors import csrf
#from import request


def useful_functions_list(request):
    functions = ''
    for i in range(len(functions_db)):
        function_name = functions_db[i]["name"]
        functions += f'<b>{functions_db[i]["name"]}</b> >> <a href="/useful/{function_name}" class="dot"> go </a> <br><br> '
    context = {
        'functions': functions
    }
    return render(request, 'useful/useful_functions_list.html', context)

def replaceit(request):
    string_to_change = ''
    symbol_to_change = ''
    symbol_to_place = ''
    oldstring = ''
    changed_string = ''
    context = {}
    if request.method == 'POST':
        string_to_change = request.POST['string_to_change']
        symbol_to_change = request.POST['symbol_to_change']
        symbol_to_place = request.POST['symbol_to_place']
        oldstring = f'<b>Your string was:</b>&nbsp;{string_to_change}'
        changed_string = f'<b>ReplaceIt result:</b>&nbsp;{string_to_change.replace(symbol_to_change, symbol_to_place)}'
    context = {
        'oldstring': oldstring,
        'changed_string': changed_string
    }
    return render(request, 'useful/ReplaceIt.html', context)
#    return f'replaced: {changed_string}'

def magic(request):
    function_description = functions_db[1]["description"] #here is needed to change DB index to "i", it must be find in DB by key "magic" and return dictionary position
    context = {'function_description': function_description}
    return render(request, 'useful/magic.html', context)