
from django.shortcuts import render
from urllib.error import URLError
from json import JSONDecodeError

from .services import buscar_destinos


def inicio(request):
    termino = request.GET.get("q", "").strip()

    try:
        destinos = buscar_destinos(termino)
        error = None

    except (URLError, TimeoutError, JSONDecodeError, OSError):
        destinos = []
        error = (
            "No fue posible consultar los destinos. "
            "Inténtalo nuevamente más tarde."
        )

    return render(
        request,
        "destinos/inicio.html",
        {
            "destinos": destinos,
            "termino": termino,
            "error": error,
        },
    )
