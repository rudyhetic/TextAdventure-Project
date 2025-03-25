import random

def debut_de_notre_jeu():
    directions = ["gauche", "droite", "devant", "derriere"]
    print("\n")
    print("Tu est dans ta maison, il est 18h ! ta pas vu l'heure depeche toi de te preparer")
    print("Tu doit te rendre au concert de Playboy carti à 20h ! Ne soit pas en retard !")
    print("...")
    print("Pour assiter au concert, tu doit prendre ton billiet pour rentrer")
    print("Cherche ton billet, il est surement quelque part chez toi")
    print("\n")
    print_color("Voici les commandes disponibles: gauche | droite | devant | derriere", "green")
    reste_dans_la_piece = True

    while reste_dans_la_piece:
        userInput = input().lower()
        if userInput == "gauche":
           cuisine()
        elif userInput == "droite":
           print("\n")
           print("Il n'y a a pas de porte par ici, seulement ton mur et un poster de playboy carti sur ton mur")
        elif userInput == "devant":
           salon()
        elif userInput == "derriere":
           print("\n")
           print("Tu est vert ton lit qui est coller au mur, si tu recule plus tu va te cogner.")
        else:
           print("\n")
           print("Non cette commande n'existe pas, relie les coammandes disponible.")

def cuisine():
    directions = ["gauche", "droite", "devant", "derriere"]
    print("\n")
    print("Tu as ouvert la porte, tu es à l'intérieur de ta cuisine")
    print_color("Voici les commandes disponibles: gauche | droite | devant | derriere", "green")
    reste_dans_la_piece = True

    while reste_dans_la_piece:
        userInput = input().lower()
        if userInput == "droite":
            print("\n")
            print("Tu es maintenant en face de ton frigo, mais il est vide.")
            print("Il n'y a donc rien par ici.")
        elif userInput == "gauche":
            print("\n")
            print("Tu te diriges vers la vaisselle, mais il n'y a rien ici.")
        elif userInput == "derriere":
            chambre()
            reste_dans_la_piece = False
        else:
            print("\n")
            print("Veuillez entrer une option valide pour le jeu d'aventure.")


def chambre():
    directions = ["gauche", "droite", "devant", "derriere"]
    print("\n")
    print_color("Tu est revenu dans ta chambre, l'aventure peut recommencer", "yellow")
    print("Si tu est de retours et que tu vient de sortir de la cusine")
    print("C'est qu'il te reste plus qu'a trouver ton salon")
    print("\n")
    print_color("Voici les commandes disponibles: gauche | droite | devant | derriere", "green")
    reste_dans_la_piece = True

    while reste_dans_la_piece:
        userInput = input().lower()
        if userInput == "gauche":
            cuisine()
        if userInput == "droite":
            print("\n")
            print("Il n'y a a pas de porte par ici, seulement ton mur et un poster de playboy carti sur ton mur")
        elif userInput == "devant":
            salon()
        elif userInput == "derriere":
            print("\n")
            print("Tu est vert ton lit qui est coller au mur, si tu recule plus tu va te cogner.")
        else: 
            print("\n")
            print("Cette commande n'existe pas, concentre toi.")

def salon():
  directions = ["gauche", "droite", "devant", "derriere"]
  print('\n')
  print("Tu a ouvert la porte, tu est à l'interieur de ton salon")
  print("Félicitation tu vient de récuper une clefs")
  print("Ainsi que ton billet pour assister au concert")
  print("\n")
  print_color("Voici les commandes disponibles: gauche | droite | devant | derriere", "green")
  reste_dans_la_piece = True
  
  while reste_dans_la_piece:
      userInput = input().lower()
      if userInput == "gauche":
         dehors()
      if userInput == "droite":
        print("\n")
        print("Tu est devant ta télévision, mais il n'y a rien que tu peut récupérer par ici")
      elif userInput == "derriere":
        chambre()
      else:
        print("\n")
        print("Cette commande n'existe pas, concentre toi.")

