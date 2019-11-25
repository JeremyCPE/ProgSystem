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
#include "p1.h"
#include "p2.h"
#include "rendez_vous.h"

#define CLE 1

void p1() {
int sem;
  printf("\n \n Je suis Amaury plutot charmante et j'attends mon gentleman (Jeremy) \n pour notre rendez-vous au cinéma voir LE JOKER \n");
  printf("Creation du sémaphore d'identificateur %d\n",sem);
  sem = sem_create(CLE,0);
  V(sem);
  while(!synchroP2());
}