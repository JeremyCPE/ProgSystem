#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
int main (int argc, char* argv[]) { 
int k,ret;

for (k=0 ; k<3; k++) {
  ret = fork();
  printf("Je suis le processus : %d, \n Mon père est %d, \n retour : %d \n",getpid(),getppid(),ret);
  exit(0);
}

return 0;

}
