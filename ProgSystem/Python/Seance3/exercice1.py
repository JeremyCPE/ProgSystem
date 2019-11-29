# Juin 2019
# Cours hippique
# Version très basique, sans mutex sur l’écran, sans arbitre, sans annoncer le gagant, ... ...

# Quelques codes d’échappement (tous ne sont pas utilisés)
CLEARSCR="\x1B[2J\x1B[;H" # Clear SCReen
CLEAREOS = "\x1B[J" # Clear End Of Screen
CLEARELN = "\x1B[2K" # Clear Entire LiNe
CLEARCUP = "\x1B[1J" # Clear Curseur UP
GOTOYX = "\x1B[%.2d;%.2dH" # (’H’ ou ’f’) : Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K" # effacer après la position du curseur
CRLF = "\r\n" # Retour à la ligne

# VT100 : Actions sur le curseur
CURSON = "\x1B[?25h" # Curseur visible
CURSOFF = "\x1B[?25l" # Curseur invisible

# VT100 : Actions sur les caractères affichables
NORMAL = "\x1B[0m" # Normal
BOLD = "\x1B[1m" # Gras
UNDERLINE = "\x1B[4m" # Souligné

# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK="\033[22;30m" # Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m" # Rouge
CL_GREEN="\033[22;32m" # Vert
CL_BROWN = "\033[22;33m" # Brun
CL_BLUE="\033[22;34m" # Bleu
CL_MAGENTA="\033[22;35m" # Magenta
CL_CYAN="\033[22;36m" # Cyan
CL_GRAY="\033[22;37m" # Gris

# "01" pour quoi ? (bold ?)
CL_DARKGRAY="\033[01;30m" # Gris foncé
CL_LIGHTRED="\033[01;31m" # Rouge clair
CL_LIGHTGREEN="\033[01;32m" # Vert clair
CL_YELLOW="\033[01;33m" # Jaune
CL_LIGHTBLU= "\033[01;34m" # Bleu clair
CL_LIGHTMAGENTA="\033[01;35m" # Magenta clair
CL_LIGHTCYAN="\033[01;36m" # Cyan clair
CL_WHITE="\033[01;37m" # Blanc

#−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
import multiprocessing as mp
import os, time,math, random, sys

keep_running=True # Fin de la course ?
global verrou
# Une liste de couleurs à affecter aléatoirement aux chevaux
lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY,\
CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN, CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]
def effacer_ecran() : print(CLEARSCR,end='')
def erase_line_from_beg_to_curs() : print("\033[1K",end='')
def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')
def move_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def en_couleur(Coul) : print(Coul,end='')
def en_rouge() : print(CL_RED,end='') # Un exemple !

# La tache d’un cheval
def un_cheval(ma_ligne : int) : # ma_ligne commence à 0
    col=1
    while col < LONGEUR_COURSE and keep_running :
        move_to(ma_ligne+1,col) # pour effacer toute ma ligne
        erase_line_from_beg_to_curs()
        en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
        #Mutex ici car plusieurs process peuvent use la ressource en mm temps
        verrou.acquire()
        print('8==3')
        verrou.release()
        col+=1
        time.sleep(0.1 * random.randint(1,5))
def un_arbitre(ma_ligne : int) : #Nb_process + 5
    move_to(25,1)
    print('En tete : ')
#−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
# La partie principale :
if __name__ == "__main__" :
    Nb_process=20
    mes_process = [0 for i in range(Nb_process)]
    
    verrou=mp.Lock()
    LONGEUR_COURSE = 100
    effacer_ecran()
    curseur_invisible()
    position = mp.Array(Nb_process)

    for i in range(Nb_process): # Lancer Nb_process processus
        mes_process[i] = mp.Process(target=un_cheval, args= (i,))
        mes_process[i].start()
    arbitre = mp.Process(target=un_arbitre,args=(i,)) 
    arbitre.start()
    move_to(Nb_process+10, 1)
    print("tous lancés")
    
    for i in range(Nb_process): mes_process[i].join()
    
    move_to(24, 1)
    curseur_visible()
    print("Fini")