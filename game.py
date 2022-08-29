import time
import threading


class inventory():
    stone = 0
    wood = 0
    fer = 0
    gold = 0
    diamond = 0


class player():
    pickaxe = 0
    sword = 0
    armor = 0
    ring = 0
    health = 100
    energy = 20


class enemy():
    rang = 0
    tour = 0
    health = 25
    attack = 1


def energy():
    while (True):
        if (player.energy != (20 + player.ring)):
            player.energy += 1
        if (player.health != (100 + (player.armor * 10))):
            player.health += 10
        time.sleep(60)


def mine():
    if (player.energy != 0):
        player.energy -= 1
        if (player.pickaxe == 0):
            inventory.stone += 1
            print("Stone +1 !")
        if (player.pickaxe == 1):
            inventory.stone += 2
            print("Stone +2 !")
            inventory.fer += 1
            print("Fer +1 !")
        if (player.pickaxe == 2):
            inventory.stone += 3
            print("Stone +3 !")
            inventory.fer += 2
            print("Fer +2 !")
        if (player.pickaxe == 3):
            inventory.stone += 4
            print("Stone +4 !")
            inventory.fer += 3
            print("Fer +3 !")
            inventory.gold += 1
            print("Gold +1 !")
        if (player.pickaxe == 4):
            inventory.stone += 5
            print("Stone +5 !")
            inventory.fer += 4
            print("Fer +4 !")
            inventory.gold += 2
            print("Gold +2 !")
        if (player.pickaxe == 5):
            inventory.stone += 6
            print("Stone +6 !")
            inventory.fer += 5
            print("Fer +5 !")
            inventory.gold += 3
            print("Gold +3 !")
            inventory.diamond += 1
            print("Diamond +1 !")
        main()
    else:
        print("Vous n'avez pas assez d'énergie")
        main()


