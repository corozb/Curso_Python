import requests
from bs4 import BeautifulSoup
import urllib.request


def run(): #Vamos a pasar entre cada hoja, obtener las imagenes y guardar de forma local
    for i in range(1,6):
        response=requests.get('https://xkcd.com/{}'.format(i)) #pasar entre hojas
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic') #url de la imagen

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1] #Guardar con el nombre original de la página
        print('Descargando imagen {}'.format(image_name))
        urllib.request.urlretrieve('https:{}'.format(image_url), image_name)


if __name__=='__main__':
    run()
