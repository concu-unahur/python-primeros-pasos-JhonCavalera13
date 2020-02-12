import time
import threading
import logging
 
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class Contador:
  def iniciar(self):
    logging.info('INICIAR()')
    self.inicio = time.perf_counter()

  def finalizar(self):
    self.fin = time.perf_counter()

  def imprimir(self):
    logging.info(f'Pasaron {round(self.fin - self.inicio, 2)} segundos')

  def dormir(self):
    time.sleep(1)


contador = Contador()

# ejemplo clásico secuencial
contador.iniciar()

contador.dormir()
contador.dormir()

contador.finalizar()
contador.imprimir()

# ejemplo con threads
contador.iniciar()

t1 = threading.Thread(target=contador.dormir)
t2 = threading.Thread(target=contador.dormir)

t1.start()
t2.start()

contador.finalizar()
contador.imprimir()

# ejemplo con threads, pero esperando que terminen
contador.iniciar()

t1 = threading.Thread(target=contador.dormir)
t2 = threading.Thread(target=contador.dormir)
t3 = threading.Thread(target=contador.dormir)
t4 = threading.Thread(target=contador.dormir)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

contador.finalizar()
contador.imprimir()

# Pregunta: ¿por qué los segundos que pasaron son 2, 0 y 1 respectivamente?
# Pregunta: ¿cuántos hilos o threads hay en cada caso?
# Pregunta: los últimos dos ejemplos tienen 3 threads cada uno, ¿cuál sería la diferencia entonces?
