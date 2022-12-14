from turtle import *
from tkinter import filedialog
def labyFromFile(fn) :
    f = open(fn)
    laby = []
    indline = 0
    for fileline in f:
        labyline = []
        inditem = 0
        for item in fileline:
            # empty cell / case vide
            if item == ".":
                labyline.append(0)
            # wall / mur
            elif item == "#":
                labyline.append(1)
            # entrance / entree
            elif item == "x":
                labyline.append(0)
                mazeIn = [indline, inditem]
            # exit / sortie
            elif item == "X":
                labyline.append(0)
                mazeOut = [indline, inditem]
            # discard "\n" char at the end of each line
            inditem += 1
        laby.append(labyline)
        indline += 1
    f.close()
    return laby, mazeIn, mazeOut
    
def pixel2cell(dico):
    posl = [0,0]
    post_x = xcor()
    post_y = ycor()
    post_0_x = dico['coin gauche'][0] - dico['taille']/2
    post_0_y = dico['coin gauche'][1] + dico['taille']/2
    avancement_x = abs(post_0_x - post_x)
    avancement_y = abs(post_0_y - post_y)
    posl[0] = int((avancement_y // dico['taille']))
    posl[1] = int((avancement_x // dico['taille'])) 
    return posl

def get_mouse_click_coor(x, y):
    testclic(x,y,d)
    
def testclic(x,y,dico):
    posl = [0,0]
    post_0_x = dico['coin gauche'][0] - dico['taille']/2
    post_0_y = dico['coin gauche'][1] + dico['taille']/2
    avancement_x = abs(post_0_x - x)
    avancement_y = abs(post_0_y - y)
    posl[0] = int((avancement_y // dico['taille']))
    posl[1] = int((avancement_x // dico['taille'])) 
    print(posl)

def cell2pixel(i,j,dico):
    post_0_x = dico['coin gauche'][0]
    post_0_y = dico['coin gauche'][1]
    pixel_x = i * dico['taille'] + post_0_x
    pixel_y = -(j * dico['taille'] - post_0_y)
    pixel = [pixel_x,pixel_y]
    return pixel

def typePassage(x,y,d):
    laby = d['laby']
    passage = 0
    if laby[y+1][x] == 0:
        passage+=1
    if laby[y-1][x] == 0:
        passage+=1
    if laby[y][x+1] == 0:
        passage+=1
    if laby[y][x-1] == 0:
        passage+=1
    if passage==1:
        return 'impasse'
    elif passage==2:
        return 'standard'
    else:
        return 'carrefour'

def typeCellule(x,y,d):
    laby=d['laby']
    if [y,x]==d['entree']:
        r='entree'
    elif [y,x]==d['sortie']:
        r='sortie'
    elif laby[y][x]==0:
        r=typePassage(x,y,d)
    else:
        r='mur'
    return r

def movegauche(inv=False):
    cel = pixel2cell(d)
    pos = typeCellule(cel[1],cel[0],d)
    do_mvmt=False
    if pos != 'sortie' or inv:
        seth(180)
        if cel[1]!=0 :
            posp=typeCellule(cel[1]-1,cel[0],d)
            if posp!='mur':
                pencolor('black') #dark green
                fd(d['taille'])
                do_mvmt=True
            else:
                pencolor('red')
                print('Erreur')
            cellchangecolor(posp)
    return do_mvmt

def movedroite(inv=False):
    cel=pixel2cell(d)
    pos = typeCellule(cel[1],cel[0],d)
    do_mvmt=False
    if pos != 'sortie' or inv:
        seth(0)
        if cel[1]!=len(d['laby'][cel[0]])-1:
            posp=typeCellule(cel[1]+1,cel[0],d)
            if posp!='mur':
                pencolor('black') #dark green
                fd(d['taille'])
                do_mvmt=True
            else:
                pencolor('red')
                print('Erreur')
            cellchangecolor(posp)
    return do_mvmt
    
def movebas(inv=False):
    cel=pixel2cell(d)
    pos = typeCellule(cel[1],cel[0],d)
    do_mvmt=False
    if pos != 'sortie' or inv:
        seth(270)
        if cel[0]!=len(d['laby'])-1:
            posp=typeCellule(cel[1],cel[0]+1,d)
            if posp!='mur':
                pencolor('black') #dark green
                fd(d['taille'])
                do_mvmt=True
            else:
                pencolor('red')
                print('Erreur')
            cellchangecolor(posp)
    return do_mvmt

def movehaut(inv=False):
    cel=pixel2cell(d)
    pos = typeCellule(cel[1],cel[0],d)
    do_mvmt=False
    if pos != 'sortie' or inv:
        seth(90)
        if cel[0]!=0:
            posp=typeCellule(cel[1],cel[0]-1,d)
            if posp!='mur':
                pencolor('black')
                fd(d['taille'])
                do_mvmt=True
            else:
                pencolor('red')
                print('Erreur')
            cellchangecolor(posp)
    return do_mvmt
    

def cellchangecolor(t):
    if t != 'mur':
        if t == 'impasse':
            fillcolor('#F5B041') #orange
        elif t =='standard':
            fillcolor('#008000') #vert
        else:
            fillcolor('#2980B9') #bleu

def checkvictoire(t,d):
    tracer(0)
    x0 = xcor()
    y0 = ycor()
    if t == 'sortie':
        ht()
        color('red')
        goto(0,0)
        write('Victoire !!',font= ('Comic Sans MS',100,'normal'),align='center')
        pencolor('black')
        fillcolor('#74FF00')
    goto(x0,y0)
    st()
    tracer(1)

def dictio(fn,thicc=30,topleft=[-200,200]):
    laby, mazeIn, mazeOut = labyFromFile(fn)
    dicojeu={'entree':mazeIn,'sortie':mazeOut,'laby':laby,'taille':thicc,'coin gauche':topleft}
    return dicojeu



def headingnext(d):
    cel=pixel2cell(d)
    if heading() == 0:
        x = 1
        y = 0
    elif heading() == 180:
        x = -1
        y = 0
    elif heading() == 90:
        x = 0
        y = -1
    elif heading() == 270:
        x = 0
        y = 1
    next = typeCellule(cel[1]+x,cel[0]+y,d)
    return next


def gotostart(dico):  #retourne au debut du labyrinth
    tracer(0)
    y=dico['entree'][0]
    x=dico['entree'][1]
    pix=cell2pixel(x,y,dico)
    goto(pix[0],pix[1])
    while (x == len(dico['laby'][0])-1 and heading() == 0 ) or (x == 0 and heading() == 180) or (y == len(dico['laby']) and heading() == 270 ) or (y == 0 and heading() == 90) or headingnext(d) == 'mur':
        left(90)
    tracer(1)

def gotoend(dico):   # aller a la fin du labyrinth
    tracer(0)
    y=dico['sortie'][0]
    x=dico['sortie'][1]
    pix=cell2pixel(x,y,dico)
    goto(pix[0],pix[1])
    while (x == len(dico['laby'][0])-1 and heading() == 0 ) or (x == 0 and heading() == 180) or (y == len(dico['laby']) and heading() == 270 ) or (y == 0 and heading() == 90) or headingnext(d) == 'mur':
        left(90)
    tracer(1)

        
file_path = filedialog.askopenfilename()
taille = numinput('Taille','Par defaut 20')
while taille > 60 or taille < 5:
    taille = numinput('Taille','Par defaut 20 \nVeuillez choisir un nombre entre 5 et 60 !!')
coor1 = numinput('X du coin gauche','Par defaut -200')
coor2 = numinput('T du coin gauche','Par defaut 200')
d = dictio(file_path,taille,[coor1,coor2])
comm = []