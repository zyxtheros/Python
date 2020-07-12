from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create some Items
potion = ("Potion", "potion", "Heals 50 HP", 50)
hipotion = ("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = ("Super Potion", "potion", "Heals 100 HP", 1000)
elixir = ("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
megaelixir = ("Mega Elixir", "elixir", "Fully restores party HP/MP", 9999)
grenade = ("Grenade", "attack", "Deals 500 DMG", 500)

player_magic = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15},
				{"item": hipotion, "quantity": 5},
				{"item": superpotion, "quantity": 5},
				{"item": elixir, "quantity": 5},
				{"item": megaelixir, "quantity": 2},
				{"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person("Valos:", 1260, 60, 300, 34, player_magic, player_items)
player2 = Person("Nick :", 4160, 90, 311, 34, player_magic, player_items)
player3 = Person("Robot:", 3089, 80, 288, 34, player_magic, player_items)
enemy   = Person("Magus",  1200, 150, 701, 25, [], [])

players = {player1, player2, player3}

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN  ENEMY ATTACKS!!" + bcolors.ENDC)
while running:
	print("-------------------------------------------------------------------")
	player1.get_stats_header()
	for player in players:
		player.get_stats()
	print(" ")

	for player in players:

		player.choose_action()
		choice = input("Choose action: ")
		index = int(choice) - 1

		if index == 0:
			dmg = player.gen_damage()
			enemy.take_dmg(dmg)
			print("You strike for", dmg)

		elif index == 1:
			player.choose_magic()
			magic_choice = int(input("Choose magic: ")) - 1

			if magic_choice == -1:  # Return to main menu
				continue

			spell = player.magic[magic_choice]
			magic_dmg = player.magic[magic_choice].gen_dmg()

			magic_dmg = spell.gen_dmg() # randomize the magic damage using .gem_dmg()
			cost = spell.cost

			current_MP = player.get_MP()

			if spell.cost > current_MP:
				print(bcolors.FAIL + "\nInsufficient MP\n" + bcolors.ENDC)
				continue

			player.reduce_MP(spell.cost)

			if spell.type == "white":  # if the player selects a heal type spell
				player.heal(magic_dmg)
				print(bcolors.OKBLUE + "\n" + spell.name + " Heals for", str(magic_dmg), "HP" + bcolors.ENDC)
			elif spell.type == "black":
				enemy.take_dmg(magic_dmg)
				print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of dmg", bcolors.ENDC)

		elif index == 2:
			player.choose_item()
			item_choice = int(input("Choose item: ")) - 1

			if item_choice == -1:  # Return to main menu
				continue

			item = player.items[item_choice]["item"]

			if player.items[item_choice]["quantity"] == 0:
				print(bcolors.FAIL + "\n" + "none left..." + bcolors.ENDC)
				continue

			player.items[item_choice]["quantity"] -= 1

			if item.type == "potion":
				player.heal(item.prop)
				print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)

			elif item.type == "elixir":
				player.HP = player.max_HP
				player.MP = player.max_MP
				print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)

			elif item.type == "attack":
				enemy.take_dmg(item.prop)
				print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of DMG" + bcolors.ENDC)

	enemy_choice = 1
	enemy_dmg = enemy.gen_damage()
	player1.take_dmg(enemy_dmg)

	print("----------------------------------")
	print("Enemy HP:" + bcolors.FAIL + str(enemy.get_HP()) + "/" + str(enemy.get_max_HP()) + bcolors.ENDC + "\n")
	print("Player HP:" + bcolors.OKGREEN + str(player.get_HP()) + "/" + str(player.get_max_HP()) + bcolors.ENDC)
	print("Player MP:" + bcolors.OKBLUE + str(player.get_MP()) + "/" + str(player.get_max_MP()) + bcolors.ENDC + "\n")

	print("----------------------------------")
	print("Enemy strikes for", str(enemy_dmg) + ".\nYour HP:", player.get_HP())

	if enemy.get_HP() == 0:
		print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)

	elif player.get_HP() == 0:
		print(bcolors.FAIL + "Enemy has defeated you. You lose :(" + bcolors.ENDC)
		running = False
