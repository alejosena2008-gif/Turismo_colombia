
import json
from io import BytesIO
from unittest.mock import patch

from django.test import TestCase

from .services import obtener_destinos, buscar_destinos


class DestinosServiceTests(TestCase):

    @patch("destinos.services.urlopen")
    def test_completa_datos_vacios(self, mock_urlopen):
        datos = [
            {
                "pa_s": "EL SALVADOR",
                "regi_n": "AMERICA CENTRAL",
                "exige_visa_corta_duraci_n": "NO",
                "condiciones_especiales": ""
            }
        ]

        respuesta = BytesIO(json.dumps(datos).encode("utf-8"))
        mock_urlopen.return_value = respuesta

        destinos = obtener_destinos()

        self.assertEqual(len(destinos), 1)
        self.assertEqual(
            destinos[0]["dias_estadia"],
            "Consultar en consulado"
        )
        self.assertEqual(
            destinos[0]["observaciones"],
            "Sin observaciones adicionales"
        )

    @patch("destinos.services.obtener_destinos")
    def test_busca_por_nombre_del_pais(self, mock_obtener):
        mock_obtener.return_value = [
            {
                "pais": "EL SALVADOR",
                "region": "AMERICA CENTRAL",
                "dias_estadia": "Consultar en consulado",
                "observaciones": "Sin observaciones adicionales"
            }
        ]

        resultados = buscar_destinos("salvador")

        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]["pais"], "EL SALVADOR")

    @patch("destinos.services.obtener_destinos")
    def test_busqueda_sin_coincidencias(self, mock_obtener):
        mock_obtener.return_value = [
            {
                "pais": "EL SALVADOR",
                "region": "AMERICA CENTRAL",
                "dias_estadia": "Consultar en consulado",
                "observaciones": "Sin observaciones adicionales"
            }
        ]

        resultados = buscar_destinos("ZZZZZZ")

        self.assertEqual(resultados, [])


class DestinosViewTests(TestCase):

    @patch("destinos.views.buscar_destinos", return_value=[])
    def test_muestra_pagina_sin_resultados(self, mock_buscar):
        respuesta = self.client.get("/", {"q": "ZZZZZZ"})

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.context["destinos"], [])
        self.assertEqual(respuesta.context["termino"], "ZZZZZZ")
