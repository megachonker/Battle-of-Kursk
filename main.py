
"""
partie fiche:
        vitesse:1
vitesse_x = 5
vitesse_y = 5

"""


                ###Chose à faire !###
"""

fair une progression:
        avec des atribue/classe:
                hp
                vitesse char ou projectile
                nombre de rebon ou durer de vie du projectile
                déga
                Pouvoir ataque spécial ?

        avec des niveaux diférant:
                automatique
                fait a la main

Animation:
        automatiser les animation ?
        rotation chart etc
        explosion fin de niveaux

projectile:

        rebont:
                nb de rebont : fait
                liftime :pas déploiyer

        rotation sprite
        direction de tire : fait


Algo/ia:
        Controle tank:
                bot
                joueur humain
        géneration du niveaux:
                algo ?
                Ou utiliser un phishier pour crée la carte


SON:
        bruitage : fait
        musique : fait

Bug:
        fair une gestion du temps correct:
                !!!!
        NE PËUT pas fair plusieur mouvement en meme temps
                Z+Q on arrete Z qui fait juste q n'avance plu !
        si souris dans écrant jeux plus rapide
                car les touche sont detecter quand un événment dans l'écrant type bouger souris
        fair des hitbox plus fine car mouvement pausible imposible
                ya une méthode!

        ralentisement quand on tire:
                fait


Optimisation:
        Nouvel methode pour x.y sprite:
                utiliser les classe ?
                tableaux 2d ?


lisibilitée code:
        rajouter comentaire
        le sinder en plusieur sous programe
        phaute etc
Sound.play(loops=0, maxtime=0, fade_ms=0)

"""




import pygame
from pygame.locals import *


direction_tire = "right"
animation_tank_explosion_a_suprimer = False
start_annimation_explosion_charmechan = False
timer_char_enemie_detruit = 0
char_enemie_detruit = 0
etat_boue =0
tire_joueur = 0
mouvement = 0
vitesse_x = 5
vitesse_y = 5

cote_creation_projectil = 19
decalage_tanque_sprite = 15
decalage_tanque_sprite2 = 0

animation_explosion_niveaux_position_x, animation_explosion_niveaux_position_y= [], []
#clock_animation_explosion_tank_enemie = []

animation_explosion_tank_position_x, animation_explosion_tank_position_y = [], []
clock_animation_explosion_tank_enemie = []

#pygame.mixer.init(frequency=48000, size=-8, channels=1, buffer=1024)
#print(pygame.mixer.get_init())
pygame.init()
pygame.time.Clock().tick(60)


#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((500,500))


#SONNN
musique_fond = pygame.mixer.Sound('musique.wav')
#bruit_char_detruit = pygame.mixer.Sound('charMEur.wav')
bruit_char_detruit = pygame.mixer.Sound('mureplosion.wav')
musique_fond.play(loops=-1, maxtime=0, fade_ms=0)
tank_tire_sons = pygame.mixer.Sound('Tiretank.wav')
mureplosion = pygame.mixer.Sound('mureplosion.wav')
bruit_char_avant = pygame.mixer.Sound('TANKmarche.wav')



#fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#rocher
rock = pygame.image.load("rock.png").convert()
position_rock = rock.get_rect() #avoir la position


#On génére des mure#

rock_list_x, rock_list_y = [] ,[]
def delimitation():
        for i in range(10):
                rock_list_x.append(50*i)
                rock_list_y.append(50*9)
        for i in range(10):
                rock_list_x.append(50*9)
                rock_list_y.append(50*i)
        for i in range(10):
                rock_list_x.append(50*i)
                rock_list_y.append(0)
        for i in range(10):
                rock_list_x.append(0)
                rock_list_y.append(50*i)

def lv(var):
        if var ==0:
                delimitation()

        elif var == 1:

                delimitation()

                #Regrouper en 4 au centre
                rock_list_x.append(50*5)
                rock_list_y.append(50*5)

                rock_list_x.append(50*4)
                rock_list_y.append(50*5)

                rock_list_x.append(50*4)
                rock_list_y.append(50*4)

                rock_list_x.append(50*5)
                rock_list_y.append(50*4)


        elif var == 2:
                delimitation()

                #Regrouper en 4 au centre
                rock_list_x.append(50*5)
                rock_list_y.append(50*5)

                rock_list_x.append(50*4)
                rock_list_y.append(50*5)

                rock_list_x.append(50*4)
                rock_list_y.append(50*4)

                rock_list_x.append(50*5)
                rock_list_y.append(50*4)

                rock_list_x.append(50*2)
                rock_list_y.append(50*2)


                rock_list_x.append(50*2)
                rock_list_y.append(50*7)


                rock_list_x.append(50*7)
                rock_list_y.append(50*2)

                rock_list_x.append(50*7)
                rock_list_y.append(50*7)

