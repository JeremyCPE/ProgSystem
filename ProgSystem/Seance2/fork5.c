#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char* argv[]) { 
  int i,pid,status;
  int isCompilationOk = 1;
  char *nomCompil,buffer[10];
  
      for(i=1;i<argc;i++){
	if( fork()==0) {
	  printf("Processus à executer : %s \n", argv[i]);
	  execlp("gcc","gcc","-c",argv[i],NULL);
	  exit(404);
	//printf("\t%d : %s\n",i,argv[i]);
	}
	pid = wait(&status);
	printf("PID = %d \n",pid);
	if(WIFEXITED(status)) {
	  if(WEXITSTATUS(status) == 404){
	    isCompilationOk = 0;
	  }	  
	}
	  
      }
      
      if(isCompilationOk == 1){
	printf("C'est compilé, maintenant on fait le lien :D\n");
	    /*  for(i=1;i<argc;i++){
		if( fork()==0) {
		  printf("Processus à executer : %s \n", argv[i]);
		  printf("Dernier carac %c \n",(argv[i][(strlen(argv[i]-1))]));
		  sprintf(buffer,"sortie %d",i);
		  char *result = malloc(strlen("exec") + strlen(buffer) + 1);
		  strcpy(result, "exec");
		  strcat(result, buffer);
		  
		//printf("\t%d : %s\n",i,argv[i]);
		}
		pid = wait(&status);
		printf("PID = %d \n",pid);
	      }
	      */
	      argv[i+1] = "-o";
	      argv[i+2] = NULL;
	      execv("/bin/gcc",argv);
	
	
      }else{
	printf("Oh... Oh oh oh oh *boule noire* \n");
      }

return 0;

}