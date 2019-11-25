#ifndef include_dijkstra_h
#define include_dijkstra_h

int sem_create(key_t cle, int initval);
void P(int semid);
void V(int semid);
void sem_delete(int semid);
#endif /* #ifndef __include_fichier_h__ */