import os, sys

somme = 0
if len(sys.argv) < 2 :
    print("Ce script est sans paramètres")
else :
    for argument in sys.argv[1 :]:
        try:
            int(argument)
            if int(argument) < 0 or int(argument) > 20:
                raise ValueError 
            somme += int(argument)
        except ValueError:
            print("Erreur saisie")
            sys.exit(0)

    print("Moyenne = ", somme/(len(sys.argv) -1))