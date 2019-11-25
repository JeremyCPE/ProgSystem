#include <stdio.h>
#include <stdbool.h>
  int main(int nbarg, char **arg) {
    int i,j,k,l=0;
    bool isOk = true;
    extern char **environ;
    char *token;
    printf("%s \n",*(environ));
    printf("%d \n",**(environ));
    
    for(i=1;i<nbarg;i++) {
      //Compte le nombre de caractère
      for(j=0;arg[k][i]!='\0';j++)
      {
      }
	for(j=0;j<**(environ);j++) {
	     for(i=0;arg[k][i]!='\0';i++) {
	       printf("%c => %c",arg[k][i],environ[k][i]);
		  if(arg[k][i] != environ[k][i]) {
		    isOk = false;
		    break;
		  }

	      }	
	      if(isOk) {
		copyenv[l] = *(environ) + j;
		printf("%s",copyenv[l]);
		l++;
	      }
	      isOk=true;
	}
    }   
    
  }