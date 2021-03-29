import pygame
from pygame.locals import *
import time


    

def Print(A):
    for fila in A:
        print(str(fila) + "\n" )
    print("---"*len(A))


def CheckInput():
   return  
    
def PintarCelda(pos,TC,fondo,tablero,state):

    div = TC**(-1)

    x = int(pos[0]*div)
    y = int(pos[1]*div)
    

    tablero[y][x] = 1

    x = x*TC
    y = y*TC

    rect = pygame.Rect(x+1,y+1,TC-2,TC-2)
    celda = pygame.draw.rect(fondo, (0,0,0), rect)
 
def Jugar(tablero):
     
    ab = list(tablero)
    for fila in range(len(tablero)):
     
     for columna in range(len(tablero[fila])):
         
         cont = 0
         n = tab[filas][columnas]

         for i in range(-1,1):
             for j in range(-1,1):
                
                 if j==0 & i ==0:
                     pass
                
                 else:
                     if tab[filas + i][columnas] == 1:
                        cont += 1
                        
         if cont >= 3:
             tablero[filas][columnas] = 1
             
          


ENCENDIDO = True

def main():
    PAUSA = 1
    Nceldas = 20
    TamañoCeldas = 10
    pygame.init()
    
    Pantalla = pygame.display.set_mode(((TamañoCeldas+2)*Nceldas,(TamañoCeldas+2)*Nceldas))
    
    Fondo = pygame.Surface(Pantalla.get_size())
    Fondo = Fondo.convert()
    Fondo.fill((255,255,255))
    
    Pantalla.blit(Fondo,(0,0))
    pygame.display.flip()
    
    tablero = [ [0 for i in range(Nceldas)] for j in range(Nceldas) ]
    
    
    
    while ENCENDIDO: 
            
        if PAUSA > 0 :
            #print("enpausa\n")
            
            Pantalla.blit(Fondo,(0,0))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    PintarCelda(event.pos,TamañoCeldas+2,Fondo,tablero,PAUSA)
                    
                
                elif event.type == KEYDOWN:
                    if event.unicode == "\r":
                        PAUSA = PAUSA*-1
                    
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.unicode == "\r":
                        PAUSA = PAUSA*-1
            
            print("Jugando\t")
            Jugar(tablero)
            
            Print(tablero)
            time.sleep(0.5)
            
        
        pygame.display.flip()
        
    
    
    

if __name__=='__main__': main()
    
    
    