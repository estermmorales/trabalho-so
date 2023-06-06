import threading
import random
import time

porcoes_tigela = 12

# Criacao dos semaforos
s_cozinheiro = threading.Semaphore(1)
s_canibal = threading.Semaphore(0)
s_comer = threading.Semaphore(1)  # Semáforo para controlar quantos canibais podem comer ao mesmo tempo

def canibal():
    global porcoes_tigela
    
    while True:
        s_canibal.acquire()
        s_comer.acquire()  
        for canibal in canibais:
            print(f"Canibal {canibais.index(canibal) + 1} comendo. Porções restantes: {porcoes_tigela - 1}")
            porcoes_tigela = porcoes_tigela - 1
            time.sleep(1.2)
            if porcoes_tigela <= 0:
                s_cozinheiro.release()
                time.sleep(2.5)
        
        s_comer.release()  # Libera o semáforo para permitir que outro canibal coma
        
def cozinheiro():
    global porcoes_tigela

    while True:
        s_cozinheiro.acquire()
        print(f"O cozinheiro adicionou 12 porções na tigela")
        porcoes_tigela = 12
        s_canibal.release()
        time.sleep(2.5)

# Instancia as threads canibal e cozinheiro
canibais = []
for i in range(0, 15):
    canibais.append(threading.Thread(target=canibal))
th_cozinheiro = threading.Thread(target=cozinheiro)

# Coloca as threads em execucao
for canibal in canibais:
    canibal.start()
th_cozinheiro.start()
