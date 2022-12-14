from turtle import * 
from Graphique import *
from NavAutomatique import *
from NavManuelle import *
from Fonctions import *

afficheGraphique(d)
mode_de_jouer = textinput('Mode Selection','Mode (auto/manuel)')
while mode_de_jouer != 'manuel' and mode_de_jouer != 'auto':
    mode_de_jouer = textinput('Mode Selection','Mode (auto/manuel)\nVeuillez choisir un des options !!')

if mode_de_jouer == 'auto': 
    auto_comm = explorer4(d)
    gotostart(d)
    suivrecheminCarrefour(auto_comm)

else:
    onkey(gauche, "Left")
    onkey(droite, "Right")
    onkey(haut, "Up")
    onkey(bas, "Down")
    onkey(suivrechemin, "1")
    onkey(inverserChemin, "2")
    listen()
mainloop()



