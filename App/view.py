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

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

listDetails_s = "Data/themoviesdb/SmallMoviesDetailsCleaned.csv"
listDetails_l = "Data/themoviesdb/AllMoviesDetailsCleaned.csv"
listCasting_s = "Data/themoviesdb/MoviesCastingRaw-small.csv"
listCasting_l = "Data/themoviesdb/AllMoviesCastingRaw.csv"
 
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
    print("1- Inicializar catálogo")
    print("2- Cargar información del catálogo")
    print("3- Descubrir productoras de cine")
    print("4- Conocer a un director")
    print("5- Conocer a un actor")
    print("6- Entender un género de cine")
    print("7- Encontrar películas por país")
    print("8- (Beta) Probar view.py")
    print("0- Salir de la aplicación") 

def main():
    while True:
    printMenu()
    inputs = int(input('Selecciona una opción para continuar'))
    if len(inputs) > 0:
        if inputs == 1:
            continuar == True
            while continuar == True:
                menuApp()
                opcion = int(input("Digita la opción que deseas ejecutar: "))
                if opcion == 1:
                    print("Inicializando Catálogo ....")
                    # cont es el controlador que se usará de acá en adelante
                    cont = ctrl.initCatalog()

                elif opcion == 2:
                    print("Cargando información de los archivos .....")
                    menuApp()
                    tamaño = int(input("Digita el tamaño de los archivos CSV: "))
                    if tamaño == 1:
                        ctrl.loadData(cont, listDetails_s,listCasting_s)
                        print('Películas (detalles) cargadas: ' + str(ctrl.listDetails_s(cont)))
                        print('Películas (Casting) cargadas: ' + str(ctrl.listCasting_s(cont)))
                    elif tamaño == 2:
                        ctrl.loadData(cont, listDetails_l,listCasting_l)
                        print('Películas (detalles) cargadas: ' + str(ctrl.listDetails_l(cont)))
                        print('Películas (Casting) cargadas: ' + str(ctrl.listCasting_l(cont)))
                    else:
                        print("Opción inválida.....")

                elif opcion == 3:
                    print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")

                elif opcion == 4:
                    print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")

                elif opcion == 5:
                    print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")
                
                elif opcion == 6:
                    print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")
            
                elif opcion == 7:
                    print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")
        
                elif opcion == 8:
                    print("Aún estamos desarrollando el funcionamiento de este requerimiento. Vuelve pronto :3")
                    
                else:
                    sys.exit(0)
sys.exit(0)
