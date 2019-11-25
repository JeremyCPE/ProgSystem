#include <unistd.h>
#include <time.h> 
#include <stdio.h>
#include <fcntl.h>
  int main(int argc, char *argv[]) {
 int i;
 int ran;
 int tube[2];
 char buffer[256]="0";
 int old=0;
 int max;
 
  if(argc < 2){

    printf("Erreur argument \n");
    return 0;
  }

  for(i=0;i<atoi(argv[1]);i++)  
  { 
    pipe(tube); //Create pipe
      if(fork() == 0) 
      {
	//Get old buffer
	old = atoi(buffer); //get old buffer
	
	if(i>0) //Comparer si on est au moins au 2eme fork
	{
	  close(tube[1]); /* close write side */
	  if(read(tube[0], buffer, 256) != 256)
	  {
		perror("Problème - Lecture dans le tube \n");
		exit(3);
	  }
	  if(atoi(buffer) > old) {
	  
	    max = atoi(buffer); 
	  }
	  else {
	    max = old;
	  }
	}
	
	//Create rand number
	srand(time(NULL) ^ (getpid()<<16));
	ran = rand()%5000;
	printf("[fils %d] pid %d valeur =  %d\n",getpid()-getppid(),getpid(),ran);
	sprintf(buffer, "%d", ran);
	close(tube[0]); //close read side

	if(write(tube[1],buffer,256) != 256) {
	      perror("Problème - Ecriture dans le tube \n");
	      exit(3);
	      }	
	      
	 close(tube[0]); /* close the pipe */
	
      } 
      else
      {
	//parent
	
         //printf("parent reads %s compare avec %d\n", buffer,compare);
	 
	//;      
      }
  } 
    printf("Le plus grand nombre = %d -pid = %d - Numéro %d \n",max,getpid(),getpid()-getppid());

  return 0;
} 

void setpipe(int valeur)
{



}