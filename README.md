PyStatix
========

Installation (using pip3)
=========================

The easiest and best way to install pystatix is using pip3.

1. If you don't have pip3 installed, use your package manager to install the package python3-pip. For Debian based systems
   the command to use would be. `$ sudo apt-get install python3-pip`.
2. Next, use pip3 to install pystatix. `$ sudo pip3 install pystatix`.

Installation (from source)
==========================

Installing from source is easy.

1. First clone the file with git. `$ git clone https://github.com/braindisassembly/pystatix.git`.
2. Enter the source directory. `$ cd pystatix/`.
3. If you don't have sudo installed/configured, execute setup.py as the root user. `$ su && python3 setup.py install`.
4. if you have sudo installed, log in as a sudoer and execute the setup.py file with sudo. `$ sudo python3 setup.py install`.
5. Done! It should now be a simple case of executing `$ pystatix` in your favorite terminal emulator.
