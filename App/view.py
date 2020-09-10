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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller as ctrl
assert config
from time import process_time
"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

listDetails_s = "themoviesdb/SmallMoviesDetailsCleaned.csv"
listDetails_l = "themoviesdb/AllMoviesDetailsCleaned.csv"
listCasting_s = "themoviesdb/MoviesCastingRaw-small.csv"
listCasting_l = "themoviesdb/AllMoviesCastingRaw.csv"
 
# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________
def menuData():
    print("Menú de opciones")
    print("1- Cargar archivos pequeños")
    print("2- Cargar archivos grandes")

def menuApp():
    print("\nBienvenido")
    print("1- Cargar información del catálogo")
    print("2- Descubrir productoras de cine")
    print("3- Conocer a un director")
    print("4- Conocer a un actor")
    print("5- Entender un género de cine")
    print("6- Encontrar películas por país")
    print("7- (Beta) Probar view.py")
    print("8- Salir de la aplicación") 

def main():
    while True:
        menuApp()
        opcion = input('Selecciona una opción para continuar: ')
        if len(opcion[0]) > 0:
            if int(opcion[0]) == 1:
                menuData()
                tamaño = int(input("Digita su selección para el tamaño de los archivos CSV: "))
                t1_start = process_time() #tiempo inicial
                if tamaño == 1:
                    size = 2000
                    print("Inicializando Catálogo ....")
                    # cont es el controlador que se usará de acá en adelante
                    cont = ctrl.initCatalog(size)
                    print("Cargando información de los archivos .....")
                    ctrl.loadData(cont,listCasting_s, listDetails_s,)
                    print('Películas (detalles) cargadas: ' + str(ctrl.moviesDetailsSize(cont)))
                    print('Películas (Casting) cargadas: ' + str(ctrl.moviesCastingSize(cont)))
                elif tamaño == 2:
                    size = 329046
                    print("Inicializando Catálogo ....")
                    # cont es el controlador que se usará de acá en adelante
                    cont = ctrl.initCatalog(size)
                    print("Cargando información de los archivos .....")
                    ctrl.loadData(cont,listCasting_l, listDetails_l)
                    print('Películas (detalles) cargadas: ' + str(ctrl.moviesDetailsSize(cont)))
                    print('Películas (Casting) cargadas: ' + str(ctrl.moviesCastingSize(cont)))
                else:
                    print("Opción inválida.....")
                t1_stop = process_time() #tiempo final
                print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")

            elif int(opcion[0]) == 2:
                print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")

            elif int(opcion[0]) == 3:
                print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")

            elif int(opcion[0]) == 4:
                print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")
                    
            elif int(opcion[0]) == 5:
                print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")
                
            elif int(opcion[0]) == 6:
                print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")
            
            elif int(opcion[0]) == 7:
                print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")
                        
            else:
                sys.exit(0)

main()
