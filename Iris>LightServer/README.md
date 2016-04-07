## LightServer (Codename: Rainbow/Iris) ##

The network -> lights/LEDs part of the project.

### Setup ###
*	For Development Environments:
	1.	Run dev-install.sh (in the [_scripts_](/Iris>LightServer/scripts/) folder) to install the needed packages and setup the Python virtual environment.
	2.	Copy the pre-commit hook script (in the [_scripts_](/Iris>LightServer/scripts/) folder) to .git/hooks. More information [here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks#Client-Side-Hooks)
	3.	???
*	For Production Environments:
	1.	Run the prod-install.sh script (To Be Written...) to build and install the LightServer.
	2.	Register the LightServer as a SystemD service.
	3.	Optionally, also follow the pi-configuration guide in the Misc project part folder (recommended for offical setups). (To Be Written...)

### Project Part Folder Layout ###
*	app/
	*	The core LightServer system.
*	docs/
	*	Just notes planning the LightServer system.
*	effects/
	*	Kind of like plugins for the LightServer.
	*	These are the 'effects' that run on the lights (think patterns/animations, etc).
*	requirements.txt
	*	A file for pip (Python Package manager) that the precommit hook auto generates before each commit.
	*	Meant to keep venv's (virtual environments) in sync across development machines.
*	scripts/
	*	A collection of development, production, and test scripts.
