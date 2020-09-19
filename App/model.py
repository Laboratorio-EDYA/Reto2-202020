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

def newCatalog(size,loadfactor):
    catalog = {'moviesDetails': None,
                'moviesCasting': None,
                'moviesIdsDetails': None,
                'moviesIdsCasting': None,
                'directors': None,
                'actors': None,
                'productionCompanies': None,
                'genres': None,
                'countries': None}

    catalog['moviesDetails'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['moviesCasting'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['moviesIdsDetails'] = mp.newMap(size,
                                maptype='CHAINING',
                                loadfactor=loadfactor,
                                comparefunction=compareMapMoviesIds)
    catalog['moviesIdsCasting'] = mp.newMap(size,
                                   maptype='CHAINING',
                                   loadfactor=loadfactor,
                                   comparefunction=compareMapMoviesIds)
    catalog['directors'] = mp.newMap(size,
                                   maptype='CHAINING',
                                   loadfactor=loadfactor,
                                   comparefunction=compareDirectorsByName)
    catalog['actors'] = mp.newMap(size,
                                  maptype='CHAINING',
                                  loadfactor=loadfactor,
                                  comparefunction=compareActorsByName)
    catalog['productionCompanies'] = mp.newMap(size,
                                 maptype='CHAINING',
                                 loadfactor=loadfactor,
                                 comparefunction=compareProductionCompany)
    catalog['genres'] = mp.newMap(size,
                                 maptype='CHAINING',
                                 loadfactor=loadfactor,
                                 comparefunction=compareGenres)
    catalog['countries'] = mp.newMap(size,
                                 maptype='CHAINING',
                                 loadfactor=loadfactor,
                                 comparefunction=compareCountry)
    return catalog

# Funciones para agregar informacion al catalogo

def addMovieDetails(catalog, movie):
    lt.addLast(catalog['moviesDetails'], movie)
    mp.put(catalog['moviesIdsDetails'], movie['id'], movie)

def addMovieCasting(catalog, movie):
    lt.addLast(catalog['moviesCasting'], movie)
    mp.put(catalog['moviesIdsCasting'], movie['id'], movie)

def addMovieByDirector(catalog,directorName,movie):
    directors = catalog['directors']
    existdirector = mp.contains(directors,directorName)
    if existdirector:
        entry = mp.get(directors, directorName)
        director = me.getValue(entry)
    else:
        director = NewDirector(directorName)
        mp.put(directors, directorName, director)
    lt.addLast(director['movies'], movie)

    direcavg = director['vote_average']
    movieavg = me.getValue(mp.get(catalog['moviesIdsDetails'],movie['id']))['vote_average']
    direcount = director['vote_count']
    moviecount = me.getValue(mp.get(catalog['moviesIdsDetails'],movie['id']))['vote_count']
    if (direcavg[0] == 0.0):
        director['vote_average'][0] = float(movieavg)
        director['vote_average'][1] = float(movieavg)
        director['vote_average'][2] = 1
    else:
        director['vote_average'][1] = direcavg[1] + float(movieavg)
        director['vote_average'][2] += 1
        director['vote_average'][0] =  director['vote_average'][1]/ director['vote_average'][2]
    if (direcount[0] == 0):
        director['vote_count'][0] = int(moviecount)
        director['vote_count'][1] = int(moviecount)
        director['vote_count'][2] = 1
    else:
        director['vote_count'][1] = direcount[1] + int(moviecount)
        director['vote_count'][2] += 1
        director['vote_count'][0] =  director['vote_count'][1]/ director['vote_count'][2]
    
def addMovieByCountry(catalog,countryName,movie):
    countries = catalog['countries']
    existcountry = mp.contains(countries,countryName)
    if existcountry:
        entry = mp.get(countries, countryName)
        country = me.getValue(entry)
    else:
        country = NewCountry(countryName)
        mp.put(countries, countryName, country)
    lt.addLast(country['movies'], movie)

def addMovieByProductionCompany(catalog,companyName,movie):
    companies = catalog['productionCompanies']
    existcompany = mp.contains(companies,companyName)
    if existcompany:
        entry = mp.get(companies, companyName)
        company = me.getValue(entry)
    else:
        company = NewProductionCompany(companyName)
        mp.put(companies, companyName, company)
    lt.addLast(company['movies'], movie)
    companyavg = company['vote_average']
    movieavg = movie['vote_average']
    if (companyavg[0] == 0.0):
        company['vote_average'][0] = float(movieavg)
        company['vote_average'][1] = float(movieavg)
        company['vote_average'][2] = 1
    else:
        company['vote_average'][1] = companyavg[1] + float(movieavg)
        company['vote_average'][2] += 1
        company['vote_average'][0] =  company['vote_average'][1]/ company['vote_average'][2]

def addMovieByGenre(catalog,genreName,movie):
    genres = catalog['genres']
    existgenre = mp.contains(genres,genreName)
    if existgenre:
        entry = mp.get(genres, genreName)
        genre = me.getValue(entry)
    else:
        genre = NewGenre(genreName)
        mp.put(genres, genreName, genre)
    lt.addLast(genre['movies'], movie)

    genrecount = genre['vote_count']
    moviecount = movie['vote_count']
    if (genrecount[0] == 0):
        genre['vote_count'][0] = int(moviecount)
        genre['vote_count'][1] = int(moviecount)
        genre['vote_count'][2] = 1
    else:
        genre['vote_count'][1] = genrecount[1] + int(moviecount)
        genre['vote_count'][2] += 1
        genre['vote_count'][0] =  genre['vote_count'][1]/ genre['vote_count'][2]

def addMovieByActor(catalog,actorName,movie):
    actors = catalog['actors']
    existactor = mp.contains(actors,actorName)
    if existactor:
        entry = mp.get(actors, actorName)
        actor = me.getValue(entry)
    else:
        actor = NewActor(actorName)
        mp.put(actors, actorName, actor)
    lt.addLast(actor['movies'], movie)
    actoravg = actor['vote_average']
    movieavg = me.getValue(mp.get(catalog['moviesIdsDetails'],movie['id']))['vote_average']
    if (actoravg[0] == 0.0):
        actor['vote_average'][0] = float(movieavg)
        actor['vote_average'][1] = float(movieavg)
        actor['vote_average'][2] = 1
    else:
        actor['vote_average'][1] = actoravg[1] + float(movieavg)
        actor['vote_average'][2] += 1
        actor['vote_average'][0] =  actor['vote_average'][1]/ actor['vote_average'][2]

# ==============================
# Funciones de consulta
# ==============================

def getmoviesByDirector(catalog, directorname):
    director = mp.get(catalog['directors'], directorname.lower())
    if director:
        return me.getValue(director)
    return None

def getmoviesByActor(catalog, actorname):
    actor = mp.get(catalog['actors'], actorname.lower())
    if actor:
        return me.getValue(actor)
    return None

def getmoviesByProductionCompany(catalog, companyname):
    company = mp.get(catalog['productionCompanies'], companyname.lower())
    if company:
        return me.getValue(company)
    return None

def getmoviesByGenres(catalog, genrename):
    genre = mp.get(catalog['genres'], genrename.lower())
    if genre:
        return me.getValue(genre)
    return None

def getmoviesByCountry(catalog, directorname):
    country = mp.get(catalog['countries'], directorname.lower())
    if country:
        return me.getValue(country)
    return None

# ==============================
# Funciones de Filtrado
# ==============================
    
def NewDirector(directorName):
    director = {'name': "", "movies": None, 'vote_average': [0.0,0.0,0], 'vote_count': [0,0,0]}
    director['name'] = directorName.lower()
    director['movies'] = lt.newList('ARRAY_LIST', compareDirectorsByName)
    return director

def NewCountry(countryName):
    country = {'name': "", "movies": None}
    country['name'] = countryName.lower()
    country['movies'] = lt.newList('ARRAY_LIST', compareCountry)

    return country

def NewProductionCompany(companyName):
    company = {'name': "", "movies": None, 'vote_average': [0.0,0.0,0]}
    company['name'] = companyName.lower()
    company['movies'] = lt.newList('ARRAY_LIST', compareProductionCompany)
    return company

def NewGenre(genreName):
    genre = {'name': "", "movies": None, 'vote_count': [0,0,0]}
    genre['name'] = genreName.lower()
    genre['movies'] = lt.newList('ARRAY_LIST', compareGenres)
    return genre

def NewActor(actorName):
    actor = {'name': "", "movies": None, 'vote_average': [0.0,0.0,0]}
    actor['name'] = actorName.lower()
    actor['movies'] = lt.newList('ARRAY_LIST', compareActorsByName)
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

def compareVotesCount(vote, entry):
    voteEntry = me.getKey(entry)
    if (int(vote) == int(voteEntry)):
        return 0
    elif int(vote) > int(voteEntry):
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

def compareDirectorsByName(director, entry):
    directorentry = me.getKey(entry)
    if (director == directorentry):
        return 0
    elif (director > directorentry):
        return 1
    else:
        return -1

def compareVotesAverage(avr,entry):
    avrentry = me.getKey(entry)
    if (int(avr) == int(avrentry)):
        return 0
    elif (int(avr) > int(avrentry)):
        return 1
    else:
        return -1

def compareActorsByName(name, entry):
    nameentry = me.getKey(entry)
    if (name == nameentry):
        return 0
    elif (name > nameentry):
        return 1
    else:
        return -1

def compareProductionCompany(company, entry):
    companyentry = me.getKey(entry)
    if (company == companyentry):
        return 0
    elif (company > companyentry):
        return 1
    else:
        return 0

def compareGenres(genre, entry):
    genreentry = me.getKey(entry)
    if (genre == genreentry):
        return 0
    elif (genre > genreentry):
        return 1
    else:
        return 0 

def compareCountry(country, entry):
    countryentry = me.getKey(entry)
    if (country == countryentry):
        return 0
    elif (country > countryentry):
        return 1
    else:
        return 0 

# ==============================
# Funciones de Comparacion
# ==============================

def moviesDetailsSize(catalog):
    return lt.size(catalog['moviesDetails'])

def moviesCastingSize(catalog):
    return lt.size(catalog['moviesCasting'])

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
    
# ==============================
# Funciones de los Requerimientos
# ==============================

def descubrirProductorasDeCine(catalog, nameCompany):
    try:
        company = getmoviesByProductionCompany(catalog, nameCompany)
        movies = company['movies']
        movies_avr = company['vote_average'][0]
        return (movies,movies_avr,lt.size(movies))
    except:
        return -1

def conocerUnActor(catalog, nameActor):
    try:
        actor = getmoviesByActor(catalog, nameActor)
        movies = actor['movies']
        movies_avr = actor['vote_average'][0]
        directors = {}
        movies_names = lt.newList('ARRAY_LIST')
        # SE HALLAN LOS NOMBRES DE LAS PELICULAS EN LA LISTA DETAILS
        movie = it.newIterator(movies)
        while it.hasNext(movie):
            current = it.next(movie)
            name = me.getValue(mp.get(catalog['moviesIdsDetails'],current['id']))['original_title']
            lt.addLast(movies_names,name)
        # SE ASIGNA EL NUMERO DE COLABORACIONES POR DIRECTOR CON EL ACTOR
        movie = it.newIterator(movies)
        while it.hasNext(movie):
            current = it.next(movie)
            if current['director_name'] not in directors:
                directors[current['director_name']] = 1
            else:
                directors[current['director_name']] += 1
        director = ['',0]
            # SE HALLA EL DIRECTOR CON MÁS COLABORACIONES CON EL ACTOR
        for i in directors:
            if directors[i] >= director[1]:
                director[0] = i
                director[1] = directors[i]
        return (movies_names,movies_avr,lt.size(movies),director[0])
    except:
        return -1