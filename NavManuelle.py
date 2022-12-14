from turtle import *
from Fonctions import * 



def gauche():
    do_mvmt=movegauche()
    cel = pixel2cell(d)
    if do_mvmt:
        comm.append('left')
        posp = typeCellule(cel[1],cel[0],d)
    else:
        posp = typeCellule(cel[1]-1,cel[0],d)    
    checkvictoire(posp,d)


def droite():
    do_mvmt=movedroite()
    cel=pixel2cell(d)
    if do_mvmt:
        comm.append('right')
        posp = typeCellule(cel[1],cel[0],d)
    else:
        posp=typeCellule(cel[1]+1,cel[0],d)
    checkvictoire(posp,d)

def bas():
    do_mvmt=movebas()
    cel=pixel2cell(d)
    if do_mvmt:
        comm.append('down')
        posp = typeCellule(cel[1],cel[0],d)
    else:
        posp=typeCellule(cel[1],cel[0]+1,d)
    checkvictoire(posp,d)


def haut():
    do_mvmt=movehaut()
    cel=pixel2cell(d)
    if do_mvmt:
        comm.append('up')
        posp = typeCellule(cel[1],cel[0],d)
    else:
        posp=typeCellule(cel[1],cel[0]-1,d)
    checkvictoire(posp,d)



def suivrechemin():
    gotostart(d)
    for move in comm:
        if move == 'left':
            t=movegauche()
            if not t:
                print('Movement Impossible')
                return None
        elif move == 'right':
            t=movedroite()
            if not t:
                print('Movement Impossible')
                return None
        elif move == 'up':
            t=movehaut()
            if not t:
                print('Movement Impossible')
                return None
        elif move == 'down':
            t=movebas()
            if not t:
                print('Movement Impossible')
                return None
        
def inverserChemin():
    gotoend(d)
    for i in range(len(comm)-1,-1,-1):
        if comm[i]=='right':
            t=movegauche(True)
            if not t:
                print('Movement Impossible')
                return None
        elif comm[i]=='left':
            t=movedroite(True)
            if not t:
                print('Movement Impossible')
                return None
        elif comm[i]=='up':
            t=movebas(True)
            if not t:
                print('Movement Impossible')
                return None
        elif comm[i]=='down':
            t=movehaut(True)
            if not t:
                print('Movement Impossible')
                return None