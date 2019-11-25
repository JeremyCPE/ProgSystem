import os,sys,random
import multiprocessing as mp

fin = -1

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

def triLPLI(qPair, qImpair,donnes):
    for i in donnes:
        if (i%2==0):
            qPair.put(i)
        else :
            qImpair.put(i)
    qPair.put(fin)
    qImpair.put(fin)

nbAlea = 10 #random.randint(0,100)
listAlea = []
random.seed()
for i in range (0,nbAlea):
    listAlea.append(random.randint(0,100))
print(listAlea)

qPair = mp.Queue()
qImpair = mp.Queue()
processTri = mp.Process(target=triLPLI,args=(qPair,qImpair,listAlea))
processTri.start()
processTri.join()
psSP = mp.Process(target=somme,args=(qPair,"p"))
psSI = mp.Process(target=somme,args=(qImpair,"i"))

psSP.start()
psSI.start()
qPair.close()
qImpair.close()
psSP.join()
psSI.join()