lv(0)

#tankjoueur
tank_joueur = pygame.image.load("tankjoueur.png")
position_tank_joueur = tank_joueur.get_rect() #avoir la position
position_tank_joueur.y = 250
position_tank_joueur.x = 100
#fenetre.blit(tank_joueur, (position_tank_joueur)) #update la position

#tankenemie
#####################QUE UN POUR L4INSANT IL FAUDRA CR2 DES LISTE §
tank_ennemi = pygame.image.load("tankenemi.png")
position_tank_ennemi = tank_ennemi.get_rect() #avoir la position tankenemie
position_tank_ennemi_x, position_tank_ennemi_y = [] ,[]

position_tank_ennemi.y = 0
position_tank_ennemi.x = 0

#spawn enemie
def enemy_spawn():
        position_tank_ennemi_x.append(350)
        position_tank_ennemi_y.append(100)

        position_tank_ennemi_x.append(300)
        position_tank_ennemi_y.append(150)

        position_tank_ennemi_x.append(350)
        position_tank_ennemi_y.append(350)

        position_tank_ennemi_x.append(300)
        position_tank_ennemi_y.append(300)
enemy_spawn()

#Animation:

#tank mouvement
tank_joueur_mouvement = pygame.image.load("mouvement.png")

#tank joueur tire
tank_joueur_tire = pygame.image.load("fire.png")
tank_joueur_tire2 = pygame.image.load("fire2.png")

        #projectile#
obus = pygame.image.load("projectil.png")

projectile_joueur_x, projectile_joueur_y = [] ,[]
position_projectile_joueur = obus.get_rect()


#spite explosion OBU:
sprite_explosion1 = pygame.image.load("explosion1.png")
sprite_explosion2 = pygame.image.load("explosion2.png")
#inutile mais on l'initialise de magnierre propre pour l'utiliser avec dees atribu x et y
position_explosion_obu = sprite_explosion1.get_rect()
position_sprite_explosion_projectile_x, position_sprite_explosion_projectile_y, sprite_explosion_durer = [] ,[], []

#sprite explosion Char
sprite_explosion_char2 = pygame.image.load("explosionDestruction1.png")
sprite_explosion_char1 = pygame.image.load("explosionDestruction2.png")
position_sprite_explosion_char1_x, position_sprite_explosion_char1_y, sprite_explosion_char1_durer = [] ,[], []
position_sprite_explosion_char1 = tank_joueur.get_rect()
animation_explosion_tank_position = tank_joueur.get_rect()

#variable pour animation_explosion_tank_position
#animation_explosion_tank_position = tank_joueur.get_rect()


#Fair ? convertion en vecteur via angle
inercie_projectile_joueur_x, inercie_projectile_joueur_y = [] ,[]
inercie_position_projectile_joueur = obus.get_rect() #inutile
inercie_creation_projectile_joueur_x=0
inercie_creation_projectile_joueur_y=0

#durer de vie du projectil si bug
liftime_projectile_joueur = []

#nombre de rebont
nombre_rebont_projectil_joueur = []


#tout les char mort
niveaux_termier = False

#niveaux
niveaux_actuelle = 0

###
def suprProjectil(var):
        print("suprimerProjectil")
        print(var)
        print(inercie_projectile_joueur_x)
        del inercie_projectile_joueur_x[var]#var partout
        del inercie_projectile_joueur_y[var]
        del liftime_projectile_joueur[var]
        del projectile_joueur_y[var]
        del projectile_joueur_x[var]
        del nombre_rebont_projectil_joueur[var]
        print("supression")


def ajout_explosion_projectile(x, y):
        #print("ajout d'une explosion")
        sprite_explosion_durer.append(0)
        position_sprite_explosion_projectile_x.append(x)
        position_sprite_explosion_projectile_y.append(y)


def supression_Explosion_Projectil(var):
        del position_sprite_explosion_projectile_x[var]
        del position_sprite_explosion_projectile_y[var]
        del sprite_explosion_durer[var]

def supression_char_enemie(var):
        del position_tank_ennemi_x[var]
        del position_tank_ennemi_y[var]

