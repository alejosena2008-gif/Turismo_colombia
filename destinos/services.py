import csv
import os
from django.conf import settings

CSV_PATH = os.path.join(settings.BASE_DIR, 'data', 'paises_sin_visa.csv')

def load_destinos():
    destinos = []
    if not os.path.exists(CSV_PATH):
        return destinos

    with open(CSV_PATH, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pais = row.get('PAIS', '').strip()
            region = row.get('REGION', '').strip()
            dias = row.get('DIAS_PERMITIDOS', '').strip()
            observaciones = row.get('OBSERVACIONES', '').strip()

            if pais:
                destinos.append({
                    'pais': pais,
                    'region': region or 'No especificada',
                    'dias': dias or 'Consultar en consulado',
                    'observaciones': observaciones or 'Sin observaciones adicionales'
                })
    return destinos

def search_destinos(query=""):
    destinos = load_destinos()
    query = (query or "").strip().lower()
    if not query:
        return destinos

    return [
        d for d in destinos
        if query in d['pais'].lower() or query in d['region'].lower()
    ]