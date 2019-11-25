#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
  int main(int argc, char *argv[]) {
   
    int fils1, fils2, fils3, fils4, tube[2],fichier,tube2[2];
    unsigned char buffer[256];
    pipe(tube);
    pipe(tube2);
    fils1 = fork();
    if(fils1==0){
      //Fils commande wc
      close(tube[1]);
      dup2(tube[0],0);
      close(tube[0]);
      execlp("grep","grep","chaine",NULL);

    }else{
      //Père commande cat Fichier
      //Suite programme sort < > bordel là
      close(tube[0]);
      dup2(tube[1],1);
      close(tube[1]);
      execlp ("sort", "sort", "monFichier",NULL); 
    }
  return 0;

  }