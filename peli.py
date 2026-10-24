from flask import Flask, jsonify, render_template_string, request, url_for

app = Flask(__name__)

peliculas = [
    {
        "nombre": "El padrino",
        "puntuacion_imdb": 9.2,
        "duracion": 175,
        "genero": "Drama",
        "director": "Francis Ford Coppola",
    },
    {
        "nombre": "Cadena perpetua",
        "puntuacion_imdb": 9.3,
        "duracion": 142,
        "genero": "Drama",
        "director": "Frank Darabont",
    },
    {
        "nombre": "Matrix",
        "puntuacion_imdb": 8.7,
        "duracion": 136,
        "genero": "Ciencia ficción",
        "director": "Lana y Lilly Wachowski",
    },
    {
        "nombre": "El caballero oscuro",
        "puntuacion_imdb": 9.0,
        "duracion": 152,
        "genero": "Acción",
        "director": "Christopher Nolan",
    },
    {
        "nombre": "Pulp Fiction",
        "puntuacion_imdb": 8.9,
        "duracion": 154,
        "genero": "Crimen",
        "director": "Quentin Tarantino",
    },
    {
        "nombre": "Forrest Gump",
        "puntuacion_imdb": 8.8,
        "duracion": 142,
        "genero": "Drama",
        "director": "Robert Zemeckis",
    },
    {
        "nombre": "Origen",
        "puntuacion_imdb": 8.8,
        "duracion": 148,
        "genero": "Ciencia ficción",
        "director": "Christopher Nolan",
    },
    {
        "nombre": "Interstellar",
        "puntuacion_imdb": 8.7,
        "duracion": 169,
        "genero": "Ciencia ficción",
        "director": "Christopher Nolan",
    },
    {
        "nombre": "Parásitos",
        "puntuacion_imdb": 8.5,
        "duracion": 132,
        "genero": "Suspense",
        "director": "Bong Joon-ho",
    },
    {
        "nombre": "El viaje de Chihiro",
        "puntuacion_imdb": 8.6,
        "duracion": 125,
        "genero": "Animación",
        "director": "Hayao Miyazaki",
    },
    {
        "nombre": "La lista de Schindler",
        "puntuacion_imdb": 9.0,
        "duracion": 195,
        "genero": "Drama histórico",
        "director": "Steven Spielberg",
    },
    {
        "nombre": "12 hombres sin piedad",
        "puntuacion_imdb": 9.0,
        "duracion": 96,
        "genero": "Drama",
        "director": "Sidney Lumet",
    },
    {
        "nombre": "El señor de los anillos: La comunidad del anillo",
        "puntuacion_imdb": 8.9,
        "duracion": 178,
        "genero": "Fantasía",
        "director": "Peter Jackson",
    },
    {
        "nombre": "Uno de los nuestros",
        "puntuacion_imdb": 8.7,
        "duracion": 145,
        "genero": "Crimen",
        "director": "Martin Scorsese",
    },
    {
        "nombre": "Los siete samuráis",
        "puntuacion_imdb": 8.6,
        "duracion": 207,
        "genero": "Acción",
        "director": "Akira Kurosawa",
    },
    {
        "nombre": "Whiplash",
        "puntuacion_imdb": 8.5,
        "duracion": 106,
        "genero": "Drama",
        "director": "Damien Chazelle",
    },
    {
        "nombre": "Gladiator",
        "puntuacion_imdb": 8.5,
        "duracion": 155,
        "genero": "Acción",
        "director": "Ridley Scott",
    },
    {
        "nombre": "Titanic",
        "puntuacion_imdb": 7.9,
        "duracion": 195,
        "genero": "Romance",
        "director": "James Cameron",
    },
    {
        "nombre": "Avatar",
        "puntuacion_imdb": 7.9,
        "duracion": 162,
        "genero": "Ciencia ficción",
        "director": "James Cameron",
    },
    {
        "nombre": "Toy Story",
        "puntuacion_imdb": 8.3,
        "duracion": 81,
        "genero": "Animación",
        "director": "John Lasseter",
    },
    {
        "nombre": "Coco",
        "puntuacion_imdb": 8.4,
        "duracion": 105,
        "genero": "Animación",
        "director": "Lee Unkrich y Adrian Molina",
    },
    {
        "nombre": "Up",
        "puntuacion_imdb": 8.3,
        "duracion": 96,
        "genero": "Animación",
        "director": "Pete Docter",
    },
    {
        "nombre": "Joker",
        "puntuacion_imdb": 8.3,
        "duracion": 122,
        "genero": "Drama",
        "director": "Todd Phillips",
    },
    {
        "nombre": "El silencio de los corderos",
        "puntuacion_imdb": 8.6,
        "duracion": 118,
        "genero": "Suspense",
        "director": "Jonathan Demme",
    },
    {
        "nombre": "Regreso al futuro",
        "puntuacion_imdb": 8.5,
        "duracion": 116,
        "genero": "Ciencia ficción",
        "director": "Robert Zemeckis",
    },
    {
        "nombre": "Parque Jurásico",
        "puntuacion_imdb": 8.2,
        "duracion": 127,
        "genero": "Aventura",
        "director": "Steven Spielberg",
    },
    {
        "nombre": "Alien, el octavo pasajero",
        "puntuacion_imdb": 8.5,
        "duracion": 117,
        "genero": "Ciencia ficción",
        "director": "Ridley Scott",
    },
    {
        "nombre": "Amélie",
        "puntuacion_imdb": 8.3,
        "duracion": 122,
        "genero": "Romance",
        "director": "Jean-Pierre Jeunet",
    },
    {
        "nombre": "La vida es bella",
        "puntuacion_imdb": 8.6,
        "duracion": 116,
        "genero": "Drama",
        "director": "Roberto Benigni",
    },
    {
        "nombre": "El rey león",
        "puntuacion_imdb": 8.5,
        "duracion": 88,
        "genero": "Animación",
        "director": "Roger Allers y Rob Minkoff",
    },
    {
        "nombre": "Mad Max: Furia en la carretera",
        "puntuacion_imdb": 8.1,
        "duracion": 120,
        "genero": "Acción",
        "director": "George Miller",
    },
    {
        "nombre": "La La Land",
        "puntuacion_imdb": 8.0,
        "duracion": 128,
        "genero": "Musical",
        "director": "Damien Chazelle",
    },
    {
        "nombre": "El gran hotel Budapest",
        "puntuacion_imdb": 8.1,
        "duracion": 99,
        "genero": "Comedia",
        "director": "Wes Anderson",
    },
    {
        "nombre": "Infiltrados",
        "puntuacion_imdb": 8.5,
        "duracion": 151,
        "genero": "Crimen",
        "director": "Martin Scorsese",
    },
    {
        "nombre": "No es país para viejos",
        "puntuacion_imdb": 8.2,
        "duracion": 122,
        "genero": "Crimen",
        "director": "Joel y Ethan Coen",
    },
]


@app.route("/", methods=["GET"])
def home():
    ejemplo_peliculas = url_for("obtener_peliculas")
    ejemplo_busqueda = url_for("obtener_peliculas", q="matrix")
    return render_template_string(
        """<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>API de películas</title>
  </head>
  <body>
    <h1>Índice de endpoints</h1>
    <table>
      <thead>
        <tr>
          <th>Método</th>
          <th>Descripción</th>
          <th>Ruta</th>
          <th>Ejemplo de uso</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>GET</td>
          <td>Obtiene todas las películas o busca por nombre.</td>
          <td>/peliculas</td>
          <td>
            <a href="{{ ejemplo_peliculas }}">Ver todas las películas</a><br>
            <a href="{{ ejemplo_busqueda }}">Buscar películas con q=matrix</a>
          </td>
        </tr>
      </tbody>
    </table>
  </body>
</html>""",
        ejemplo_peliculas=ejemplo_peliculas,
        ejemplo_busqueda=ejemplo_busqueda,
    )


@app.route("/peliculas", methods=["GET"])
def obtener_peliculas():
    busqueda = request.args.get("q", "").strip().casefold()
    resultado = [
        pelicula
        for pelicula in peliculas
        if busqueda in pelicula["nombre"].casefold()
    ]
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
