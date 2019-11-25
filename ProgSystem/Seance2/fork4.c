#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int pid, df1, df2;
   // char argv[5] = {"who","ps","ls","-l",NULL};
    
    if( fork()==0 ) {
   printf("WHO PID: %d \n",getpid());
    execlp("who","who",NULL);
    }
   
    if( fork()==0 ) { 
    printf("PS PID: %d \n",getpid());
    execlp("ps","ps",NULL);
    }
    if( fork()==0 ) { 
    printf("LS PID: %d \n",getpid());
    execlp("ls","ls","-l",NULL);
    }
    printf("Fin \n");
    return 0;
    }
    
    /* En executant plusieurs fois le résultat on remarque que le processus père et le processus fils s'executent simultanément  */