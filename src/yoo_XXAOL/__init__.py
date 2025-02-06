import subprocess
from os import system
from os import chdir
import sys
from time import sleep

args = sys.argv[1]
system("mkdir ~/.yoo")
sleep(0.25)
chdir("./.yoo")
system("git clone https://aur.archlinux.org/"+ args +".git")
chdir("./"+args)
system("makepkg -s -i")
system("rm -rf ~/.yoo/"+ args + "/")