
import json
import ssl
import certifi
import unicodedata

from urllib.request import Request, urlopen


URL_DATOS = (
    "https://www.datos.gov.co/resource/qbd2-y27r.json"
    "?$limit=5000"
)


def normalizar(texto):
    """Convierte el texto a minúsculas y elimina las tildes."""
    texto = unicodedata.normalize("NFD", texto.lower())

    return "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )


def obtener_destinos():
    """Consulta los destinos disponibles en Datos Abiertos Colombia."""

    solicitud = Request(
        URL_DATOS,
        headers={
            "User-Agent": "TurismoColombia/1.0"
        }
    )

    contexto_ssl = ssl.create_default_context(
        cafile=certifi.where()
    )

    with urlopen(
        solicitud,
        timeout=15,
        context=contexto_ssl
    ) as respuesta:
        datos = json.loads(
            respuesta.read().decode("utf-8")
        )

    destinos = []

    for registro in datos:

        pais = (
            registro.get("pa_s") or ""
        ).strip()

        region = (
            registro.get("regi_n") or ""
        ).strip()

        visa = (
            registro.get("exige_visa_corta_duraci_n") or ""
        ).strip().upper()

        if not pais or pais.upper() == "(NO REGISTRA)":
            continue

        if visa != "NO":
            continue

        observaciones = (
            registro.get("condiciones_especiales") or ""
        ).strip()

        if not observaciones or observaciones.upper() in (
            "(N/A)",
            "(NO REGISTRA)",
        ):
            observaciones = "Sin observaciones adicionales"

        destinos.append({
            "pais": pais,
            "region": region or "Región no especificada",
            "dias_estadia": "Consultar en consulado",
            "observaciones": observaciones,
        })

    return destinos


def buscar_destinos(termino=""):
    """Busca destinos por nombre del país o región."""

    destinos = obtener_destinos()

    termino = normalizar(
        termino.strip()
    )

    if not termino:
        return destinos

    resultados = []

    for destino in destinos:

        pais = normalizar(destino["pais"])
        region = normalizar(destino["region"])

        if termino in pais or termino in region:
            resultados.append(destino)

    return resultados
