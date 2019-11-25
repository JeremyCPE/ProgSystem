#include <stdio.h>
  int main(int argc, char *argv[]) {
    int i,j,k=0;
    printf("Mirroir \n");
    printf("Nombre d'arguments de la ligne de commande %d \n", argc -1);
    for(k=1;k<argc;k++)
    {
      for(i=0;argv[k][i]!='\0';i++)
      {
	j++;
      }
      for(j;j>=0;j--)
      {
	printf("%c",argv[k][j]);
      }
      printf(" ");
    }
    printf("\n");
    return 0;

  }