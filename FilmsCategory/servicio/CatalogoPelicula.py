import os

class FilmCategory:
    filmRoute = "films.txt"

    @staticmethod
    def addFilm(film):
        try:
            file = open(FilmCategory.filmRoute, "a")
            file.write(film.__str__())
        except Exception as e:
            print(e)
        finally:
            file.close()

    @staticmethod
    def listFilms():
        try:
            file = open(FilmCategory.filmRoute, "r")
            print("Film Category: ")
            print(file.read())
        except Exception as e:
            print(e)
        finally:
            file.close()

    @staticmethod
    def remove():
        try:
            os.remove(FilmCategory.filmRoute)
            print("Yeah! Delete film with name, " + FilmCategory.filmRoute)
        except Exception as e:
            print(e)

2