def dehors():
  directions = ["gauche", "droite", "devant", "arriere"]
  print('\n')
  print_color("Tu a ouvert la porte, tu est maintenant dehors", "yellow")
  reste_dans_la_piece = True
  
  while reste_dans_la_piece not in directions:
    print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
    userInput = input()
    if userInput == "droite":
      print("\n")
      print("Il y'a un chemin qui s'arrete chez un voisin, ce n'est pas par ici que se trouve le concert")
    elif userInput == "devant":
      print("\n")
      print("tu ne peut pas passer par ici, car c'est une route, tu peut peut etre prendre le bus pour allez a ta destination")
    elif userInput == "gauche":
      bus()
    elif userInput == "arriere":
      print("\n")
      print("Tu est en retard, ne retourne pas chez toi, ou tu va louper le concert.")
    else:
      print("Non cette commande n'existe pas, tu peut soit prendre la voiture, le bus ou marcher.")

def bus():
  directions = ["continue"]
  print('\n')
  print_color("Génial tu a pris le bus", "yellow")
  print("profite de ton parcours le chauffeur de bus conduit")
  print("Jusqu'a ce que tu arrive à ta destination")
  print("Quand tu sera arriver Le chauffeur de bus te dira de sortir")
  userInput = ""
  while userInput not in directions:
    print_color("Voici les commandes disponibles dans le bus: continue", "green")
    userInput = input()
    if userInput == "continue":
      station_suivant()
    else:
      print("\n")
      print("Cette commande n'existe pas à l'interieur du bus.")

def station_suivant():
  directions = ["continue"]
  print('\n')
  print_color("la station Naboo vient d'etre annoncer", "yellow")
  print("Ce n'est pas encore ta station de bus qui t'emmene au concert")
  userInput = ""
  while userInput not in directions:
    print_color("Voici les commandes disponibles dans le bus: continue", "green")
    userInput = input()
    if userInput == "continue":
      station_suivant_deux()
    else:
      print("\n")
      print("Cette commande n'existe pas à l'interieur du bus.")

def station_suivant_deux():
  directions = ["continue"]
  print('\n')
  print_color("la station Kamino vient d'etre annoncer", "yellow")
  print("Il te reste encore un peu de chemin, ce n'est pas encore ta station")
  userInput = ""
  while userInput not in directions:
    print_color("Voici les commandes disponibles dans le bus: continue", "green")
    userInput = input()
    if userInput == "continue":
      station_suivant_trois()
    else:
      print("\n")
      print("Cette commande n'existe pas à l'interieur du bus.")

def station_suivant_trois():
  directions = ["continue"]
  print('\n')
  print_color("la station Kashyyyk vient d'etre annoncer", "yellow")
  print("Ta station va bientot etre annoncer")
  userInput = ""
  while userInput not in directions:
    print_color("Voici les commandes disponibles dans le bus: continue", "green")
    userInput = input()
    if userInput == "continue":
      station_suivant_fin()
    else:
      print("\n")
      print("Cette commande n'existe pas à l'interieur du bus.")

def station_suivant_fin():
  directions = ["continue"]
  print('\n')
  print_color("la station Utapau vient d'etre annoncer", "yellow")
  print("Bon bah parfait tu est arriver")
  userInput = ""
  while userInput not in directions:
    print_color("Voici les commandes disponibles dans le bus: continue", "green")
    userInput = input()
    if userInput == "continue":
      station_concert()
    else:
      print("\n")
      print("Cette commande n'existe pas à l'interieur du bus.")

def station_concert():
    directions = ["gauche", "droite", "devant"]
    print("\n")
    print("Tu est arriver au concert")
    print("dirige toi vers l'entrée pour acceder au concert")
    print("heuresement que tu a pris ton badge pour rentrer")
    print_color("Voici les commandes disponibles: gauche | droite | devant", "green")
    reste_dans_la_piece = True

    while reste_dans_la_piece:
        userInput = input().lower()
        if userInput == "droite":
            print("\n")
            print("Il y'a des barrieres tu ne peut pas passer par ici.")
            print("Il n'y a donc rien par ici.")
            print("Cherche l'entrée")
        elif userInput == "gauche":
            print("\n")
            print("Tu te dirige vers les barrieres.")
            print("tu ne peut pas passer par ici, tu a un badge utilise le pour passer par l'entrée")
        elif userInput == "devant":
            entrer_concert()
            reste_dans_la_piece = False
        else:
            print("\n")
            print("Cette commande n'existe pas, il faut que tu te concentre.")

