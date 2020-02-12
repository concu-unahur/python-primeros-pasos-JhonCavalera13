import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaphore = threading.Semaphore(0)

total = 0
def sumarUno():
    global total
    try:
        total += 1
        logging.info('sumar uno')
    finally:
        semaphore.release()
    

def multiplicarPorDos():
    global total

    try:    
        semaphore.acquire()
        total *= 2
        logging.info('multiplicar por dos')
    finally:
        semaphore.release()



""" threadSumarUno = threading.Thread(target=sumarUno, name='Desde SumarUno()')
threadMultiplicarPorDos = threading.Thread(target=multiplicarPorDos, name='Desde SumarUno()') """

logging.info(total)

""" lock.acquire()
threadMultiplicarPorDos.start()
threadSumarUno.start()
logging.info(total) """

""" logging.info('Quedan4')
semaphore.acquire()
logging.info('Quedan3')
semaphore.acquire()
logging.info('Quedan2')
semaphore.acquire()
logging.info('Quedan1')
semaphore.acquire()
logging.info('Quedan0') """

threadSumarUno = threading.Thread(target=sumarUno, name='Desde SumarUno()')
threadMultiplicarPorDos = threading.Thread(target=multiplicarPorDos, name='Desde SumarUno()')

threadMultiplicarPorDos.start()
threadSumarUno.start()

threadMultiplicarPorDos.join()

logging.info(total)
