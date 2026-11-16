from django.shortcuts import render
from .services import load_destinos, search_destinos

def home(request):
    query = request.GET.get('q', '').strip()
    region_filtro = request.GET.get('region', '').strip()
    dias_filtro = request.GET.get('dias', '').strip()

    todos = load_destinos()
    resultados = search_destinos(query)

    if region_filtro:
        resultados = [d for d in resultados if region_filtro.lower() in d['region'].lower()]

    if dias_filtro:
        resultados = [d for d in resultados if dias_filtro.lower() in d['dias'].lower()]

    regiones = sorted(list({d['region'] for d in todos if d.get('region')}))
    regiones_count = len({d['region'] for d in resultados})
    larga_estadia = sum(1 for d in resultados if '90' in d['dias'] or '180' in d['dias'])

    return render(request, 'destinos/index.html', {
        'destinos': resultados,
        'query': query,
        'region_filtro': region_filtro,
        'dias_filtro': dias_filtro,
        'regiones': regiones,
        'total': len(resultados),
        'total_catalogo': len(todos),
        'regiones_count': regiones_count,
        'larga_estadia': larga_estadia,
    })