def entrer_concert():
    directions = ["ticket"]
    print('\n')
    print_color("Chef sécurité : Bonjour veuillez nous montrer votre billet pour entrer", "yellow")
    userInput = ""
    
    while userInput not in directions:
      print_color("Utilise ton billet de concert que tu a recuperer dans ton salon la commande est: (ticket)", "green")
      userInput = input()
      if userInput == "ticket":
        concert()
      else:
        print("\n")
        print("Desoler, si vous n'avez pas votre place de concert, vous ne pouvez pas rentrer.")

def concert():
  directions = ["gauche", "droite", "devant", "arriere"]
  print('\n')
  print_color("Tu est maintenant à l'interieur du concert", "green")
  print("Tu a pleins de possibilités")
  print("Tu peut allez au stands voir ce que tu peut trouver")
  print("Ou tu peut te diriger directement vers la musique")
  print("...")
  print_color("oublie pas que tout tes choix modifie le cours des événement, fait le bon choix", "yellow")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
    userInput = input()
    if userInput == "gauche":
      print("\n")
      print("Il y'a une vitre, qui donne un appercu du concert")
      print("On peut voir les gens bouger, danser et chanter, mais on ne peut pas passer par là.")
    elif userInput == "devant":
      couloir()
    elif userInput == "droite":
      print("\n")
      print("Il y'a un mur qui contient une affiche de la promotion du concert de Carti")
    elif userInput == "arriere":
      print("\n")
      print("Tu est devant le portail que tu vient de passer pour entrer dans le concert.")
      print("Tu a mis du temps pour te rendre au concert, ce n'est pas le moment de sortir...")
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def couloir():
    directions = ["gauche", "droite", "devant", "arriere"]
    print('\n')
    print_color("Tu avances dans le couloir", "green")
    print("Il fait assez sombre... Mais on entend de la musique...")
    reste_dans_la_piece = True
    choix = ""

    while reste_dans_la_piece not in directions:
        print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
        userInput = input()
        if userInput == "gauche":
            print("\n")
            print("Il y a une vitre, qui donne un aperçu du concert.")
            print("On peut voir les gens bouger, danser et chanter, mais on ne peut pas passer par là.")
        elif userInput == "devant":
            print("\n")
            print("Tu ne peux pas encore passer par là, il fait trop sombre.")
        elif userInput == "droite":
            print("\n")
            print("Il semble que l'accès soit interdit, veux-tu quand même rentrer ?")
            choix = input("(oui) si tu veux entrer et (non) si tu veux éviter : ")
            if choix == "oui":
                print("\n")
                toilette()
            elif choix == "non":
                print("\n")
                print("Tu refuses de rentrer, tu as bien fait !")
        elif userInput == "arriere":
            print("\n")
            concert()
        else:
            print("Tu t'es trompé de commande, utilise les commandes proposées.")

sante_ennemi = 80

def toilette():
    global sante_ennemi

    directions = ["gauche", "droite", "devant", "arriere"]
    print('\n')
    print_color("Tu es entré dans une loge visiteur", "green")
    print("Il fait assez sombre.. Mais on entend de la musique")
    print("Une scène de combat a lieu entre deux fans hystériques juste devant toi ! Ils ne semblent plus eux-mêmes")
    print("...")
  
    reste_dans_la_piece = True
    while reste_dans_la_piece not in directions:
        print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
        userInput = input()
        if userInput == "gauche":
            print("\n")
            print("C'est du sang sur le mur, la bagarre risque de mal tourner si tu n'interviens pas")
        elif userInput == "devant":
            print("\n")
            print_color("Tu décides d'intervenir dans la bagarre !", "yellow")
            combat()
            break
        elif userInput == "droite":
            print("\n")
            print("Il y a du sang sur le sol.. Il faut des preuves ! Prends une photo")
        elif userInput == "arriere":
            print("\n")
            print("Tu est dans une zone de combat, tu a decider precedement d'accepter d'entrer, tu ne peut plus reculer")
        else:
            print("Tu t'es trompé de commande, relie les commandes qui sont proposées.")

