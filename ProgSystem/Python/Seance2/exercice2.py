 #Exercice 2
#Six taches sequentielles A,B,C,D,E et F
#Tache A doit préceder les taches B, C D
#B et C doivent preceder la tache E
#D et E doivent preceder la tache F
import multiprocessing as mp
import sys, time, random

def processA(s):
        print("Je suis le process A et j'attends 5 sec")
        time.sleep(5)
        print("Je suis le process A et je génère 3 jetons")
        s.release()
        s.release()
        s.release()
        sys.exit(0)
def processB(s,s2):
        print("Je suis le process B ")
        s.acquire()
        print("Je suis le process B et je vais génèrer 1 jeton dans 5 sec ")
        time.sleep(5)
        s2.release()
        sys.exit(0)
def processC(s,s2):
        print("Je suis le process C")
        s.acquire()
        print("Je suis le process C et je vais génèrer 1 jeton dans 5 sec")
        time.sleep(5)
        s2.release()
        sys.exit(0)
def processD(s,s3):
        print("Je suis le process D")
        s.acquire()
        print("Je suis le process D et je vais generer 1 jeton dans 5 sec")
        time.sleep(5)
        s3.release()
        sys.exit(0)

def processE(s2,s3):
        print("Je suis le process E")
        s2.acquire()
        s2.acquire()
        print("Je suis le process E et je vais generer 1 jeton dans 5 sec")
        time.sleep(5)
        s3.release()
        sys.exit(0)

def processF(s3):
        print("Je suis le process F")
        s3.acquire()
        s3.acquire()
        print("Je suis le process F et je suis DEBLOQUE")
        sys.exit(0)

sem = mp.Semaphore(0)
sem2 = mp.Semaphore(0)
sem3 = mp.Semaphore(0)
pA = mp.Process(target = processA, args =(sem,))
pB = mp.Process(target = processB, args =(sem,sem2,))
pC = mp.Process(target = processC, args =(sem,sem2,))
pD = mp.Process(target = processD, args =(sem,sem3,))
pE = mp.Process(target = processE, args =(sem2,sem3,))
pF = mp.Process(target = processF, args =(sem3,))
pA.start()
pB.start()
pC.start()
pD.start()
pE.start()
pF.start()
pA.join()
pB.join()
pC.join()
pD.join()
pE.join()
pF.join()
sys.exit(0)