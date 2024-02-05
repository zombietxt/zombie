import random

def kampf(player_life, zombie_life):
    print("******************")
    print("Der Kampf beginnt!")
    print("Player life: ", player_life)
    print("Zombie life: ", zombie_life)
    print("-----------------------------------------------")    
    for i in range(0, 5):
        human_attack = random.random() * 9 + 1
        zombie_life = zombie_life - human_attack
        print("Zwischen human und zombie random")
        print("Human attack: ", human_attack)
        zombie_attack = random.random() * 9 + 1
        print("Zombie attack: ", zombie_attack)
        print("-----------------------------------------------")
        player_life = player_life - zombie_attack
        print("Player life: ", player_life)
        print("Zombie life: ", zombie_life)    
    return player_life, zombie_life  # Diese Zeile wurde geändert

print("############")
print("Hello Zombie")
print("############")

# Die zurückgegebenen Werte von kampf() werden hier gespeichert
#player_life, zombie_life = kampf(100, 100)
player_l, zombie_l = kampf(100, 100)

print("------------Nach Kampf-----------------------------------")
print("Player life: ", player_l)
print("Zombie life: ", zombie_l)
kampf(player_l, zombie_l)
kampf(player_l, zombie_l)
