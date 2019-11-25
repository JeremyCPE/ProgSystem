import os,sys,random, time
import multiprocessing as mp

#Valeur de fin
fin = -1

#Fonction de dépôt dans la queue associée au processus
def depotQueue(q, sem):
    #On va déposer 5 valeurs dans la queue
    for i in range (0,5):
        donnee=random.randint(0,100)
        tpsDodo=random.randint(0,5)
        nomPs = mp.current_process().name
        print("Je suis "+str(nomPs)+" et j'attends "+str(tpsDodo)+"s avant de déposer "+str(donnee)+" dans ma queue")
        #Temps d'attente aléatoire avant le dépo
        time.sleep(tpsDodo)
        q.put(donnee)
        #On ajoute un jeton dans le sémaphore associé au tube
        sem.release()
    #Fin d'écriture pour boucler le programme
    q.put(fin)
    sem.release()


def priseQueue(q, sem):
    #On récupère le nom du processus courant
    nomPs = mp.current_process().name
    while(True):
        #Récupération d'un jeton dans le sémaphore de l'autre processus
        print("Je suis "+str(nomPs)+" et j'essaye de prendre dans ma queue (attente synchro)")
        sem.acquire()
        #Une fois jeton, dispo, on récupère la valeur dans la queue associée au ps
        value = q.get()
        if(value!=fin):
            print("Je suis "+str(nomPs)+" et je viens de prendre "+ str(value) + " de ma queue")
        else:
            break

# MAIN
random.seed()

#Création des queues
q1 = mp.Queue()
q2 = mp.Queue()
#Création des sémaphores
semConsoQ1 = mp.Semaphore(0)
semConsoQ2 = mp.Semaphore(0)

# PROCESS DE DEPOT
p1 = mp.Process(target=depotQueue,args=(q1,semConsoQ1))
p2 = mp.Process(target=depotQueue,args=(q2,semConsoQ2))

# PROCESS DE CONSOMMATION : Attention aux bons arguments de sémaphore!
c1 = mp.Process(target=priseQueue,args=(q1,semConsoQ2))
c2 = mp.Process(target=priseQueue,args=(q2,semConsoQ1))

p1.start()
p2.start()
c1.start()
c2.start()

q1.close()
q2.close()

p1.join()
p2.join()
c1.join()
c2.join()





