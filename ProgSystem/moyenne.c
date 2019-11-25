#include <stdio.h>
#include <stdbool.h>
  int main(int argc, char *argv[]) {
    int i,k=0;
    float j=0.0;
    bool isOk = true;
    //printf("Moyenne \n");
    printf("Nombre d'arguments de la ligne de commande %d \n", argc -1);
    for(k=1;k<argc;k++)
    {
      
      for(i=0;argv[k][i]!='\0';i++)
      {
	 if(argv[k][i] < '0' || argv[k][i] > '9')
      {
	isOk = false;
      }
      
      }
     
	if( (atoi(argv[k]) >= 0 && atoi(argv[k]) <= 20) && isOk )
	{
	  j = j+atoi(argv[k]);
	  //printf("%d \n",atoi(argv[k]));
	}
	else
	{
	  printf("Argument non valide \n");
	  return 0;
	}
    }
    
    printf("Moyenne = %.2f \n",j/(argc -1));
    return 0;

  }