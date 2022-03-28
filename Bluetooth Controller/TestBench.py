# import sys
# import glob
# import serial
#
#
# def serial_ports():
#     """ Lists serial port names
#
#         :raises EnvironmentError:
#             On unsupported or unknown platforms
#         :returns:
#             A list of the serial ports available on the system
#     """
#     if sys.platform.startswith('win'):
#         ports = ['COM%s' % (i + 1) for i in range(256)]
#     elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
#         # this excludes your current terminal "/dev/tty"
#         ports = glob.glob('/dev/tty[A-Za-z]*')
#     elif sys.platform.startswith('darwin'):
#         ports = glob.glob('/dev/tty.*')
#     else:
#         raise EnvironmentError('Unsupported platform')
#
#     result = []
#     for port in ports:
#         try:
#             s = serial.Serial(port)
#             s.close()
#             result.append(port)
#         except (OSError, serial.SerialException):
#             pass
#     return result
#
#
# if __name__ == '__main__':
#     print(serial_ports())

import bluetooth


def listMAC():  # prints out all bluetooth devices on the system
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
        print("name:", name)
        print("address:", addr)

    return target_address
# listMAC()


def MACmenu():
    target = {}  # holds the key:value pairs for the names and targets
    indexLookup = []
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    i = 0

    # col_width = max(len(word) for name in nearby_devices for word in name) + 2  # padding
    for addr, name in nearby_devices:
        print("[" + str(i) + "]", "Name:", "{:<20}".format(name), "\taddress:", addr)
        indexLookup.append(name)
        target[name] = addr
        i = i + 1

    selection = input("Selection:\t")  # passes back the index of the selection)

    return target[indexLookup[int(selection)]]  # return the value specified by user


my_addr = MACmenu()
print(my_addr)