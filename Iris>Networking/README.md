## Networking (Codename: Zephyrus) ##

This contains all the config files and scripts needed to make a Bluetooth NAP on a Raspberry Pi for use with the rest of Iris OR independent of Iris.

The steps and scripts included below are largely borrowed from Rahul Rameshbabu's work on the BT <-> Ethernet Bridge for the Scouting App; the changes here allow for a single seat installation (no separate computer for the DHCP server), removed the need for bluezutils.py, and allow the network to be run as a SystemD service. Eventually some of these changes may be backported to Rameshbabu's repo as well.

### Setup ###
1.	Run the setup script to install all the necessary packages.
2.	Update /etc/network/interfaces to match the file provided.
3.	Update the isc dhcp server config file.
4.	Update the isc dhcp interfaces line.
5.	Run the install script to move the python file to the appropriate location and install the systemd service.
6.	Add your devices using bluetoothctl. (pair + trust)
7.	Fin.