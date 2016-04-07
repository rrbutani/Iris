# Iris #
### Magical Rainbow Lights! ###

Iris is a multipart project. Here are its parts:
*	LightServer (Codename: Rainbow/Iris)
	*	This is the main part of the project and as such, inherits the name Iris from the project for use in all code/configuration files.
	*	Located in the [_Iris>LightServer_](/Iris>LightServer/) folder.
	*	Essentially provides network control of the lights.
	*	Internally known as Rainbow, since the LightServer is the part of the project that actually controls the lights/LEDs. Or just Iris.
*	Networking	(Codename: Zephyrus)
	*	Located in the [_Iris>Networking_](/Iris>Networking/) folder.
	*	This part of the project is responsible for creating a bluetooth NAP on the Raspberry Pi that enables mobile devices to communicate with the LightServer.
	*	This is an optional part of the Iris setup, however it is useful in embedded installations such as the Team Standard.
	*	Internally known as Zephyrus (The West Wind) as he is, mythologically, the 'messenger' that enabled communication.
*	APIClient	(Codename: Pothos)
	*	Located in the [_Iris>APIClient_](/Iris>APIClient/) folder.
	*	This contains some sample code for interfacing with the LightServer's REST API as well as documentation on the API.
	*	Internally known as Pothos as Pothos is, in Greek mythology, the son of Iris and Zephyrus.
*	Misc 		(Codename: Blackhole)
	*	Located in the [_Iris>Misc_](/Iris>Misc/) folder.
	*	Contains some other things (guides/scripts/links) relevant to the setup of either Iris or the Raspberry Pis.
	*	Internally known as the blackhole. Keep it neat though.

Each part of the project has it's own README and setup instructions.