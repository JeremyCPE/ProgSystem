#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
int main (int argc, char* argv[]) { 
char *f[20];
int status, i, j= 0;
for (i=1 ; i<=argc; i++) { 
  if ( fork()==0) {
  execlp (argv[i], argv[i], NULL);
  exit(3);
  }
wait(&status);
  if (WIFEXITED(status)) { //Check si problème lors de l'execution du fils de pute 
  printf("Terminaison normale du processus fils.\n");
    if( WEXITSTATUS(status)== 3) {  
    //récupérer le code de retourf[j] = (char *)malloc(strlen(argv[i])+1);
    strcpy(f[j],argv[i]); //strcpy(s1, s2) : copie la chaîne de caractère s2 dans s1
    j++;
    }
  }
}
if(j != 0){
  for (i=0; i<j; i++){
    printf("%s \n", f[i]);
  }
}
return 0;

}