"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------



# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================

def newCatalog(sizes):
    """ Inicializa el catálogo de libros
    Crea una lista vacia para guardar todos los libros
    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion
    Retorna el catalogo inicializado.
    """
    catalog = {'movies': None,
               'moviesIds': None,
               'directors': None,
               'votesAverage': None,
               'actors': None,
               'productionCompany': None,
               'genre': None,
               'country': None}

    catalog['movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['moviesIds'] = mp.newMap(lt.getElement(sizes,0)),
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['directors'] = mp.newMap(lt.getElement(sizes,1),
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareDirectorsByName)
    catalog['votesAverage'] = mp.newMap(lt.getElement(sizes,2),
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareVotesAverage)
    catalog['actors'] = mp.newMap(lt.getElement(sizes,3),
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compareActorsByName)
    catalog['productionCompany'] = mp.newMap(lt.getElement(sizes,4),
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareProductionCompany)
    catalog['genres'] = mp.newMap(lt.getElement(sizes,5),
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareGenres)
    catalog['country'] = mp.newMap(lt.getElement(sizes,6),
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareCountry)
    atalog['votesCount'] = mp.newMap(lt.getElement(sizes,7),
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareCountry)

def addMovie(catalog, movie):
    lt.addLast(catalog['movies'], movie)
    mp.put(catalog['moviesIds'], movie['id'], movie)
    mp.put(catalog['directors'], movie['id'], movie)
    mp.put(catalog['votesAverage'], movie['id'], movie)
    mp.put(catalog['actors'], movie['id'], movie)
    mp.put(catalog['productionCompany'], movie['id'], movie)
    mp.put(catalog['genres'], movie['id'], movie)
    mp.put(catalog['country'], movie['id'], movie)
    mp.put(catalog['votesCount'], movie['id'], movie)

def moviesByDirector(directorName):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    director = {'name': "", "movies": None,  "average_rating": 0}
    director['name'] = directorName
    director['movies'] = lt.newList('SINGLE_LINKED', compareDirectorsByName)
    return director

def getmoviesByDirector(catalog, directorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    director = mp.get(catalog['directors'], directorname)
    if director:
        return me.getValue(director)
    return None

def getmoviesByActor(catalog, actorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    actor = mp.get(catalog['actors'], authorname)
    if author:
        return me.getValue(author)
    return None

def moviesByCountry(countryName):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    country = {'name': "", "movies": None}
    country['name'] = countryName
    country['movies'] = lt.newList('SINGLE_LINKED', compareCountry)
    return country

def moviesByProductionCompany(companyName):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    company = {'name': "", "movies": None}
    company['name'] = companyName
    company['movies'] = lt.newList('SINGLE_LINKED', compareProductionCompany)
    return company

def moviesByProductionAuthor(authorName):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    author = {'name': "", "books": None,  "average_rating": 0}
    author['name'] = authorName
    author['books'] = lt.newList('SINGLE_LINKED', compareActorsByName)
    return author

def moviesByGenre(genreName):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    genre = {'name': "", "movies": None}
    genre['name'] = genreName
    genre['movies'] = lt.newList('SINGLE_LINKED', compareGenres)
    return genre

def compareMoviesIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (int(id1) == int(id2)):
        return 0
    elif int(id1) > int(id2):
        return 1
    else:
        return -1

def compareVotesCount(vote1, vote2):
    """
    Compara dos vote count de libros
    """
    if (int(vote1) == int(vote2)):
        return 0
    elif int(vote1) > int(vote2):
        return 1
    else:
        return -1

def compareMapMoviesIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareDirectorsByName(keyname, director):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    directentry = me.getKey(director)
    if (keyname == directentry):
        return 0
    elif (keyname > directentry):
        return 1
    else:
        return -1

def compareVotesAverage(Avr1,Avr2):
    if (int(Avr1) == int(Avr2)):
        return 0
    elif (int(Avr1) > int(Avr2)):
        return 1
    else:
        return -1

def compareActorsByName(name1, name2):
    if (name1 == name2):
        return 0
    elif (name1 > name2):
        return 1
    else:
        return -1

def compareProductionCompany(company1, company2):
    if (company1 == company2):
        return 0
    elif (company1 > company2):
        return 1
    else:
        return 0

def compareGenres(genre1, genre2):
    if (genre1 == genre2):
        return 0
    elif (genre1 > genre2):
        return 1
    else:
        return 0 
    return catalog

def compareCountry(country1, country2):
    if (country1 == country2):
        return 0
    elif (country1 > country2):
        return 1
    else:
        return 0 
    return catalog
