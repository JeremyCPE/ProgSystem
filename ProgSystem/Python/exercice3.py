import os, sys
from os import path
import time

link = []
if len(sys.argv) < 2 :
    print("Ce script est sans paramètres")
else :
    for arg in sys.argv[1 :]:
        if path.exists(arg) and arg.endswith('.c'):
            pid = os.fork()
            if pid == 0: 
                # fils
                print("Compilation du fichier ",arg)
                os.execlp("gcc","gcc","-c",arg)
            else: 
                # pere       
                ppid, status = os.waitpid(pid, 0)
                file_name = list(arg)
                file_name[-1] = 'o'
                link.append(file_name)
                print("wait returned, pid",pid, "with status",status )
        else:
            print("Le fichier", arg, " ne peut pas etre compilé \n")
    str1 = ''
    str2 = str1.join(link)
    print("Lien= ",str2)cd 

