from turtle import *
from Fonctions import * 


def affichageTextuelle(dicojeu):
    for ligne in range(len(dicojeu["laby"])):
        for colonne in range(len(dicojeu["laby"][ligne])):
            if [ligne,colonne] == dicojeu["entree"]:
                print('x',end = '')
            elif [ligne,colonne] == dicojeu["sortie"]:
                print('o', end = '')
            elif dicojeu["laby"][ligne][colonne] == 1:
                print('#',end = '')
            else:
                print(' ',end='')
        print()

def turtreset(x=10,y=1): #retourne a la ligne
    up()
    bk(x)
    right(90)
    fd(y)
    left(90)


def afficheGraphique(dico):
    bgcolor('lightgrey')
    thicc=dico['taille']
    topleft=dico['coin gauche']
    laby=dico['laby']
    tracer(0)
    up()
    tl1=topleft[0]
    tl2=topleft[1]
    goto(tl1,tl2)
    shape('square')
    bk(thicc)
    shapesize(thicc/20,thicc/20,thicc/20)
    for i in range(len(laby)):
        for j in range(len(laby[i])):
            if [i,j]==dico['entree']:
                fillcolor('#E74C3C') #red
                fd(thicc)
                stamp()
            elif [i,j]==dico['sortie']:
                fillcolor('#2ECC71') #light green
                fd(thicc)
                stamp()
            elif laby[i][j]==1:
                fillcolor('#000000') #black
                fd(thicc)
                stamp()
            else:
                if typePassage(j,i,dico)=='carrefour':
                    fillcolor('#D4D4D4') #grey
                    fd(thicc)
                    stamp()
                else:
                    fillcolor('#FFFFFF') #white
                    fd(thicc)
                    stamp()
        turtreset(len(laby[i])*thicc,thicc) #retourne a la ligne
    shape('turtle')
    fillcolor('#008000') #dark green
    gotostart(dico) #va vers l'entree
    tracer(1)
        