def mon_attaque():
    return random.randint(5, 15)

def attaque_de_adversaire():
    return random.randint(3, 10)

def combat():
    notre_sante = 100
    sante_ennemi = 80

    print("Le fan t'insulte il devient fou.. ATTENTION IL ARRIVE !", "red")

    while notre_sante > 0 and sante_ennemi > 0:
        print("\n")
        print("Tu a pas le choix.. Affronte le sinon il va vous tuer tout les deux..")
        print("\n")
        print("Tu choisit quoi ?")
        print_color("1. Coup de poing", "green")
        print_color("2. Fuir", "green")
        print("\n")
        choix = input("Choisit une action : ")

        if choix == "1":

            nos_dommage = mon_attaque()
            sante_ennemi -= nos_dommage
            print(f"Tu lui a mis un coup de poing ! Tu la endommager sa force diminue tu a fait {nos_dommage} points de dégâts à l'ennemi. Santé de l'ennemi : {sante_ennemi}")

            if sante_ennemi <= 0:
                print("\n")
                print_color("L'ennemi est vaincu !", "yellow")
                toilette_apres_combat()
                break

            ennemi_dommage = attaque_de_adversaire()
            notre_sante -= ennemi_dommage
            print("\n")
            print(f"L'ennemi ta mis un coup pied dans la tete et vient de te mettre {ennemi_dommage} points de dégâts. Ton niveau de santé : {notre_sante}")

            if notre_sante <= 0:
                print("\n")
                print_color("Vous êtes vaincu !", "red")
                break

        elif choix == "2":
            print("\n")
            print_color("tu decide de prendre la fuite, tu tourne le dos a ton adversaire", "green")
            print("l'ennemie vient de t'achever au moment ou tu lui a tourner le dos")
            print("La porte etait fermer, il n'y avait aucune issue")
            print("...")
            print_color("La partie s'acheve, car tu a perdu", "green")
            print("")
            quit()

        else:
            print("Choix invalide. Veuillez choisir une action valide.")

    print("C'est la fin du combat, tant pis, mais ne te decourage")


