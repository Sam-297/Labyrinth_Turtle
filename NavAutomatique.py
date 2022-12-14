from turtle import *
from Fonctions import * 


def appendheading(l):  # fonction pour ajouter les commandes que la tortue a fait
    if heading() == 0:
        l.append('right')
    elif heading() == 90:
        l.append('up')
    elif heading() == 180:
        l.append('left')
    elif heading() == 270:
        l.append('down')

def invCheminCarrefour(comm):  # fonction pour retourner au carrefour lorsque la tortue termine d'explorer la branche
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


def explorer4(d):
    lists_commands_carrefours = []
    headings_carrefours = []
    initial_headings_carrefours = []
    already_passed_carrefours = []
    in_Carrefour=False
    current_cell_type='entree'
    Commandes=[]

    while current_cell_type != 'sortie':

        current_cell_position=pixel2cell(d)
        current_cell_type = typeCellule(current_cell_position[1],current_cell_position[0],d)

        if current_cell_type == 'standard' or current_cell_type == 'entree':
            next_cell_type = headingnext(d)
            if next_cell_type == 'mur':
                left(90)
                next_cell_type = headingnext(d)
                if next_cell_type == 'mur':
                    right(180)
            fd(d['taille'])
            appendheading(Commandes)

        elif current_cell_type == 'carrefour':
            in_Carrefour=True
            lists_commands_carrefours.append([])
            if pixel2cell(d) not in already_passed_carrefours:
                already_passed_carrefours.append(pixel2cell(d))
                tracer(0)
                front_cell_type = headingnext(d)
                right(90)
                right_cell_type = headingnext(d)
                left(180)
                left_cell_type = headingnext(d)
                right(90)
                tracer(1)
                headings_carrefours.append([])
                if left_cell_type != 'mur':
                    headings_carrefours[-1].append(heading()+90)
                if right_cell_type != 'mur':
                    headings_carrefours[-1].append(heading()-90)
                if front_cell_type != 'mur':
                    headings_carrefours[-1].append(heading())
                initial_headings_carrefours.append(heading())
            if headings_carrefours[-1]==[]:
                seth(initial_headings_carrefours.pop(-1))
                invCheminCarrefour(lists_commands_carrefours.pop(-1))
                headings_carrefours.pop(-1)
            else:
                seth(headings_carrefours[-1].pop(-1))
                fd(d['taille'])
                appendheading(Commandes)
                

        elif current_cell_type == 'impasse' and pixel2cell(d):
            wrong_way=lists_commands_carrefours.pop(-1)
            invCheminCarrefour(wrong_way)
            for x in range(len(wrong_way)):
                Commandes.pop(-1)
            
        
        if in_Carrefour and lists_commands_carrefours!=[] and current_cell_type!='sortie':
            appendheading(lists_commands_carrefours[-1])

        cellchangecolor(current_cell_type)
    checkvictoire(current_cell_type,d)
    return Commandes

def suivrecheminCarrefour(comm): # fonction pour tester le chemin de la tortue
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