def craft(item, value):
    if (item == "pickaxe"):
        if (value == "1"):
            if (inventory.stone >= 1 and inventory.wood >= 1):
                player.pickaxe = 1
                inventory.stone -= 1
                inventory.wood -= 1
                print("Vous avez craft un pickaxe")
                main()
            else:
                print("Vous n'avez pas assez de ressources (1 Stone + 1 Wood)")
                main()
        if (value == "2"):
            if (inventory.stone >= 3 and inventory.wood >= 5 and inventory.fer >= 1):
                player.pickaxe = 2
                inventory.stone -= 3
                inventory.wood -= 5
                inventory.fer -= 1
                print("Vous avez craft un pickaxe")
                main()
            else:
                print("Vous n'avez pas assez de ressources (3 Stones + 5 Wood + 1 Fer)")
                main()
        if (value == "3"):
            if (inventory.stone >= 5 and inventory.wood >= 8 and inventory.fer >= 3):
                player.pickaxe = 3
                inventory.stone -= 5
                inventory.wood -= 8
                inventory.fer -= 3
                print("Vous avez craft un pickaxe")
                main()
            else:
                print("Vous n'avez pas assez de ressources (5 Stones + 8 Wood + 3 Fer)")
                main()
        if (value == "4"):
            if (inventory.stone >= 10 and inventory.wood >= 12 and inventory.fer >= 5 and inventory.gold >= 1):
                player.pickaxe = 4
                inventory.stone -= 10
                inventory.wood -= 12
                inventory.fer -= 5
                inventory.gold -= 1
                print("Vous avez craft un pickaxe")
                main()
            else:
                print("Vous n'avez pas assez de ressources (10 Stones + 12 Wood + 5 Fer + 1 Gold)")
                main()
        if (value == "5"):
            if (inventory.stone >= 20 and inventory.wood >= 20 and inventory.fer >= 10 and inventory.gold >= 3):
                player.pickaxe = 5
                inventory.stone -= 20
                inventory.wood -= 20
                inventory.fer -= 10
                inventory.gold -= 3
                print("Vous avez craft un pickaxe")
                main()
            else:
                print("Vous n'avez pas assez de ressources (20 Stones + 20 Wood + 10 Fer + 3 Gold)")
                main()
    if (item == "armor"):
        if (value == "1"):
            if (inventory.stone >= 1 and inventory.wood >= 1):
                player.armor = 1
                inventory.stone -= 1
                inventory.wood -= 1
                print("Vous avez craft une armure")
                main()
            else:
                print("Vous n'avez pas assez de ressources")
                main()
        if (value == "2"):
            if (inventory.stone >= 4 and inventory.wood >= 2 and inventory.fer >= 1):
                player.armor = 2
                inventory.stone -= 4
                inventory.wood -= 2
                inventory.fer -= 1
                print("Vous avez craft une armure")
                main()
            else:
                print("Vous n'avez pas assez de ressources (4 Stones + 2 Wood + 1 Fer)")
                main()
        if (value == "3"):
            if (inventory.stone >= 10 and inventory.wood >= 8 and inventory.fer >= 5):
                player.armor = 3
                inventory.stone -= 10
                inventory.wood -=  8
                print("Vous avez craft une armure")
                main()
            else:
                print("Vous n'avez pas assez de ressources (10 Stones + 8 Wood + 5 Fer)")
                main()
        if (value == "4"):
            if (inventory.stone >= 20 and inventory.wood >= 12 and inventory.fer >= 10 and inventory.gold >= 3):
                player.armor = 4
                inventory.stone -= 20
                inventory.wood -= 12
                inventory.fer -= 10
                inventory.gold -= 3
                print("Vous avez craft une armure")
                main()
            else:
                print("Vous n'avez pas assez de ressources (20 Stones + 12 Wood + 10 Fer + 3 Gold)")
                main()
        if (value == "5"):
            if (inventory.stone >= 35 and inventory.wood >= 25 and inventory.fer >= 20 and inventory.gold >= 10):
                player.armor = 5
                inventory.stone -= 35
                inventory.wood -= 25
                inventory.fer -= 20
                inventory.gold -= 10
                print("Vous avez craft une armure")
                main()
            else:
                print("Vous n'avez pas assez de ressources (35 Stones + 25 Wood + 20 Fer + 10 Gold)")
                main()
    if (item == "sword"):
        if (value == "1"):
            if (inventory.stone >= 2 and inventory.wood >= 4):
                player.sword = 1
                inventory.stone -= 2
                inventory.wood -= 4
                print("Vous avez craft une épée")
                main()
            else:
                print("Vous n'avez pas assez de ressources (2 Stones + 4 Wood)")
                main()
        if (value == "2"):
            if (inventory.stone >= 8 and inventory.wood >= 15 and inventory.fer >= 5):
                player.sword = 2
                inventory.stone -= 8
                inventory.wood -= 15
                inventory.fer -= 5
                print("Vous avez craft une épée")
                main()
            else:
                print("Vous n'avez pas assez de ressources (8 Stones + 15 Wood + 5 Fer)")
                main()
        if (value == "3"):
            if (inventory.stone >= 15 and inventory.wood >= 30 and inventory.fer >= 10):
                player.sword = 3
                inventory.stone -= 15
                inventory.wood -= 30
                inventory.fer -= 10
                print("Vous avez craft une épée")
                main()
            else:
                print("Vous n'avez pas assez de ressources (15 Stones + 30 Wood + 10 Fer)")
                main()
        if (value == "4"):
            if (inventory.stone >= 25 and inventory.wood >= 45 and inventory.fer >= 20 and inventory.gold >= 5):
                player.sword = 4
                inventory.stone -= 25
                inventory.wood -= 45
                inventory.fer -= 20
                inventory.gold -= 5
                print("Vous avez craft une épée")
                main()
            else:
                print("Vous n'avez pas assez de ressources (25 Stones + 45 Wood + 20 Fer + 5 Gold)")
                main()
        if (value == "5"):
            if (inventory.stone >= 30 and inventory.wood >= 60 and inventory.fer >= 30 and inventory.gold >= 10 and inventory.diamond >= 1):
                player.sword = 5
                inventory.stone -= 30
                inventory.wood -= 60
                inventory.fer -= 30
                inventory.gold -= 10
                inventory.diamond -= 1
                print("Vous avez craft une épée")
                main()
            else:
                print("Vous n'avez pas assez de ressources (30 Stones + 60 Wood + 30 Fer + 10 Gold + 1 Diamond)")
                main()
    if (item == "ring"):
        if (value == "1"):
            if (inventory.stone >= 5 and inventory.wood >= 5):
                player.ring = 1
                inventory.stone -= 5
                inventory.wood -= 5
                print("Vous avez craft un anneau")
                main()
            else:
                print("Vous n'avez pas assez de ressources (5 Stones + 5 Wood)")
                main()
        if (value == "2"):
            if (inventory.stone >= 8 and inventory.wood >= 8):
                player.ring = 2
                inventory.stone -= 2
                inventory.wood -= 2
                print("Vous avez craft un anneau")
                main()
            else:
                print("Vous n'avez pas assez de ressources (8 Stones + 8 Wood)")
                main()
        if (value == "3"):
            if (inventory.stone >= 15 and inventory.wood >= 15):
                player.ring = 3
                inventory.stone -= 3
                inventory.wood -= 3
                print("Vous avez craft un anneau")
                main()
            else:
                print("Vous n'avez pas assez de ressources (15 Stones + 15 Wood)")
                main()
        if (value == "4"):
            if (inventory.stone >= 20 and inventory.wood >= 20):
                player.ring = 4
                inventory.stone -= 4
                inventory.wood -= 4
                print("Vous avez craft un anneau")
                main()
            else:
                print("Vous n'avez pas assez de ressources (20 Stones + 20 Wood)")
                main()
        if (value == "5"):
            if (inventory.diamond >= 10):
                player.ring = 5
                inventory.diamond -= 10
                print("Vous avez craft un anneau")
                main()
            else:
                print("Vous n'avez pas assez de ressources (10 Diamonds)")
                main()


