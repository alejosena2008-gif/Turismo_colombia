HU-01: Listar todos los países sin visa de turismo (Issue #1)
Type: Feature | Label: Historia de Usuario
Priority: P0 (High) | Size: M | Estimate: 3 Story Points | Status: Done
Milestone: Sprint 1 — Incremento Funcional de Consulta de Destinos

Historia de Usuario:

Como ciudadano colombiano que planea un viaje al exterior,
quiero ver la lista completa de países que no me exigen visa de turismo,
para conocer mis opciones de viaje sin tener que realizar trámites consulares previos.

Criterios de Aceptación:

 La página principal (/) carga y muestra el catálogo de países desde el archivo oficial de datos.gov.co (bign-27m7).
 Cada tarjeta presenta: Nombre del país, Región, Días de permanencia permitidos y Observaciones.
 La interfaz muestra los datos reales diferenciados de cualquier ejemplo estático.
HU-02: Buscar y filtrar países por nombre o región (Issue #2)
Type: Feature | Label: Historia de Usuario
Priority: P0 (High) | Size: L | Estimate: 5 Story Points | Status: Done
Milestone: Sprint 1 — Incremento Funcional de Consulta de Destinos

Historia de Usuario:

Como viajero colombiano,
quiero ingresar el nombre de un país o una región geográfica en un buscador,
para saber en segundos si requiero visa y cuántos días puedo permanecer legalmente.

Criterios de Aceptación:

 Existe un campo de búsqueda y botón "Buscar" en la pantalla principal.
 La búsqueda filtra coincidencias tanto por nombre de país (ej. "Brasil") como por región (ej. "Europa"), sin importar mayúsculas o minúsculas.
 Se incluye un botón "Limpiar" para restablecer la vista con todos los destinos.
HU-03: Pruebas unitarias de vistas y manejo de casos borde (Issue #3)
Type: Task | Label: Historia de Usuario
Priority: P1 (Medium) | Size: S | Estimate: 2 Story Points | Status: Done
Milestone: Sprint 1 — Incremento Funcional de Consulta de Destinos

Historia de Usuario:

Como equipo de desarrollo,
queremos contar con pruebas automatizadas en Django (tests.py),
para verificar que el recorrido principal y las búsquedas sin coincidencias funcionan sin errores bloqueantes.

Criterios de Aceptación:

 Prueba automatizada test_home_page_status_200 comprueba que la página carga con código HTTP 200.
 Prueba automatizada test_search_existing_country verifica que una búsqueda válida muestra el país esperado.
 Prueba automatizada test_search_no_results verifica que una búsqueda inexistente muestra el mensaje amigable sin fallar.
 El comando python manage.py test finaliza con resultado OK.
HU-04: Documentación del producto, reproducibilidad y origen de datos (Issue #4)
Type: Task | Label: documentation
Priority: P2 (Low) | Size: S | Estimate: 2 Story Points | Status: Done
Milestone: Sprint 1 — Incremento Funcional de Consulta de Destinos

Historia de Usuario:

Como docente o evaluador externo,
quiero contar con instrucciones claras de instalación y el contexto de descubrimiento en el README.md,
para clonar, ejecutar y verificar la aplicación localmente siguiendo el origen de los datos.

Criterios de Aceptación:

 El README.md documenta la hipótesis de necesidad, el beneficiario, el Product Goal, el Sprint Goal y la DoD.
 Incluye los pasos reproducibles de instalación (venv, requirements.txt, manage.py test y runserver).
 Registra el resultado de la Sprint Review y la acción de mejora de la Sprint Retrospective.
HU-05: Manejo de estados vacíos y tolerancia a datos incompletos (Issue #5)
Type: Feature | Label: Historia de Usuario
Priority: P1 (Medium) | Size: M | Estimate: 3 Story Points | Status: Done
Milestone: Sprint 1 — Incremento Funcional de Consulta de Destinos

Historia de Usuario:

Como usuario de la aplicación,
quiero recibir un mensaje comprensible cuando mi búsqueda no tenga coincidencias o falte algún dato en el registro,
para entender qué ocurrió sin encontrarme con pantallas vacías o errores técnicos.

Criterios de Aceptación:

 Cuando una búsqueda no tiene resultados, se muestra el mensaje "No se encontraron destinos para [búsqueda]" con una recomendación de uso.
 Si un registro del CSV tiene campos de días u observaciones vacíos, el servicio asigna valores por defecto seguros ("Consultar en consulado" / "Sin observaciones adicionales").
HU-06: Preparación del entorno Django, starter base y control de versiones (Issue #6)
Type: Task | Label: enhancement
Priority: P0 (High) | Size: S | Estimate: 1 Story Point | Status: Done
Milestone: Sprint 1 — Incremento Funcional de Consulta de Destinos

Historia de Usuario:

Como desarrollador del equipo,
quiero estructurar el proyecto Django separando rutas, vistas, servicios y plantillas junto con un .gitignore adecuado,
para mantener el repositorio limpio, modular y sin subir entornos virtuales ni archivos temporales.

Criterios de Aceptación:

 Archivo .gitignore excluye venv/, __pycache__/ y *.sqlite3.
 Separación de responsabilidades en urls.py, views.py, services.py, templates/ y tests.py.
 Archivo requirements.txt generado con las versiones compatibles de Django.
HU-07: Contador dinámico y resumen estadístico de destinos (Issue #7)
Type: Feature | Label: Historia de Usuario
Priority: P1 (Medium) | Size: S | Estimate: 2 Story Points | Status: Done
Milestone: Sprint 1 — Incremento Funcional de Consulta de Destinos

Historia de Usuario:

Como viajero colombiano,
quiero visualizar un contador dinámico con el total de destinos encontrados,
para dimensionar rápidamente cuántas alternativas de viaje tengo en cada región o búsqueda.

Criterios de Aceptación:

 La vista principal muestra el total de países disponibles al cargar la página.
 Al filtrar por país o región, el contador se actualiza automáticamente mostrando la cantidad exacta de resultados.
 Si no hay coincidencias, el contador muestra 0.
HU-08: Diseño responsivo para móviles y componente de atribución oficial (Issue #8)
Type: Feature | Label: Historia de Usuario
Priority: P2 (Low) | Size: M | Estimate: 2 Story Points | Status: Done
Milestone: Sprint 1 — Incremento Funcional de Consulta de Destinos

Historia de Usuario:

Como ciudadano que consulta desde un teléfono móvil o computador,
quiero navegar en una interfaz clara y adaptable que incluya el enlace directo a la fuente oficial del Estado,
para consultar cómodamente desde cualquier pantalla y corroborar la procedencia de los datos.

Criterios de Aceptación:

 Diseño adaptable con grilla CSS que ajusta las tarjetas automáticamente a pantallas móviles y de escritorio.
 Insignia superior y pie de página con atribución y enlace directo al dataset bign-27m7 de datos.gov.co (Ministerio de Relaciones Exteriores).
