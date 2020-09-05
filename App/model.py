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
from DISClib.DataStructures import listiterator as it
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def newCatalog(sizes):
    catalog = {'moviesDetails': None,
                'moviesCasting': None,
               'moviesIdsDetails': None,
               'moviesIdsCasting'
               'directors': None,
               'votesAverage': None,
               'actors': None,
               'productionCompanies': None,
               'genres': None,
               'countries': None}

    catalog['moviesDetails'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['moviesCasting'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['moviesIdsDetails'] = mp.newMap(lt.getElement(sizes,0)),
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['moviesIdsCasting'] = mp.newMap(lt.getElement(sizes,0)),
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
    catalog['productionCompanies'] = mp.newMap(lt.getElement(sizes,4),
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareProductionCompany)
    catalog['genres'] = mp.newMap(lt.getElement(sizes,5),
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareGenres)
    catalog['countries'] = mp.newMap(lt.getElement(sizes,6),
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareCountry)
    atalog['votesCount'] = mp.newMap(lt.getElement(sizes,7),
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareCountry)

# Funciones para agregar informacion al catalogo

def addMovieDetails(catalog, movie):
    lt.addLast(catalog['moviesDetails'], movie)
    mp.put(catalog['moviesIdsDetails'], movie['id'], movie)
    mp.put(catalog['votesAverage'], movie['vote_average'], movie)
    mp.put(catalog['productionCompanies'], movie['production_companies'], movie)
    mp.put(catalog['genres'], movie['genres'], movie)
    mp.put(catalog['countries'], movie['production_countries'], movie)
    mp.put(catalog['votesCount'], movie['vote_count'], movie)

def addMovieCasting(catalog, movie):
    lt.addLast(catalog['moviesCasting'], movie)
    mp.put(catalog['moviesIdsCasting'], movie['id'], movie)
    mp.put(catalog['directors'], movie['director'], movie)
    mp.put(catalog['actors'], movie['actor1_name'], movie)
    mp.put(catalog['actors'], movie['actor2_name'], movie)
    mp.put(catalog['actors'], movie['actor3_name'], movie)
    mp.put(catalog['actors'], movie['actor4_name'], movie)
    mp.put(catalog['actors'], movie['actor5_name'], movie)

# ==============================
# Funciones de consulta
# ==============================

def getmoviesByDirector(catalog, directorname):
    director = mp.get(catalog['directors'], directorname)
    if director:
        return me.getValue(director)
    return None

def getmoviesByActor(catalog, actorname):
    actor = mp.get(catalog['actors'], actorname)
    if actor:
        return me.getValue(actor)
    return None

def getmoviesByProductionCompany(catalog, companyname):
    company = mp.get(catalog['productionCompanies'], companyname)
    if company:
        return me.getValue(company)
    return None

def getmoviesByGenres(catalog, genrename):
    genre = mp.get(catalog['genres'], genrename)
    if genre:
        return me.getValue(genre)
    return None

def getmoviesByCountry(catalog, directorname):
    country = mp.get(catalog['countries'], directorname)
    if country:
        return me.getValue(country)
    return None

# ==============================
# Funciones de Filtrado
# ==============================

def filtrado(lst, catalog, criterio):
    
def moviesByDirector(directorName):
    director = {'name': "", "movies": None}
    director['name'] = directorName
    director['movies'] = lt.newList('SINGLE_LINKED', compareDirectorsByName)
    return director

def moviesByCountry(countryName):
    country = {'name': "", "movies": None}
    country['name'] = countryName
    country['movies'] = lt.newList('SINGLE_LINKED', compareCountry)

    return country

def moviesByProductionCompany(companyName):
    company = {'name': "", "movies": None}
    company['name'] = companyName
    company['movies'] = lt.newList('SINGLE_LINKED', compareProductionCompany)
    return company

def moviesByGenre(genreName):
    genre = {'name': "", "movies": None}
    genre['name'] = genreName
    genre['movies'] = lt.newList('SINGLE_LINKED', compareGenres)
    return genre

def moviesByActor(actorName):
    actor = {'name': "", "movies": None}
    actor['name'] = actorName
    actor['movies'] = lt.newList('SINGLE_LINKED', compareActorsByName)
    return actor

# ==============================
# Funciones de Comparacion
# ==============================

def compareMoviesIds(id1, id2):
    if (int(id1) == int(id2)):
        return 0
    elif int(id1) > int(id2):
        return 1
    else:
        return -1

def compareVotesCount(vote1, vote2):
    if (int(vote1) == int(vote2)):
        return 0
    elif int(vote1) > int(vote2):
        return 1
    else:
        return -1

def compareMapMoviesIds(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareDirectorsByName(director1, director2):
    if (director1 == director2):
        return 0
    elif (director1 > director2):
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

# ==============================
# Funciones de Comparacion
# ==============================

def moviesSize(catalog):
    return lt.size(catalog['movies'])

def MoviesIdsSize(catalog):
    return mp.size(catalog['moviesIds'])

def actorsSize(catalog):
    return mp.size(catalog['actors'])

def genresSize(catalog):
    return mp.size(catalog['genres'])

def productionCompaniesSize(catalog):
    return mp.size(catalog['productionCompanies'])

def countriesSize(catalog):
    return mp.size(catalog['countries'])

def voteAverageSize(catalog):
    return mp.size(catalog['voteAverage'])

def voteCountSize(catalog):
    return mp.size(catalog['voteCount'])
    