def toilette_apres_combat():
  directions = ["gauche", "droite", "devant", "arriere"]
  print('\n')
  print_color("Tu vient de sauver le fan de sont emprises de cette mysterieuse musique", "green")
  print("Tu a etait brave ce n'etait pas un combat facile")
  print("...")
  print("Mais quelque choses ne tourne pas ronds dans ce concert")
  reste_dans_la_piece = True
  while reste_dans_la_piece not in directions:
    print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
    userInput = input()
    if userInput == "gauche":
      entrer_du_concert()
    elif userInput == "devant":
      deuxieme_part_du_couloir()
    elif userInput == "droite":
      print("\n")
      print("Le mur plafond c'est detruit sur le sol.. trouve une autre issue")
    elif userInput == "arriere":
      print("\n")
      print("La porte est bloquer tu vient de finir ton combat, tu ne peut plus passer par ici")
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def entrer_du_concert():
  directions = ["gauche", "droite", "devant"]
  print('\n')
  print_color("La sécurité a disparue.. Tu est revenu à l'entrer du concert, tout le monde semble avoir disparu..", "yellow")
  print("...")
  reste_dans_la_piece = True
  while reste_dans_la_piece not in directions:
    print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
    userInput = input()
    if userInput == "gauche":
      print("\n")
      print("Il y'a une vitre, qui donne un appercu du concert")
      print("On peut voir les gens bouger, danser et chanter, mais on ne peut pas passer par là.")
    elif userInput == "devant":
      couloir_scene_principal()
    elif userInput == "droite":
      print("\n")
      print("Il y'a un mur qui contient une affiche de la promotion du concert de Carti")
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def couloir_scene_principal():
  directions = ["gauche", "droite", "devant", "arriere"]
  print('\n')
  print("Tu est revenu devant l'entre du couloir")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
    userInput = input()
    if userInput == "gauche":
      entrer_concert()
    elif userInput == "devant":
      deuxieme_part_du_couloir()
    elif userInput == "droite":
      print("\n")
      print("Le mur plafond c'est detruit sur le sol.. trouve une autre issue")
    elif userInput == "arriere":
      print("\n")
      print("La porte est bloquer tu vient de finir ton combat, tu ne peut plus passer par ici")
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def deuxieme_part_du_couloir():
  directions = ["gauche", "droite", "devant", "arriere"]
  print('\n')
  print("Tu a avancer dans la partie ouest du couloir")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
    userInput = input()
    if userInput == "gauche":
      print("\n")
      print("Il y'a un mur par ici, tu ne peut pas passer")
    elif userInput == "devant":
      troisieme_part_du_couloir()
    elif userInput == "droite":
      print("\n")
      print("il y'a un piano par ici, tu  ne peut pas passer")
    elif userInput == "arriere":
      couloir_scene_principal()
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def troisieme_part_du_couloir():
  directions = ["gauche", "droite", "devant", "arriere"]
  print('\n')
  print("Tu a avancer dans la partie Nord Ouest du couloir")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
    userInput = input()
    if userInput == "gauche":
      print("\n")
      print("Sur ta gauche se trouve un mur, tu ne peut donc pas passer par ici")
    elif userInput == "devant":
      print("\n")
      print("Devant toi se trouve un mur, tu pourra donc pas passer par ici")
    elif userInput == "droite":
      quatrieme_part_du_couloir()

    elif userInput == "arriere":
      deuxieme_part_du_couloir()
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def quatrieme_part_du_couloir():
  directions = ["gauche", "droite", "devant", "arriere"]
  print('\n')
  print("Tu avance encore dans le Nord Est du couloir")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
    userInput = input()
    if userInput == "gauche":
      print("\n")
      print("Il y'a un mur, tu ne peut donc pas passer par ici")
    elif userInput == "devant":
      cinquieme_part_du_couloir()
    elif userInput == "droite":
      print("\n")
      print("Il y'a le piano sur ta droite, tu peut pas passer par ici, tu est entrain de faire le tour")
      print("c'est sans doute une bonne idée, ou pas..")
      print("tu est le maitre de ton chemin")
    elif userInput == "arriere":
      troisieme_part_du_couloir()
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def cinquieme_part_du_couloir():
  directions = ["gauche", "droite", "devant", "arriere"]
  print('\n')
  print("Tu avance vers la partie Est du couloir")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
    userInput = input()
    if userInput == "gauche":
      print("\n")
      print("Il y'a un mur, c'est pas possible de passer par ici")
    elif userInput == "devant":
      print("\n")
      print("Devant toi se trouve un mur, tu pourra donc pas passer par ici")
    elif userInput == "droite":
      sixieme_part_du_couloir()
    elif userInput == "arriere":
      quatrieme_part_du_couloir()
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def sixieme_part_du_couloir():
  directions = ["gauche", "droite", "devant", "arriere"]
  print('\n')
  print("Tu avance vers la partie Sud Est du couloir")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
    userInput = input()
    if userInput == "gauche":
      print("\n")
      print("Il y'a un mur, tu peut pas prendre ce chemin")
    elif userInput == "devant":
      septieme_part_du_couloir()
    elif userInput == "droite":
      print("\n")
      print("Il le piano par ici, si tu est ici, c'est que tu est entrain de faire le tour de la piece")
    elif userInput == "arriere":
      cinquieme_part_du_couloir()
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def septieme_part_du_couloir():
    directions = ["gauche", "droite", "devant", "arriere"]
    print('\n')
    print("Tu avances vers la partie du Sud du couloir")
    reste_dans_la_piece = True
    choix = ""

    while reste_dans_la_piece not in directions:
        print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
        userInput = input()
        if userInput == "gauche":
            print("\n")
            print("Il y a une porte avec une serrure.")
            print("Tu vas devoir utiliser la clé de ta voiture pour crocheter l'entrée.")
            choix = input("(oui) si tu veux utiliser ta clé pour crocheter l'entrée et (non) si tu ne veux pas : ")

        if choix == "oui":
            print("\n")
            controle_danger()
        elif choix == "non":
            print("\n")
            print("Tu as refusé d'utiliser ta clé !")
        elif userInput == "devant":
            print("\n")
            print("Il y a un mur par ici, tu ne pourras pas passer.")
        elif userInput == "droite":
            print("\n")
            print("Le plafond s'est effondré sur le sol, tu ne peux pas passer par ici.")
            print("Si tu es arrivé jusqu'ici, c'est que tu as fait le tour de la pièce qui est à moitié détruite.")
        elif userInput == "arriere":
            sixieme_part_du_couloir()
        else:
            print("Tu t'es trompé de commande, utilise les commandes proposées.")

