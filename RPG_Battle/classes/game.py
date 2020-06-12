import random
from classes.magic import Spell


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
		self.max_HP = HP
		self.HP = HP
		self.max_MP = MP
		self.MP = MP
		self.ATK_HIGH = ATK + 10
		self.ATK_LOW = ATK - 10
		self.DEF = DEF
		self.magic = magic
		self.items = items
		self.action = ["Attack", "Magic", "Items"]

	def gen_damage(self):
		return random.randrange(self.ATK_LOW, self.ATK_HIGH)

	def heal(self, dmg):
		self.HP += dmg
		if self.HP > self.max_HP:
			self.HP = self.max_HP

	def take_dmg(self, dmg):
		self.HP -= dmg
		if self.HP < 0:
			self.HP = 0
		return self.HP

	def get_HP(self):
		return self.HP

	def get_max_HP(self):
		return self.max_HP

	def get_MP(self):
		return self.MP

	def get_max_MP(self):
		return self.max_MP

	def reduce_MP(self, cost):
		self.MP -= cost

	def choose_action(self):
		i = 1
		print(bcolors.BOLD + self.name + bcolors.ENDC)
		print("ACTIONS")
		for item in self.action:
			print("\t" + str(i) + ":", item)
			i += 1

	def choose_magic(self):
		i = 1
		print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGIC" + bcolors.ENDC)
		for spell in self.magic:  # acces n elements, use for spell in self.magic[o:n]
			print("\t" + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
			i += 1

	def get_stats(self):
		print("				    _________________________           __________")
		print(bcolors.BOLD + self.name + "   " +
			  str(self.HP) + "/" + str(self.max_HP) + " |" + bcolors.OKGREEN + "███                      "
			  + bcolors.ENDC
			  + bcolors.BOLD + "|   " + str(self.MP) + "/" + str(self.max_MP) + " |" + bcolors.OKBLUE + "███       "
			  + bcolors.ENDC + bcolors.BOLD + "|" + bcolors.ENDC)

	def get_stats_header(self):
		print("NAME				HP								     MP")