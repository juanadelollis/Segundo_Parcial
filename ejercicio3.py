import requests

class Batmancola:
    def __init__(self):
        self.info = None
        self.pelis = []
        self.year = None
       
    def que_pelis(self):
        self.info = requests.get("https://fake-movie-database-api.herokuapp.com/api?s=batman")
        for movies in self.info.json()["Search"]:
            self.pelis.append(movies["Title"])
        print("La lista de peliculas es:")
        for movies in self.pelis:
            print("-", movies)
            
   
    def una_del(self, anio):
        self.info = requests.get("https://fake-movie-database-api.herokuapp.com/api?s=batman")
        for movies in self.info.json()["Search"]:
            if movies["Year"] == anio:
                self.year = movies["Title"]
                print("La pelicula para ese anio es: ", self.year)

        
        
b = Batmancola()
b.que_pelis()
b.una_del("2017")



#b. ¿Cuál es el dominio al que estamos consultando?

"""
El dominio al que estamos consultando es: fake-movie-database-api.herokuapp.com
"""

#c. Si esta fuera una aplicación REST ¿Cómo esperías que sea la ruta para obtener la información detallada 
#de la 1er película? 
"""
https://fake-movie-database-api.herokuapp.com/api?s=batman/search1

"""

#d. Describí las características que deben tener las computadoras que actúan como cliente en la 
#arquitectura web cliente-servidor

"""
La diferemcia de caracteristicas esta en el software. Es decir, las computadores que actuan como lcientes 
pueden tener memoria, red, procesadores mas potentes o no. Pero la diferencia es lo programatico, lo que 
efctivamente hace la maquina. 
Como las computadoras clientes comparten recursos, los piden, se caracterizan por ser de salida.ESto es porque 
se encargan de presentar/renderizar la respuesta al usuario. 
Detrás del cliente siempre hay un usuario que consume recursos.
Por eso los tipos de tecnologias detras son java, css, html, que son softwares que dialogan con le navegador.
"""