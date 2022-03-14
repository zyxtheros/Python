try:
	import bluetooth

except ImportError:
	None

def MAChelp():
	def __init__(self):


	def listMAC(): # prints out all bluetooth devices on the system
		print("Looking for Bluetooth devices...")
		nearby_devices = bluetooth.discover_devices(lookup_names=True)

		for addr, name in nearby_devices:
			print("name:", name)
			print("address:", addr)

	def getMAC(target_name):
		nearby_devices = bluetooth.discover_devices(lookup_names=True)

		for addr, name in nearby_devices:
			if name == target_name:
				target_address = addr
			# print("name:", name)
			# print("address:", addr)

		return target_address

	def checkMAC(self, target_address, target_name = "DEFAULT"):
		nearby_devices = bluetooth.discover_devices()

		for bdaddr in nearby_devices:
			if target_name == bluetooth.lookup_name(bdaddr):
				target_address = bdaddr
				break

		if target_address is not None:
			print("found target bluetooth device with address ", target_address)
		else:
			print("could not find target bluetooth device nearby")

	def MACmenu():
		target = {} # holds the key:value pairs for the names and targets
		indexLookup = []
		nearby_devices = bluetooth.discover_devices(lookup_names=True)
		i=0
		for addr, name in nearby_devices:
			print("["+str(i)+"]", "name:", name, "\taddress:", addr)
			indexLookup.append(name)
			target[name] = addr
			i=i+1

		selection = input("Selection:\t") # passes back the index of the selection)

		return target[indexLookup[selection]] # return the value specified by user
