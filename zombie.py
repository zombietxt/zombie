import random

def kampf(player_life, zombiel_ife):
	print("Der Kampf beginnt!")
	human_attack = random.random() * 9 + 1
	zombiel_HP = zombie_life - human_attack
	
	zombie_attack = random.random() * 9 + 1
	humanHP = human_life - zombie_attack
	
	print("Player HP: ", human_HP)
	print ("Zombie HP: ", zombie_HP)
	

print("Hello World!")
human_attack = 0
zombie_attack = 0
player_life = 0
zombie_life = 0
human_life = 0
human_HP = 0
zombie_HP = 0

kampf(100,100)