def controle_danger():
  directions = ["-", "+"]
  print('\n')
  print_color("Tu va devoir forcer la serrure avec le coter pointue du dessus de ta clef", "green")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print("Appuie sur le signe (-) de ton clavier pour tourner le dessus de ta clef a gauche")
    print("Ou appuie sur le signe (+) de ton clavier pour tourner le dessus de ta clef a droite")
    userInput = input()
    if userInput == "-":
      diminus_un()
    elif userInput == "+":
      augmentus_un()
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def diminus_un():
  directions = ["-"]
  print('\n')
  print_color("Tu a tourner le coter pointue de ta clef a gauche", "green")
  print("Insiste")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print("Appuie sur le signe (-) de ton clavier pour tourner le dessus de ta clef a gauche")
    userInput = input()
    if userInput == "-":
      diminus_deux()
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def diminus_deux():
  directions = ["-"]
  print('\n')
  print_color("La poignée semble se détendre..", "green")
  print("Insiste")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print("Appuie sur le signe (-) de ton clavier pour tourner le dessus de ta clef a gauche")
    userInput = input()
    if userInput == "-":
      crochet_porte()
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def crochet_porte():
  directions = ["-", "+"]
  print('\n')
  print_color("il semble que lorsque tu tourne à gauche la serrure ne s'ouvre pas", "green")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print("Appuie sur le signe (-) de ton clavier pour tourner le dessus de ta clef a gauche")
    print("Ou appuie sur le signe (+) de ton clavier pour tourner le dessus de ta clef a droite")
    userInput = input()
    if userInput == "-":
      diminus_un()
    elif userInput == "+":
      augmentus_un()
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def augmentus_un():
  directions = ["+"]
  print('\n')
  print_color("Tu a tourner le coter pointue de ta clef a droite", "green")
  print("Insiste")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print("Appuie sur le signe (+) de ton clavier pour tourner le dessus de ta clef a droite")
    userInput = input()
    if userInput == "+":
      augmentus_deux()
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def augmentus_deux():
  directions = ["+"]
  print('\n')
  print_color("La poignée bouge de plus en plus.. Et le verrous se déverouille", "green")
  print("Insiste")
  reste_dans_la_piece = True

  while reste_dans_la_piece not in directions:
    print("Appuie sur le signe (+) de ton clavier pour tourner le dessus de ta clef a droite")
    userInput = input()
    if userInput == "+":
      nouvelle_loge()
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def nouvelle_loge():
    directions = ["gauche", "droite", "devant", "arriere"]
    print('\n')
    print_color("La porte c'est ouverte", "yellow")
    print("Tu es dans la pièce de contrôle, où la sécurité fouille les fans pour voir s'ils ont des objets dangereux, mais il n'y a plus personne. Reste quand même sur tes gardes.")
    reste_dans_la_piece = True
    attempts = 0
    while reste_dans_la_piece not in directions:
        print_color("Voici les commandes disponibles : gauche | droite | devant | arriere", "green")
        userInput = input()
        if userInput == "gauche":
            print("\n")
            print("Il y a une fiche sur le bureau, un numéro est écrit [55]")
        elif userInput == "devant":
            while attempts < 2:
                print("\n")
                print_color("Il semble que la porte devant toi est fermer", "green")
                print("Tu va devoir l'ouvrir, mais tu pourra pas l'ouvrir avec la pointe de ta clef cette fois")
                print("Il va falloir entrer un code pour entrer dans la boutique")
                print("\n")
                code = input("Entrez le code pour accéder à la boutique : ")
                if code == "5511":
                    boutique_souvenir()
                    return
                else:
                    attempts += 1
                    print("\n")
                    print_color("Code incorrect. Attention il ne te reste qu'une tentative.", "red")
                    print("Si tu te trompe encore. Il y'a un gaz toxique de sécurité qui se déclenchera")
            else:
                print_color("Trop de tentatives incorrectes. Le gaz c'est déclencher tu a sucomber à ce gaz.", "red")
                quit()
        elif userInput == "droite":
            print("\n")
            print("Il y a un papier collé au mur, un numéro est écrit [11]")
        elif userInput == "arriere":
            print("\n")
            print("Tu ne peux plus passer par ici")
        else:
            print("Tu t'es trompé de commande, utilise les commandes proposées.")

