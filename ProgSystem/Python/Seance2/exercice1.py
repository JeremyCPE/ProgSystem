import os,sys,random
import multiprocessing as mp

# Valeur d'arrêt des boucles
fin = -1

# Fais la somme du contenu de q
# typeSomme definit l'affichage du résultat final
def somme(q,typeSomme):
    somme = 0
    while True:
        v = q.get()
        if(v!=fin):
            somme+=v
        else:
            break
    if(typeSomme=="p"):
        print("Somme paire "+str(somme))
    else:
        print("Somme impaire "+str(somme))

# Trie une liste de nombre selon s'ils sont pairs/impairs
# Place chiffres pairs dans queue qPair
# Place chiffres impairs dans queue qImpair
def triLPLI(qPair, qImpair,donnes):
    for i in donnes:
        if (i%2==0):
            qPair.put(i)
        else :
            qImpair.put(i)
    qPair.put(fin)
    qImpair.put(fin)

# MAIN
#Longueur de la liste de chiffres
nbAlea = 10 #random.randint(0,100)
listAlea = []
random.seed()

#Ajoute nbAlea chiffres aléatoires à la liste
for i in range (0,nbAlea):
    listAlea.append(random.randint(0,100))
print(listAlea)

#Création des queues
qPair = mp.Queue()
qImpair = mp.Queue()

# PROCESS DE TI
processTri = mp.Process(target=triLPLI,args=(qPair,qImpair,listAlea))
processTri.start()
processTri.join()

# PROCESS DE SOMME
psSP = mp.Process(target=somme,args=(qPair,"p"))
psSI = mp.Process(target=somme,args=(qImpair,"i"))

psSP.start()
psSI.start()
qPair.close()
qImpair.close()
psSP.join()
psSI.join()




