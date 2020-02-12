import threading
import logging
import time
 
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

contador = 0

def sumarCinco():
  # necesario para poder usar la variable definida afuera
  global contador
  contador += 5

def sumarTres():
  # necesario para poder usar la variable definida afuera
  global contador
  contador += 3

logging.info('creando threads')

threadCinco = threading.Thread(target=sumarCinco, name='Sumar Cinco')
threadTres = threading.Thread(target=sumarTres, name='Sumar Tres')

threadTres.start()
threadCinco.start()

threadTres.join()
threadCinco.join()

logging.info(f'valor final {contador}')
