#include <sys/types.h>
#include <sys/ipc.h>
#include <unistd.h>
#include <errno.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <stdbool.h>
#include "dijkstra.h"
#include "p1.h"
#include "p2.h"

#define CLE 1
int SEM=0;

void main()
{
  printf("Serveur attente des deux clients pour servir un \n bon repas dans ce magnifique Cinéma (salle 1) \n");
  int sem;
  sem = sem_create(CLE,0);
  printf("Creation du sémaphore d'identificateur %d\n",sem);
  SEM = sem;
}

int get_rendez_vous()
{
return SEM;
}

_Bool synchroP1()
{
  _Bool sync = false;  
  if(SEM!=0) {
    sync=true;
  }
  return sync;
}

_Bool synchroP2()
{
  _Bool sync = false;  
  if(SEM==0) {
    sync=true;
  }
  return sync;
}

void set_rendez_vous(int sem)
{
SEM = sem;
}

void destroy_rendez_vous(int sem)
{
SEM = 0;
sem_delete(sem);
}