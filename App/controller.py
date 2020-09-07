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

import config as cf
from App import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def initcatalog():
    catalog=model.newCatalog()
    return catalog
# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadData(catalog,moviesCastingFile,moviesDetailsFile):
    loadmoviesCastingRaw(catalog,moviesCastingFile)
    loadmoviesDetailsCleaned(catalog,moviesDetailsFile)
def loadmoviesCastingRaw(catalog,moviesfile):
    movies= cf.data_dir + moviesfile
    input_file= csv.DictReader(open(moviesfile, encoding='utf-8-sig'))
    for movie in input_file:
        model.addMovieCasting(catalog,movie)
def loadmoviesDetailsCleaned(catalog,moviesfile):
    movies=cf.data_dir+moviesfile
    input_file=csv.DictReader(open(moviesfile,encoding='utf-8-sig'))
    for movie in input_file:
        model.addMovieDetails(catalog,movie)
# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def moviesSize(catalog):
    return model.moviesSize(catalog)
def moviesIdsSize(catalog):
    return model.MoviesIdsSize(catalog)
def actorsSize(catalog):
    return model.actorsSize(catalog)
def genresSize(catalog):
    return model.genresSize(catalog)
def productionCompaniesSize(catalog):
    return model.productionCompaniesSize(catalog)
def countriesSize(catalog):
    return model.countriesSize(catalog)
def voteAverageSize(catalog):
    return model.voteAverageSize(catalog)
def voteCountSize(catalog):
    return model.voteCountSize(catalog)
def getMoviesByDirector(catalog):
    return model.moviesByDirector(catalog)
def getMoviesByActor(catalog):
    return model.moviesByActor(catalog)
def getMoviesByProductionCompanies(catalog):
    return model.moviesByProductionCompany(catalog)
def getMoviesByCountry(catalog):
    return model.moviesByCountry(catalog)
def getMoviesByGenre(catalog):
    return model.moviesByGenre(catalog)



    