def afficher_caillou(rock_list_x, rock_list_y):
        for u in range(len(rock_list_x)):
                position_rock.y = rock_list_y[u]
                position_rock.x = rock_list_x[u]
                fenetre.blit(rock, (position_rock))



pygame.display.flip()

#appuit des touche en boucle
pygame.key.set_repeat(1, 30)


#Boucle du jeux
continuer = 1
while continuer:

        #CLock projectile

        for u in range(len(liftime_projectile_joueur)):
                if liftime_projectile_joueur[u] < 1000:
                        liftime_projectile_joueur[u] = liftime_projectile_joueur[u] + 1 #cHaque tick on ajjoute 1 a la durer de vie de tout les projectile
                        #print(liftime_projectile_joueur[u])

                else :
                        #print("liftime_projectile_joueur Depasée", liftime_projectile_joueur[u],"u ",u)
                        suprProjectil([u])

        for event in pygame.event.get():

                #pour quiter
                if event.type == QUIT:
                        continuer = 0

                #Déplacement:

                eventTouche = pygame.key.get_pressed()
                position_tank_joueur_avant = position_tank_joueur

                #Z Q S D espace
                if eventTouche[K_w]:
                        position_tank_joueur=position_tank_joueur.move(0, -vitesse_y)
                        etat_boue = 60
                        inercie_creation_projectile_joueur_y = -vitesse_y/35
                        inercie_creation_projectile_joueur_x = 0
                if eventTouche[K_a]:
                        position_tank_joueur=position_tank_joueur.move(-vitesse_x, 0)
                        inercie_creation_projectile_joueur_x = -vitesse_x/35
                        inercie_creation_projectile_joueur_y = 0
                        etat_boue = 60
                if eventTouche[K_s]:
                        position_tank_joueur=position_tank_joueur.move(0, vitesse_y)
                        etat_boue = 60
                        inercie_creation_projectile_joueur_y = vitesse_y/35
                        inercie_creation_projectile_joueur_x = 0
                if eventTouche[K_d]:
                        position_tank_joueur=position_tank_joueur.move(vitesse_x, 0)
                        inercie_creation_projectile_joueur_x = vitesse_x/35
                        inercie_creation_projectile_joueur_y = 0
                        etat_boue = 60
                if etat_boue == 0:
                        inercie_creation_projectile_joueur_y = 0
                        inercie_creation_projectile_joueur_x = 0



                if eventTouche[K_LEFT]:
                        direction_tire = "left"
                        #changement direction sprite
                        decalage_tanque_sprite2 = 25 #sprite animation tire
                        cote_creation_projectil = 0 #endroit creation projectile
                        decalage_tanque_sprite = 0 #sprite pour boue rouler
                        tank_joueur = pygame.image.load("rotation/tankjoueurG.png")
                        tank_joueur_mouvement = pygame.image.load("rotation/mouvementG.png")
                        tank_joueur_tire = pygame.image.load("rotation/fireG.png")
                        tank_joueur_tire2 = pygame.image.load("rotation/fire2G.png")
                if eventTouche[K_RIGHT]:
                        direction_tire = "right"
                        decalage_tanque_sprite2 = 0
                        cote_creation_projectil = 19
                        decalage_tanque_sprite = 15
                        tank_joueur = pygame.image.load("tankjoueur.png")
                        tank_joueur_mouvement = pygame.image.load("mouvement.png")
                        tank_joueur_tire = pygame.image.load("fire.png")
                        tank_joueur_tire2 = pygame.image.load("fire2.png")

                        changement_direction_tank_j(direction_tire)
                if eventTouche[K_UP]:
                        #print("up")
                        direction_tire = "up"
                if eventTouche[K_DOWN]:
                        #print("down")
                        direction_tire = "down"



                #Tire
                if eventTouche[K_SPACE]:
                        if tire_joueur == 0:
                                tire_joueur = 750
                                projectile_joueur_x.append(position_tank_joueur.x)
                                projectile_joueur_y.append(position_tank_joueur.y)
                                liftime_projectile_joueur.append(0)

                                if direction_tire == "right":
                                        #print(1+inercie_creation_projectile_joueur_x)
                                        inercie_projectile_joueur_x.append(1+inercie_creation_projectile_joueur_x)
                                        inercie_projectile_joueur_y.append(0+inercie_creation_projectile_joueur_y)
                                if direction_tire == "left":
                                        inercie_projectile_joueur_x.append(-1+inercie_creation_projectile_joueur_x)
                                        inercie_projectile_joueur_y.append(0+inercie_creation_projectile_joueur_y)
                                if direction_tire == "up":
                                        inercie_projectile_joueur_x.append(0+inercie_creation_projectile_joueur_x)
                                        inercie_projectile_joueur_y.append(-1+inercie_creation_projectile_joueur_y)
                                if direction_tire == "down":
                                        inercie_projectile_joueur_x.append(0+inercie_creation_projectile_joueur_x)
                                        inercie_projectile_joueur_y.append(1+inercie_creation_projectile_joueur_y)


                                nombre_rebont_projectil_joueur.append(0)
                                tank_tire_sons.play()


                #quiter avec une touche
                if eventTouche[K_e]:
                        continuer = 0


                #SI le tank joueur contre un mure ou un autre tank il s'arrete
                for u in range(len(rock_list_x)):
                        position_rock.y = rock_list_x[u]
                        position_rock.x = rock_list_y[u]

                        if position_rock.colliderect(position_tank_joueur):
                                position_tank_joueur = position_tank_joueur_avant
                                #print("position_tank_joueur", position_tank_joueur)
                                #print("position_rock", position_rock)
                        #else:
                                #print("Joueur libre")
                #SI enemie Recule
                for u in range(len(position_tank_ennemi_x)):
                        position_tank_ennemi.y = position_tank_ennemi_y[u]
                        position_tank_ennemi.x = position_tank_ennemi_x[u]

                        if position_tank_ennemi.colliderect(position_tank_joueur):
                                position_tank_joueur = position_tank_joueur_avant




                #Rafraichissement: (d'une frame)

        #rafraichire fond
        fenetre.blit(fond, (0,0))

        #rafraichisement des Mure


        if niveaux_termier == True:
                niveaux_actuelle = niveaux_actuelle + 1
                niveaux_termier = False
                #CHarger niveaux



                for i in range(len(rock_list_x)):
                        clock_animation_explosion_tank_enemie.append(0)
                        animation_explosion_niveaux_position_x.append(rock_list_x[i])
                        animation_explosion_niveaux_position_y.append(rock_list_y[i])

                for o in range(90):#90 frame
                        afficher_caillou(rock_list_x, rock_list_y)
                        if o < 30:
                                pygame.time.wait(3)
                                for u in range(len(animation_explosion_niveaux_position_y)):
                                        position_rock.y = animation_explosion_niveaux_position_y[u]
                                        position_rock.x = animation_explosion_niveaux_position_x[u]
                                        fenetre.blit(sprite_explosion_char1, (position_rock))

                        elif 30 < o < 60:
                                pygame.time.wait(3)#tempo
                                for u in range(len(animation_explosion_niveaux_position_y)):
                                        position_rock.y = animation_explosion_niveaux_position_y[u]
                                        position_rock.x = animation_explosion_niveaux_position_x[u]
                                        fenetre.blit(sprite_explosion_char2, (position_rock))

                        pygame.display.flip()



                rock_list_x, rock_list_y = [],[]

                lv(niveaux_actuelle)#on load les kayou
                enemy_spawn()#spawn enemie



        #j'ai du inverser les x et y pour que se soit normal
        for u in range(len(rock_list_x)):
                position_rock.y = rock_list_y[u]
                position_rock.x = rock_list_x[u]
                fenetre.blit(rock, (position_rock))

        #animation Projectile
        projectil_a_detruire = 69 # =[]
        char_enemie_toucher = 69
        for u in range(len(projectile_joueur_x)):


                if liftime_projectile_joueur[u] < 5000 and nombre_rebont_projectil_joueur[u] <= 2:

                        #calcule de nouvelle Position a l'aide du temps
                        position_projectile_joueur.x = 19 + inercie_projectile_joueur_x[u] * liftime_projectile_joueur[u] + projectile_joueur_x[u]
                        position_projectile_joueur.y = 21 + inercie_projectile_joueur_y[u] * liftime_projectile_joueur[u] + projectile_joueur_y[u]


                        #Colision mure Des Projectile
                        for t in range(len(rock_list_x)):
                                #on charge les mure
                                position_rock.y = rock_list_x[t]
                                position_rock.x = rock_list_y[t]

                                #verification que projectile pas sur mure sinon
                                if position_rock.colliderect(position_projectile_joueur):
                                        #projectil_a_detruire.append(u)
                                        projectil_a_detruire = u
                                        ajout_explosion_projectile(position_projectile_joueur.x, position_projectile_joueur.y)
                                        #print(nombre_rebont_projectil_joueur)
                                        #on rajoute un projectile dans le sens inverse car rebon
                                        projectile_joueur_x.append(inercie_projectile_joueur_x[u] * liftime_projectile_joueur[u] + projectile_joueur_x[u])
                                        projectile_joueur_y.append(inercie_projectile_joueur_y[u] * liftime_projectile_joueur[u] + projectile_joueur_y[u])
                                        nombre_rebont_projectil_joueur.append(nombre_rebont_projectil_joueur[u] + 1)
                                        liftime_projectile_joueur.append(0)
                                        #l'orsque le projectile touche le mur il change de direction
                                        if direction_tire == "left" or direction_tire == "right":
                                                inercie_projectile_joueur_x.append(-inercie_projectile_joueur_x[u])
                                                inercie_projectile_joueur_y.append(inercie_projectile_joueur_y[u])
                                        if direction_tire == "up" or direction_tire == "down":
                                                inercie_projectile_joueur_x.append(inercie_projectile_joueur_x[u])
                                                inercie_projectile_joueur_y.append(-inercie_projectile_joueur_y[u])
                                        #print(nombre_rebont_projectil_joueur)
                                        mureplosion.play(nombre_rebont_projectil_joueur[u])
                                        #quand un projectile est crée on arrete de lister les mure
                                        break



                        #verification si projectile touche char
                        for t in range(len(position_tank_ennemi_x)):
                                position_tank_ennemi.x = position_tank_ennemi_x[t]
                                position_tank_ennemi.y = position_tank_ennemi_y[t]

                                if position_tank_ennemi.colliderect(position_projectile_joueur):

                                        #jouer sont convivial
                                        bruit_char_detruit.play()
                                        #print("u avant =", t)
                                        projectil_a_detruire = u
                                        char_enemie_toucher = t #lier ça a une liste de char enemie + vie le bordelle quoi
                                        ajout_explosion_projectile(position_projectile_joueur.x, position_projectile_joueur.y)
                                        #verifi si le niveaux est clean
                                        if len(position_tank_ennemi_x) == 1:
                                                niveaux_termier = True



                        #fonction qui sere a afficher les sprite


                        fenetre.blit(obus, (position_projectile_joueur))

                else:
                        projectil_a_detruire = u


        #fonction qui ser a detruire les projectile quand il touche quelque chose
        #hor de la boucle pour suprimer tout les item des liste en une soeul foit sinon conflict
        """
        for u in range(len(projectil_a_detruire)):
                print("u --> ",u, "projectil_a_detruire", projectil_a_detruire)
                print("u ==> ",u, "inercie_projectile_joueur_x", inercie_projectile_joueur_x)
                suprProjectil(projectil_a_detruire[u])
        """
        if projectil_a_detruire != 69:
                #print("projectil_a_detruire numero => ", projectil_a_detruire)
                #print("liste des position projectil", projectile_joueur_x)
                suprProjectil(projectil_a_detruire)


        #animation sprite explosion
        #SI explosion 1 et 2 spawn
        #ET SI explosion 1 se finit
        #ALLor

        """
        U ==>  1  sprite_explosion_durer  [33, 18]
                                               +1
        U ==>  0  sprite_explosion_durer  [33, 19]
                                          +1
        U ==>  1  sprite_explosion_durer  [34, 19]
                                               +1
        U ==>  0  sprite_explosion_durer  [34, 20]
                                          +1
        Supression de l'explosion
        U ==>  1  sprite_explosion_durer  [20] {ICI} le tableaux n'a que une case or l'algo verifi cette case elle n'existe pas donc erreur
        """
        #DOnC on  va fair la supression en dehor de la boucle on pere donc une frame
        explosion_a_detruire = 69 #=[]
        for u in range(len(sprite_explosion_durer)):

                #print("U ==> ",u ," sprite_explosion_durer ",sprite_explosion_durer)

                #ajouter au sprite du temps
                sprite_explosion_durer[u] = sprite_explosion_durer[u] + 1

                position_explosion_obu.x = position_sprite_explosion_projectile_x[u]
                position_explosion_obu.y = position_sprite_explosion_projectile_y[u]

                #choix des animation dexplosion projectile en fc du temps
                if sprite_explosion_durer[u] < 200:
                        fenetre.blit(sprite_explosion1, (position_explosion_obu))

                elif sprite_explosion_durer[u] < 350:
                        fenetre.blit(sprite_explosion2, (position_explosion_obu))

                else: #si le temps est epuiser
                        #print("Supression de l'explosion")
                        #explosion_a_detruire.append(u)
                        explosion_a_detruire = u
        """
        #le tableaux crache les var a suprimer
        for u in range(len(explosion_a_detruire)):
                #print("U --> ",u ," explosion_a_detruire", explosion_a_detruire)
                #suprExplosionProjectil(explosion_a_detruire[u])
                supression_Explosion_Projectil(explosion_a_detruire[u])
        """
        if explosion_a_detruire != 69:
                #print("explosion_a_detruire", explosion_a_detruire)
                #print("sprite_explosion_durer", sprite_explosion_durer)
                supression_Explosion_Projectil(explosion_a_detruire)


        #rafraichire joueur

        if tire_joueur > 400:

                position_tank_joueurCOPI = position_tank_joueur.x
                position_tank_joueur.x = position_tank_joueur.x - decalage_tanque_sprite2

                fenetre.blit(tank_joueur_tire, (position_tank_joueur))
                position_tank_joueur.x = position_tank_joueurCOPI

                #desincrémentation temps de tire
                tire_joueur = tire_joueur -1
                #print("temps restant tire",tire_joueur)
        elif tire_joueur > 100:


                position_tank_joueurCOPI = position_tank_joueur.x
                position_tank_joueur.x = position_tank_joueur.x - decalage_tanque_sprite2

                fenetre.blit(tank_joueur_tire2, (position_tank_joueur))
                position_tank_joueur.x = position_tank_joueurCOPI
                tire_joueur = tire_joueur -1
                #print("temps restant tire",tire_joueur)
        else:
                if tire_joueur > 0:
                        tire_joueur = tire_joueur -1
                        #print("temps restant tire",tire_joueur)

                if etat_boue > 0:
                        bruit_char_avant.play()
                        etat_boue = etat_boue -1
                        position_tank_joueurCOPI = position_tank_joueur.x
                        position_tank_joueur.x = position_tank_joueur.x - decalage_tanque_sprite
                        fenetre.blit(tank_joueur_mouvement, (position_tank_joueur))
                        position_tank_joueur.x = position_tank_joueurCOPI
                        #print(position_tank_joueur.x)
                        #print("etat_boue",etat_boue)
                elif etat_boue == 0:
                        fenetre.blit(tank_joueur, (position_tank_joueur))
                        bruit_char_avant.stop()


        #rafraichire tout les chard enemei + animation


        #SI Detection de char toucher
        #on suprime le chard concerner + sauvgarde donner dans buffer
        if char_enemie_toucher != 69:
                position_tank_ennemi.x = position_tank_ennemi_x[char_enemie_toucher]
                position_tank_ennemi.y = position_tank_ennemi_y[char_enemie_toucher]

                animation_explosion_tank_position_x.append(position_tank_ennemi.x)
                animation_explosion_tank_position_y.append(position_tank_ennemi.y)

                clock_animation_explosion_tank_enemie.append(0)
                supression_char_enemie(char_enemie_toucher)

        #quand chard toucher animation lancer selon les donner
        for t in range(len(animation_explosion_tank_position_x)):
                clock_animation_explosion_tank_enemie[t] = clock_animation_explosion_tank_enemie[t] + 1

                animation_explosion_tank_position.x=animation_explosion_tank_position_x[t]
                animation_explosion_tank_position.y=animation_explosion_tank_position_y[t]


                if clock_animation_explosion_tank_enemie[t] < 150:
                        fenetre.blit(tank_ennemi, (animation_explosion_tank_position))
                        fenetre.blit(sprite_explosion_char1, (animation_explosion_tank_position))

                else:
                        fenetre.blit(tank_ennemi, (animation_explosion_tank_position))
                        fenetre.blit(sprite_explosion_char2, (animation_explosion_tank_position))

                if clock_animation_explosion_tank_enemie[t] == 300:
                        animation_tank_explosion_a_suprimer = True
                        #quand on sort de la boucle on suprime les animaiton

        #on suprime les animation
        if animation_tank_explosion_a_suprimer == True:
                del clock_animation_explosion_tank_enemie[0]
                del animation_explosion_tank_position_y[0]
                del animation_explosion_tank_position_x[0]
                animation_tank_explosion_a_suprimer = False


        #on afficher tout les chard a lécrant selo leur position
        for u in range(len(position_tank_ennemi_x)):
                position_tank_ennemi.x = position_tank_ennemi_x[u]
                position_tank_ennemi.y = position_tank_ennemi_y[u]
                fenetre.blit(tank_ennemi, (position_tank_ennemi))






        pygame.display.flip()



pygame.quit()