#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
  int main(int argc, char *argv[]) {
   
    int fils1, fils2, fils3, fils4, tube[2];
    unsigned char buffer[256];
    pipe(tube);
    fils1 = fork();
    if(fils1==0){
      //Fils commande wc
      close(tube[1]);
      dup2(tube[0],0);
      close(tube[0]);
      execlp("wc","wc",NULL);

    } 
    else{
      //Père commande cat Fichier
      //Suite programme sort < > bordel là
      close(tube[0]);
      dup2(tube[1],1);
      close(tube[1]);
      execlp ("cat", "cat", "monFichier",NULL);   

    
      
    }
    
  return 0;

  }