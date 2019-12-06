#• On se donne une (grande) liste (ou array pour plus d’efficacité) initialisé à 1.
#• On calculera la somme de cette liste d’abord par un seul processus puis par plusieurs. On com-
#parera les temps de calculs respectifs.
import multiprocessing as mp
import os, time,math, random, sys

def somme(ma_ligne : int) : # ma_ligne commence à 0
    somme = 0
    for i in range(range_somme): # Lancer Nb_process processus
        somme+= tab_somme[i]
    print("Somme = " + str(somme))

if __name__ == "__main__" :

    Nb_process=2
    range_somme = 10000
    tab_somme = mp.Array("i",range_somme)  #Tableau Partagé de int
    tab_somme[:]= [random.randint(1,10000) for _ in range(range_somme) ] #Initialisés à NB ALEA
    mes_process = [0 for i in range(Nb_process)]
    for i in range(Nb_process): # Lancer Nb_process processus
            mes_process[i] = mp.Process(target=somme, args= (i,))
            mes_process[i].start()


