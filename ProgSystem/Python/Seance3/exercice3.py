# Calcul de PI par la loi de monte carlo (et esperence c'est exactement la meme formule)
import multiprocessing as mp
import random, time
# calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes)
start_time = time.time()

def frequence_de_hits_pour_n_essais(nb_iteration, count, lock):
    for i in range(nb_iteration):
        x = random.random()
        y = random.random()
     # si le point est dans l’unit circle
        if x * x + y * y <= 1: 
            with lock:
                count.value += 1

if __name__ == "__main__" :
    # Nombre d’essai pour l’estimation
    nb_total_iteration = 1000000
    count = mp.Value('i', 0) #Value (int) partagée entre les process
    #nb_hits=frequence_de_hits_pour_n_essais(nb_total_iteration)
    nb_process=1
    nb_iteration =int(nb_total_iteration/nb_process)  #Chaque Process aura nb_iteration a faire
    lock=mp.Lock() #Verrou
    mes_process = [0 for i in range(nb_process)]
    for i in range(nb_process):
        mes_process[i] = mp.Process(target=frequence_de_hits_pour_n_essais, args= (nb_iteration,count,lock))
        mes_process[i].start()
    for i in range(nb_process): mes_process[i].join() #Attendre la fin
    print("Nombre de Process : ",nb_process)
    print("Valeur estimée Pi par la méthode  : ", 4 * count.value / nb_total_iteration)
    print("Temps d'execution : ", time.time() - start_time)