def chop():
    if (player.energy != 0):
        player.energy -= 1
        if (player.pickaxe == 0):
            inventory.wood += 1
            print("Wood +1 !")
        if (player.pickaxe == 1):
            inventory.wood += 2
            print("Wood +2 !")
        if (player.pickaxe == 2):
            inventory.wood += 3
            print("Wood +3 !")
        if (player.pickaxe == 3):
            inventory.wood += 4
            print("Wood +4 !")
        if (player.pickaxe == 4):
            inventory.wood += 5
            print("Wood +5 !")
        if (player.pickaxe == 5):
            inventory.wood += 6
            print("Wood +6 !")
    main()


def inventoryshow():
    print("Ressources:")
    print("Stone : " + str(inventory.stone))
    print("Wood : " + str(inventory.wood))
    print("Fer : " + str(inventory.fer))
    print("Gold : " + str(inventory.gold))
    print("Diamond : " + str(inventory.diamond))
    print(" ")
    print("Outils:")
    print("Pickaxe : " + str(player.pickaxe))
    print("Sword : " + str(player.sword))
    print("Armor : " + str(player.armor))
    print("Ring : " + str(player.ring))
    print(" ")
    print("Stats:")
    print("Health : " + str(player.health) + "/" + str(100 + (player.armor * 10)) + " hp (+10/minute)")
    print("Energy : " + str(player.energy) + "/" + str(20 + player.ring) + " energy (+1/minute)")
    print("Damage : " + str(player.sword) + " damage")
    main()


def attack():
    battle()


def battle():
    for k in range(1000):
        if(player.health >= 0):
            if(enemy.health >= 0):
                player.health -= enemy.attack
                print(f'\x1b[6;35;31m' + "TOUR " + str(enemy.tour) + ": L'ennemi vous inflige " + str(
                    enemy.attack) + " dommages" + " Vous avez " + str(player.health) + " hp restants." + '\x1b[0m')
                enemy.health -= player.sword
                print(f'\x1b[6;35;32m' + "TOUR " + str(enemy.tour) + ": Vous infligez " + str(
                    player.sword) + " dommages" + " L'ennemi a " + str(
                    enemy.health) + " hp restants." + '\x1b[0m')
                enemy.tour += 1
    if (player.health <= 0):
        print(f'\x1b[6;35;91m' + "Vous avez perdu." + '\x1b[0m')
        player.health = 1
        main()

    if (enemy.health <= 0):
        print(f'\x1b[6;35;92m' + "Vous avez gagné !" + '\x1b[0m')
        if (enemy.rang == 5):
            print("Vous avez gagné contre le jeu !")
            print("Le jeu va se fermer dans 5 secondes")
            time.sleep(5)
            exit()




        else:
            print(
                "L'ennemi monte au niveau suppérieur ! Vous devez le battre dans sa 5 pour gagner le jeu." + " Phase battu: " + str(
                    enemy.rang))
            enemy.tour = 0
            enemy.rang += 1
            time.sleep(1)
            enemy.health = 100
            enemy.attack = 1 + (enemy.rang * 1)
            main()
    main()





# // LANCEMENT DU JEU //



print(f'\x1b[6;35;41m' + "Bienvenue dans le jeu !" + '\x1b[0m')
print("")


def main():
    print(" ")
    action = input(f'\x1b[6;35;92m' " Que voulez-vous faire ?  >>> " + '\x1b[0m')
    if (action == "mine"):
        mine()
    if (action == "craft"):
        item = input(f'\x1b[6;35;93m' + "Quel item voulez-vous craft ? (pickaxe, sword, armor, ring) >>> " + '\x1b[0m')
        rang = input(f'\x1b[6;35;93m' + "Quel rang voulez-vous ?  >>> ")
        craft(item, rang)
    if (action == "inventory"):
        inventoryshow()
    if (action == "exit"):
        exit()
    if (action == "attack"):
        attack()
    if (action == "chop"):
        chop()
    if (action == "credit"):
        print(f'\x1b[7m' + "Jeu créé par: Azrotho dans une durée de 2h !" + '\x1b[0m')
        main()
    if (action == "help"):
        print("Liste des commandes:")
        print(" ")
        print("mine : Mine un bloc de pierre")
        print("chop : Coupe un arbre")
        print("craft : Craft un item")
        print("inventory : Affiche l'inventaire")
        print("attack : Attaque un ennemi")
        print("credit : Affiche les crédits")
        print("exit : Quitte le jeu")
        main()
    print(f'\x1b[6;35;95m' + "Commande inconnue, faites help pour voir la liste des commandes" + '\x1b[0m')
    main()


thE = threading.Thread(target=energy)
thE.start()
main()