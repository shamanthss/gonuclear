#!/usr/bin/env python3

import os
import subprocess
import time

# Define colors
red = '\033[0;31m'
red1 = '\033[1;31m'
green = '\033[0;32m'
green1 = '\033[1;32m'
yellow = '\033[0;33m'
yellow1 = '\033[1;33m'
blue = '\033[0;34m'
blue1 = '\033[1;34m'
pink = '\033[0;35m'
nc = '\033[0m' # NoColor

# Function to print banner
def about():
    print(f" {blue}----------------------------------------------------------")
    print(f" {blue}|{nc}         Simple Script to Install {green1}Go {nc}and {blue1}Nuclei         {blue}|{nc}")
    print(f" {blue}|{nc}                 {pink}Created by {yellow1}@shamanthss                 {blue}|{nc}")
    print(f" {blue}----------------------------------------------------------{nc}")
    time.sleep(1)
    user = os.getlogin()
    print(f"{green1} Hello{yellow1}",user,f"{green}....")
    time.sleep(1)
    
# Adding PATH to source file based on OS Option from check_os()
def add_path_kali():
    home_directory = os.path.expanduser("~")
    zshrc_path = os.path.join(home_directory, ".zshrc")
    print(f"{green} (+) Making changes to{yellow1}",zshrc_path)
    with open(zshrc_path, "a") as zshrc_file:
        zshrc_file.write("\n")
        zshrc_file.write("GOPATH=/root/go-workspace\n")
        zshrc_file.write("export GOROOT=/usr/local/go\n")
        zshrc_file.write("PATH=$PATH:$GOROOT/bin/:$GOPATH/bin\n")
    print(f"{green} (+) Made changes successfully....{nc}")
    time.sleep(2)
    print("")
    print(f"{yellow1} Please execute {green1}sudo python3 installer.py{nc}")
    print("")
    os.system("zsh")

def add_path_ubuntu():
    home_directory = os.path.expanduser("~")
    bashrc_path = os.path.join(home_directory, ".bashrc")
    print(f"{green} (+) Making changes to{yellow1}",bashrc_path)
    with open(bashrc_path, "a") as bashrc_file:
        bashrc_file.write("\n")
        bashrc_file.write("GOPATH=/root/go-workspace\n")
        bashrc_file.write("export GOROOT=/usr/local/go\n")
        bashrc_file.write("PATH=$PATH:$GOROOT/bin/:$GOPATH/bin\n")
    print(f"{green} (+) Made changes successfully....{nc}")
    time.sleep(2)
    print("")
    print(f"{yellow1} (*) Please execute {green1}sudo python3 installer.py{nc}")
    print("")
    os.system("bash")    

# Function to autofind the Operating System using os-release file    
def find_os():
    try:
        with open('/etc/os-release', 'r') as file:
            for line in file:
                if line.startswith('ID='):
                    os_id = line.split('=')[1].strip().strip('"')
                    # Check the OS and print specific messages
                    if os_id == "kali":
                        print(f"{green} (+) Operating System Detected: {blue1}Kali{nc}")
                        time.sleep(1)
                        add_path_kali()
                    elif os_id == "ubuntu":
                        print(f"{green} (+) Operating System Detected: {yellow1}Ubuntu{nc}")
                        time.sleep(1)
                        add_path_ubuntu()

                    return
    except FileNotFoundError:
        pass
    print(f"{red1} (X) Unable to determine the Operating System.")
    print(f"{red} (X) Only {blue1}Kali and {yellow1}Ubuntu {red}are support at this moment...")
    print(f"{yellow1} You can manually add the following lines to your {green}/home/",{user},"/.bashrc {yellow}config file{nc}")
    print(f"{nc} GOPATH=/root/go-workspace")
    print(f"{nc} export GOROOT=/usr/local/go")
    print(f"{nc} PATH=$PATH:$GOROOT/bin/:$GOPATH/bin")
    print("")
def main():
    if os.geteuid() == 0:
        print("")
        print(f"{red1} (X) Please run this script as a Normal User...")
        print("")
    else:
        about()
        find_os()

# Calling main function        
main()

