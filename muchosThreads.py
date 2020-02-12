import threading
import time
import logging
from clasesYfunciones import *
from tiempo import Contador


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread

cont = Contador()

lista = []

cont.iniciar()
for i in range(10):
    t1 = threading.Thread(target=dormir(1), name='loop')
    #t1 = UnThread(1)
    t1.start()
    t1.join() 
    lista.append(t1)
    
cont.finalizar()
cont.imprimir()

for thread in lista:
    
    logging.info(thread)



