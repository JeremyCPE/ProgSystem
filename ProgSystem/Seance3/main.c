#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
  int main(int argc, char *argv[]) {
   
    int tube[2];
    unsigned char buffer[256];
    int i;
    
    printf("Création du tube \n");
    
    if(pipe(tube) != 0) {
    
      perror("Problème - création du tube \n");
      exit(3);
    }
    for(i=0; i<256; i++) buffer[i] = i;
    
    printf("Ecriture dans le tube \n");
    
    if(write(tube[1],"hello world",256) != 256) {
      perror("Problème - Ecriture dans le tube \n");
      exit(3);
    }
    printf("Lecture dans le tube \n");


    if(read(tube[0],buffer,256) != 256) {
      perror("Problème - Lecture depuis le tube \n");
      exit(3);
    }
    else {
    printf("Voici les caractères lus : %s \n", buffer);
    }
    
  return 0;

  }