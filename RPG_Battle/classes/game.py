import random
from classes.magic import Spell
from classes.inventory import Item


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'  # end color use
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


class Person:
	def __init__(self, name, HP, MP, ATK, DEF, magic, items):
		self.name = name
		self.max_HP = HP # Person Max Health
		self.HP = HP # Person Health
		self.max_MP = MP # Person Max Mana
		self.MP = MP # Person Mana
		self.ATK_HIGH = ATK + 10 # Lower attack limit
		self.ATK_LOW = ATK - 10 # Upper attack limit
		self.DEF = DEF # Person Defense
		self.magic = magic # Person magic library
		self.items = items # Person item library
		self.action = ["Attack", "Magic", "Items"] # valid action types

	def gen_damage(self): # generate a randomized damage value
		return random.randrange(self.ATK_LOW, self.ATK_HIGH)

	def heal(self, dmg): # Increase Person HP
		self.HP += dmg
		if self.HP > self.max_HP: # Ensure HP cannot exceed max HP
			self.HP = self.max_HP

	def take_dmg(self, dmg): # decrease the Person's health
		self.HP -= dmg
		if self.HP < 0:
			self.HP = 0
		return self.HP

	def get_HP(self): # return the HP of the Person
		return self.HP

	def get_max_HP(self): # return the maximum HP of the Person
		return self.max_HP

	def get_MP(self): # return the MP of the Person
		return self.MP

	def get_max_MP(self): # return the maximum MP of the Person
		return self.max_MP

	def reduce_MP(self, cost): # Decrease Person MP
		self.MP -= cost

	def choose_action(self): # Action selection menu
		i = 1
		print(bcolors.BOLD + "    " + self.name + bcolors.ENDC)
		print(bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS" + bcolors.ENDC)
		for item in self.action:
			print("\t    " + str(i) + ":", item)
			i += 1

	def choose_magic(self): # Magic selection menu
		i = 1
		print(bcolors.OKBLUE + bcolors.BOLD + "    MAGIC" + bcolors.ENDC)
		for spell in self.magic:  # acces n elements, use for spell in self.magic[o:n]
			print("\t    " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
			i += 1

	def choose_item(self): # Item selection menu
		i = 1
		for item in self.items:
			print("\t    " + str(i) + ".", item.name, "(desc:", str(item.description) + ")")
			i += 1

	def get_enemy_stats(self): # Enemy HP readout
		HP_bar_len = 50  # number of characters wide the HP bar will be
		HP_bar = ""
		bar_ticks = (self.HP / self.max_HP) * HP_bar_len

		while bar_ticks > 0:
			HP_bar += "█"  # add fill
			bar_ticks -= 1

		while len(HP_bar) < HP_bar_len:
			HP_bar += " "  # add whitespace

		HP_buffer = ""
		if len(str(self.max_HP)) > len(str(self.HP)):  # compare the length of HP vs. max HP
			while len(str(self.max_HP)) > (len(str(self.HP)) + len(HP_buffer)):
				HP_buffer += " "  # add a space to make HP have the same number of characters as max HP

		print("			    	_________________________           __________")
		print(bcolors.BOLD + self.name + "   " + HP_buffer + str(self.HP) + "/" + str(self.max_HP) + " |"
			+ bcolors.OKGREEN + HP_bar + bcolors.ENDC + bcolors.BOLD + "|" + bcolors.ENDC)

	def get_stats(self): # Person HP/MP readout
		HP_bar_len = 25  # number of characters wide the HP bar will be
		MP_bar_len = 10  # number of characters wide the MP bar will be
		HP_bar = ""
		MP_bar = ""

		bar_ticks = (self.HP / self.max_HP) * HP_bar_len
		while bar_ticks > 0:
			HP_bar += "█"  # add fill
			bar_ticks -= 1

		while len(HP_bar) < HP_bar_len:
			HP_bar += " "  # add whitespace

		bar_ticks = (self.MP / self.max_MP) * MP_bar_len
		while bar_ticks > 0:
			MP_bar += "█"  # add fill
			bar_ticks -= 1

		while len(MP_bar) < MP_bar_len:
			MP_bar += " "  # add whitespace

		HP_buffer = ""  # string to make HP have the same number of characters as max HP
		if len(str(self.max_HP)) > len(str(self.HP)):  # compare the length of HP vs. max HP
			while len(str(self.max_HP)) > (len(str(self.HP)) + len(HP_buffer)):
				HP_buffer += " "  # add a space to make HP have the same number of characters as max HP

		MP_buffer = ""  # string to make MP have the same number of characters as max MP
		if len(str(self.max_MP)) > len(str(self.MP)):  # compare the length of MP vs. max MP
			while len(str(self.max_MP)) > (len(str(self.MP)) + len(MP_buffer)):  # test the length of max MP vs. MP + buffer
				HP_buffer += " "  # add a space to make MP have the same number of characters as max MP

		print("			    	_________________________           __________")
		print(bcolors.BOLD + self.name + "   "
			+ HP_buffer + str(self.HP) + "/" + str(self.max_HP)
			+ " |" + bcolors.OKGREEN + HP_bar + bcolors.ENDC + bcolors.BOLD + "|   "
			+ MP_buffer + str(self.MP) + "/" + str(self.max_MP)
			+ " |" + bcolors.OKBLUE + MP_bar + bcolors.ENDC + bcolors.BOLD + "|" + bcolors.ENDC)

	def get_stats_header(self): # Stats readout Header Bar
		print("NAME				HP								     MP")
