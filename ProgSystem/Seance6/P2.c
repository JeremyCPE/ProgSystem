#include <unistd.h>
#include <errno.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <stdbool.h>
#include "dijkstra.h"
#include "rendez_vous.h"
#include "p1.h"
#include "p2.h"
#define CLE 1

void p2() {
  int sem;
  printf("\n \n Je suis Jérémy, ce bel étalon, doté d'un braquemart que meme Jonny Sins \n en serait Jaloux, arrive à son rendez-vous pret à accompagner Amaury lors du visionnage de ce magnifique film réalisé par Todd Phillips \n");
  while(!synchroP1());
  sem = get_rendez_vous();
  printf("Jeremy, sem = %d",sem);
  P(sem);
  printf("Les deux tourteraux se sont rencontrés, le rendez-vous ne fait que commencer... ;) ;)\n");
  destroy_rendez_vous(sem);
  
}