santé_du_boss = 95
def boutique_souvenir():
  global santé_du_boss
  directions = ["gauche", "droite", "devant", "arriere"]
  print('\n')
  print_color("Bravo ! Tu a reussit à entrer dans la boutique souvenirs", "yellow")
  print("...")
  print("Playboy carti est devant toi, c'est lui aui a causer tout ce tord a tout les fans")
  print("Tu doit le battre pour sauver tout le monde")
  reste_dans_la_piece = True
  while reste_dans_la_piece not in directions:
    print_color("Voici les commandes disponibles: gauche | droite | devant | arriere", "green")
    userInput = input()
    if userInput == "gauche":
      print("\n")
      print("Il y'a des fans ligoter qui te supllient de les liberer.")
      print("Mais pour sa il faut que gagne contre Carti.")
    elif userInput == "devant":
      boss_final()
    elif userInput == "droite":
      print("\n")
      print("Il y'a un mur")
    elif userInput == "arriere":
      print("\n")
      print("Le portail que tu a utiliser a pris feu, c'est carti qui la fait pour etre sur que tu t'echappe pas.")
      print("Tu ne peut plus passer par ici...")
    else:
      print("Tu tes tromper de commande, relie les commandes qui sont proposer.")

def notre_attaque():
    return random.randint(5, 15)

def attaque_du_boss():
    return random.randint(3, 10)

def boss_final():
    ta_santé = 100
    santé_du_boss = 95

    print_color("Carti est dechainer ! Il veut en découdre ! Il te suspecte de saboter sont plan", "yellow")

    while ta_santé > 0 and santé_du_boss > 0:
        print("\n")
        print("Carti est plus fort que les fans que ta affronter..")
        print("\n")
        print("Si tu le bat les fans seront tous libérer de l'emprise magique de sa musique, que choisit tu ?")
        print_color("1. Coup de poing", "green")
        print_color("2. Fuir", "green")
        print("\n")
        choix = input("Choisit une action : ")

        if choix == "1":
            dommage_par_toi = notre_attaque()
            santé_du_boss -= dommage_par_toi
            print(f"Tu lui a mis un coup de poing ! Tu la endommager sa force diminue tu a fait {dommage_par_toi} points de dégâts à l'ennemi. Santé de l'ennemi : {santé_du_boss}")

            if santé_du_boss <= 0:
                print("\n")
                print_color("Tu a enfin battu Carti, les fans sont tous liberer !", "yellow")
                print("Le calme est revenu, les fans reprennent connaissances, le monde sera l'exploit que tu vient de faire")
                credits()
                break

            dommage_par_ennemie = attaque_de_adversaire()
            ta_santé -= dommage_par_ennemie
            print("\n")
            print(f"L'ennemi ta mis un coup pied dans la tete et vient de te mettre {dommage_par_ennemie} points de dégâts. Ton niveau de santé : {ta_santé}")

            if ta_santé <= 0:
                print("\n")
                print_color("Vous êtes vaincu !", "red")
                break

        elif choix == "2":
            print("\n")
            print_color("tu decide de prendre la fuite, tu tourne le dos a ton adversaire", "green")
            print("l'ennemie vient de t'achever au moment ou tu lui a tourner le dos")
            print("La porte etait fermer, il n'y avait aucune issue")
            print("...")
            print_color("La partie s'acheve, car tu a perdu", "green")
            print("")
            quit()

        else:
            print("Choix invalide. Veuillez choisir une action valide.")

    print("Fin du combat.")

