#!/bin/bash

#Just in case..
unset DHCP

# 'Option' Variable for also setting up the DHCP server on the device
# Uncommnent to disable (not install/configure DHCP bits)
DHCP=true

# Packages for Bluetooth Bridge:
echo "Installing Bluetooth-Ethernet Bridge Packages..."
sudo apt-get install -qq --force-yes bluetooth dbus bluez bridge-utils python-bluez python-dbus

if [ $DHCP ]; then
	# Packages for DHCP, if option is set:
	echo "Installing DHCP Server Packages..."
	sudo apt-get install -qq --force-yes isc-dhcp-server bind9

	# # Webmin stuff; first adding the repo for Webmin:
	# sudo -s
	# sudo echo "#" >>/etc/apt/sources.list
	# sudo echo "#Webmin Repo Stuff:" >> /etc/apt/sources.list
	# sudo echo "deb http://download.webmin.com/download/repository sarge contrib" >> /etc/apt/sources.list
	# sudo echo "deb http://webmin.mirror.somersettechsolutions.co.uk/repository sarge contrib" >> /etc/apt/sources.list
	# exit

	# # Now update package listings...
	# wget -q http://www.webmin.com/jcameron-key.asc -O- | sudo apt-key add -
	# sudo apt-get update -qq

	# # Finally, install Webmin:
	# echo "Installing Webmin..."
	# sudo apt-get install -qq --force-yes webmin
fi

