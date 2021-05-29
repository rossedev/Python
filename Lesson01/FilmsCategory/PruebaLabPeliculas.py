from dominio.Pelicula import Film
from servicio.CatalogoPelicula import FilmCategory
import os

option = None

while option != 4:
    print("Choose in the Menu\n" +
          "1. Add film\n" +
          "2. List films\n" +
          "3. Remove films\n" +
          "4. Exit")

    option = int(input("Enter the number: "))

    if option == 1:
        nameFilm = input("Enter the name film: ")
        film = Film(nameFilm)
        FilmCategory.addFilm(film)

    elif option == 2:
        FilmCategory.listFilms()
    elif option == 3:
        FilmCategory.remove()
    else:
        "incorrect, please try again"
else:
    "Exit the program"