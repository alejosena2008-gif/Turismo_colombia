from django.shortcuts import render
from .services import search_destinos

def home(request):
    query = request.GET.get('q', '').strip()
    resultados = search_destinos(query)

    return render(request, 'destinos/index.html', {
        'destinos': resultados,
        'query': query,
        'total': len(resultados)
    })