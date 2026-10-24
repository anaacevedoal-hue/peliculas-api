# API REST de películas

API REST sencilla desarrollada con Flask. Incluye un catálogo de películas de ejemplo y permite consultarlo o buscar películas por nombre.

## Requisitos

- Python 3.10 o superior
- pip

## Instalación y ejecución

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python peli.py
```

La API se inicia en `http://127.0.0.1:5000`.

## Endpoints

| Método | Ruta | Descripción |
| --- | --- | --- |
| GET | `/` | Muestra el índice HTML de la API y enlaces de ejemplo. |
| GET | `/peliculas` | Devuelve el catálogo completo en formato JSON. |
| GET | `/peliculas?q=matrix` | Busca películas cuyo nombre contiene el texto indicado. |

### Ejemplos

Consultar todas las películas:

```text
http://127.0.0.1:5000/peliculas
```

Buscar películas por nombre:

```text
http://127.0.0.1:5000/peliculas?q=matrix
```

Cada película contiene estos campos:

```json
{
  "nombre": "Matrix",
  "puntuacion_imdb": 8.7,
  "duracion": 136,
  "genero": "Ciencia ficción",
  "director": "Lana y Lilly Wachowski"
}
```

`duracion` está expresada en minutos. Los datos se guardan en una lista dentro de `peli.py`; al reiniciar la aplicación, cualquier cambio realizado en ejecución se pierde.