def credits():
   print("\n")
   print("Merci d'avoir jouer à notre jeu, ce fut un projet tres passionnant")
   print("Ce jeu a etait fait par Dan, Saïf et Rudy")
   print("Vous avez réussit à passer un certains nombre de defis")
   print("Puis votre réussite et votre patiance face au defis vous ont mener jusqu'au protagoniste de notre jeu")
   print("Vous avez ensuite réussit à battre le Boss et vous avez triompher !")
   print("\n")
   print("Vous pouvez recommencer une partie au menu principal à chaque fois que vous le voudrez, merci")
   menu()

def voiture():
    directions = ["gauche", "droite", "devant"]
    print("\n")
    print_color("Tu a l'interieur de ta voiture", "green")
    print("ta destination s'apelle (concert)")
    print("Mais tu peut choisir d'allez dans d'autre destination")
    print_color("Voici les destination disponible : (Naboo), (Kamino), (Kashyyyk), (Utapau), (station_concert)", "yellow")
    print("tu devra entrer le nom de cette destination pour que le GPS t'indique la destination à prendre pour allez à ton concert")
    print("\n")
    print_color("GPS : Bonjour, veuillez entrer la destination ou vous souhaiter allez ?", "yellow")
    name = input()
    print_color("Parfait, je vous emmene à votre destination" +name+ " je sais que tu fera le bon choix.", "yellow")
    print_color("Voici les commandes disponibles: gauche | droite | devant", "green")

def print_color(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }

    if color in colors:
        print(f"{colors[color]}{text}{colors['reset']}")
    else:
        print(text)

def afficher_menu():
    print('\n')
    print_color("=== MENU PRINCIPAL ===", "yellow")
    print_color("1. Nouvelle partie (Commencer l'aventure)", "blue")
    print_color("4. Quitter", "red")

def menu():
    while True:
        afficher_menu()
        print('\n')
        choix = input("Choisissez une option : ")

        if choix == "1":
            print("Génial ! Tu a choisit de débuter une nouvelle partie.")
            print("\n")
            print_color("Bienvenu sur (Survivre au concert de Playboi Carti)", "green")
            print("Tu est un fan de playboi carti, tu assiste à sont concert, le public est venu nombreux.")
            print("Quand tout à coup, le concert tourne au drame, le public fini par etre controler par le son.")
            print("Le Volume augmente, tu doit retrouver ton chemin, la music a changer les fans qui t'attaque.")
            print("Esque Playboi carti savais ce qu'il fesait ? Qu'a t-il fait ? Controle t-il le public ?")
            print("...")
            print("C'est a toi de le decouvrir, resous cette énigme, fouille le concert")
            print("Evite les piéges, cherche des preuves, trouve sa loge puis affronte le.")
            print("Pour parcourir librement le stade ou se deroule le concert, il te faudra un nom")
            print_color("Commence par te crée un nom: ", "green")
            name = input()
            print('\n')
            print_color("Bon bah.. Bonne chance, " +name+ " je sais que tu fera le bon choix.", "green")
            print("\n")
            debut_de_notre_jeu()
            print('\n')

        elif choix == "2":
            print("Au revoir !")
            quit()

        else:
            print("Choix invalide. Veuillez choisir une option valide.")
            print('\n')

menu()
