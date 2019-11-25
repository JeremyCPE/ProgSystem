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

#define CLE_SEM1 1
#define CLE_SEM2 2

void rdv_un (){
    printf("Exécution de la fonction du processus 1\n");
}

void rdv_deux (){
    printf("Exécution de la fonction du processus 2\n");
}

int main() {
  int processus;
  int semP1, semP2;
  semP1 = sem_create(CLE_SEM1,0);
  semP2 = sem_create(CLE_SEM2,0);
  processus = fork();
  if(processus==0){
    sleep(2);
    V(semP2);
    printf("\nJe suis le processus fils P2, je viens de me réveiller\n");
    P(semP1);
    printf("\nIci P2 synchronisé avec P1\n");
    sem_delete(semP1);
    rdv_deux();
    exit(0);
  } else {
    sleep(4);
    V(semP1);
    printf("\nJe suis le processus père P1, je viens de me réveiller\n");
    P(semP2);
    printf("\nIci P1 synchronisé avec P2\n");
    sem_delete(semP2);
    rdv_un();
  }
  return 0;
}

/*
ESSAIS INFRUCTUEUX :
CODE MAIN :
#define CLE 1
int sem;

CODE PS FILS:
  sleep(4);
  if(semget(CLE,1,IPC_CREAT|IPC_EXCL|0666)==-1){
    printf("\nJe suis le processus fils P2, je suis le 1er au rdv\n");
    P(sem);
    rdv_un();
    sem_delete(sem);
  }else{
    printf("\nJe suis le processus fils P2, j'arrive également au rdv\n");
    V(sem);
  }
  exit(0);

CODE PS PERE :
sleep(2);
if(semget(CLE,1,IPC_CREAT|IPC_EXCL|0666)==-1){
  printf("\nJe suis le processus père P1, je suis le 1er au rdv\n");
  P(sem);
  rdv_deux();
  sem_delete(sem);
}else{
  printf("\nJe suis le processus fils P1, j'arrive également au rdv\n");
  V(sem);
}





*/
