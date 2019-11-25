#include <unistd.h>
#include <errno.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/ipc.h>

#include "dijkstra.h"

#define CLE 1

main() {
  int sem;
  sem = sem_create(CLE,0);
  printf("Creation du sémaphore d'identificateur %d\n",sem);
  if(fork()==0) {
    //son
    printf("Je suis le T1 (je ne suis pas un batiment, mais un traitement (T signifant Traitement)) \n");
    printf("Execution de la tache T1... \n");
    sleep(5);
    printf("Tache 1 fini... \n");
    V(sem);
    exit(0);
  
  }
  else {
  //parent
    printf("Je suis le T2 (je ne suis pas un batiment, mais un traitement (T signifant Traitement)) \n");
    P(sem);
    printf("Execution de la tache T2... \n");
    sem_delete(sem);
  }
}