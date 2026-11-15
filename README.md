# TurismoCol 🇨🇴✈️

> **Lema**: Construye, aprende e innova.  
> Aplicación web desarrollada con Python y Django para la consulta ágil de países que no exigen visa de turismo a ciudadanos colombianos, utilizando datos abiertos del Estado.

---

## 1. Descubrimiento del Problema
- **Fuente de datos**: [Portal Nacional de Datos Abiertos de Colombia](https://www.datos.gov.co/Funci-n-p-blica/Paises-que-no-exigen-visa-de-turismo-a-colombianos/bign-27m7/about_data)  
- **Identificador oficial**: `bign-27m7`  
- **Entidad publicadora**: Función Pública / Cancillería - Ministerio de Relaciones Exteriores de Colombia.
- **Dato disponible**: Tabla oficial con países exentos de visa de turismo, días permitidos y condiciones migratorias.
- **Hipótesis de necesidad**: Muchos colombianos que desean viajar al exterior desconocen con certeza a qué destinos pueden viajar sin visa o cuántos días pueden permanecer, lo que genera desinformación o gastos innecesarios.
- **Beneficiario potencial**: Viajeros, estudiantes y familias colombianas que planean salidas internacionales.
- **Limitaciones de los datos**: Las condiciones de ingreso pueden variar por decisiones diplomáticas bilaterales; la aplicación informa que se debe validar siempre con el consulado respectivo.

---

## 2. Marco Ágil y Scrum

### 2.1. Objetivo del Producto (Product Goal)
Facilitar a los ciudadanos colombianos el acceso inmediato, claro y confiable a las condiciones de ingreso por turismo a países de todo el mundo sin necesidad de visa.

### 2.2. Objetivo del Sprint (Sprint Goal)
Construir y verificar un incremento web funcional que permita listar todos los destinos exentos de visa y realizar búsquedas por país o región, gestionando de forma predecible búsquedas sin coincidencias.

### 2.3. Definición de Terminado (Definition of Done - DoD)
Un incremento solo está terminado cuando:
- [x] Django inicia y la aplicación es navegable desde el navegador.
- [x] Se utilizan datos reales del dataset oficial `bign-27m7`.
- [x] Las búsquedas sin coincidencias o entradas vacías no rompen la aplicación y muestran mensajes claros.
- [x] Las pruebas automatizadas con `python manage.py test` pasan en verde (OK).
- [x] El código fue integrado mediante rama y Pull Request revisado.
- [x] El README permite la reproducción e instalación completa.
- [x] Los estados en GitHub Projects reflejan el avance real.

---

## 3. Instalación y Ejecución Local

### Prerrequisitos
- Python 3.10 o superior instalado.
- Git instalado.

### Pasos para ejecutar:
```bash
# 1. Clonar el repositorio
git clone https://github.com/alejosena2008-gif/Turismo_colombia.git
cd Turismo_colombia

# 2. Crear y activar entorno virtual
python -m venv venv
# En Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# En Windows (CMD):
venv\Scripts\activate.bat

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar pruebas automatizadas
python manage.py test

# 5. Iniciar servidor de desarrollo
python manage.py runserver
```
Abre en tu navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 4. Sprint Review y Retrospectiva

### Sprint Review (Revisión)
- Se entregó un recorrido funcional donde el usuario puede ver los países exentos de visa y filtrar en tiempo real por país o región.
- Se verificó el manejo de estados vacíos y la persistencia del dataset en formato CSV documentado.

### Sprint Retrospective (Retrospectiva)
- **¿Qué funcionó bien?**: Desacoplar la lectura de datos en `services.py` permitió mantener las vistas limpias y realizar pruebas rápidas y reproducibles.
- **¿Qué obstáculo afectó más?**: La normalización de tildes y nombres de columnas del CSV oficial requirió validaciones de fallback.
- **¿Qué acción concreta mejoraremos en el próximo ciclo?**: Integrar un comando para sincronización periódica directa contra la API Socrata de datos.gov.co.
