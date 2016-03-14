#!/bin/sh
#Must run in the root directory of the project!!!

common()
{
  . venv/bin/activate
  echo "Installing required packages.."
  sudo pip -q install -r requirements.txt >> install-log.txt
  echo "Finished!"
}

macOSX()
{
  echo "OS Detected: Mac OS X"
  echo "Assuming MacPorts is already installed..."
  xcode-select --install #For fun!
  sudo port install python34 py34-pip py34-virtualenv
  sudo port select --set python3 python34
  alias virtualenv='virtualenv-3.4'

  echo "Creating virtual environment"
  virtualenv-3.4 --no-site-packages --distribute venv >> install-log.txt
  virtualenv-3.4 --relocatable venv >> install-log.txt
}

linux()
{
  echo "OS Detected: Linux/GNU"
  echo "Assuming Ubuntu 10.10+ or equivalent..."
  sudo apt-get install python3 python3-pip python3-dev virtualenv -qq

  echo "Creating virtual environment"
  virtualenv --no-site-packages --distribute  venv >> install-log.txt
  virtualenv --relocatable venv >> install-log.txt
}

windows()
{
  echo "OS Detected: DOS. Err..Windows"
  echo "Setup for Windows not implemented at this time."
  echo "I pity your soul..."
}
#Creds to SO: http://bit.ly/1pHeRRa
if [ "$(uname)" == "Darwin" ]; then
  # Do something under Mac OS X platform
  macOSX
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  # Do something under GNU/Linux platform
  linux
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
  # Do something under Windows NT platform
  windows
fi

common


#First check environment (Mac OS X or Linux): Assume apt-get for Linux, port for Mac OS X

#Then install python3, pip3, python3-dev, and virtualenv

#Then create/generate the virtualenvironment according to spec and use pip to install all packages

#That should be it.. for now the required packages are 'Flask' and 'flask-restful'
