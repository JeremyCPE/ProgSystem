 #Exercice 3
import multiprocessing as mp
import sys, time, random

"""
Un système est composé de deux taches T1 et T2 soumises a la contrainte de precedence
T1 < T2.Ces deux taches appartiennent a deux processus P1 et P2 différents qui doivent etre 
synchronisés => Le processus P2 doit retarder l'execution de la tache T2 jusqu'à ce que le premier
processus P1 termine la tache T1
"""

#with : fait un acquire au début et un release a la fin
def process1(verrou,stream):
        with verrou:
            stream.write("Je suis le P1, jexecute la Tache T1 \n")
            time.sleep(2)
            stream.write("Fin de la tache T1 \n")


def process2(verrou,stream):
        stream.write("Je suis le P2 \n")
        verrou.acquire()
        try:
            stream.write("Execution de la tache T2 \n")
        finally:
            verrou.release()


verrou = mp.Lock()
p1 = mp.Process(target = process1, args =(verrou, sys.stdout))
p2 = mp.Process(target = process2, args =(verrou, sys.stdout))

p1.start();p2.start();
p1.join();p2.join();