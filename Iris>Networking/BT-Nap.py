#!/usr/bin/python

#Modified By Babu To Prevent Timeouts
#Based on BlueZ Script For NAP Functionality
#This script is intended for BlueZ Version 5 or higher and DBUS Version 4 or higher

from __future__ import absolute_import, print_function, unicode_literals

from optparse import OptionParser, make_option
import sys
import time
import dbus

SERVICE_NAME = "org.bluez"
ADAPTER_INTERFACE = SERVICE_NAME + ".Adapter1"
DEVICE_INTERFACE = SERVICE_NAME + ".Device1"

def get_managed_objects():
	bus = dbus.SystemBus()
	manager = dbus.Interface(bus.get_object("org.bluez", "/"),
				"org.freedesktop.DBus.ObjectManager")
	return manager.GetManagedObjects()

def find_adapter(pattern=None):
	return find_adapter_in_objects(get_managed_objects(), pattern)

def find_adapter_in_objects(objects, pattern=None):
	bus = dbus.SystemBus()
	for path, ifaces in objects.iteritems():
		adapter = ifaces.get(ADAPTER_INTERFACE)
		if adapter is None:
			continue
		if not pattern or pattern == adapter["Address"] or \
							path.endswith(pattern):
			obj = bus.get_object(SERVICE_NAME, path)
			return dbus.Interface(obj, ADAPTER_INTERFACE)
	raise Exception("Bluetooth adapter not found")

bus = dbus.SystemBus()

option_list = [
		make_option("-i", "--device", action="store",
				type="string", dest="dev_id"),
		]
parser = OptionParser(option_list=option_list)

(options, args) = parser.parse_args()

adapter_path = find_adapter(options.dev_id).object_path
server = dbus.Interface(bus.get_object("org.bluez", adapter_path),
						"org.bluez.NetworkServer1")

service = "nap"

if (len(args) < 1):
	bridge = "tether"
else:
	bridge = args[0]

server.Register(service, bridge)

print("Server for %s registered for %s" % (service, bridge))

raw_input("Press <Enter> to disconnect")

server.Unregister(service)
