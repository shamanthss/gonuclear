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

global_user= os.getlogin()

# Function to print banner
def about():
    user = os.getcwd()
    print(f" {blue}----------------------------------------------------------")
    print(f" {blue}|{nc}         Simple Script to Install {green1}Go {nc}and {blue1}Nuclei         {blue}|{nc}")
    print(f" {blue}|{nc}                 {pink}Created by {yellow1}@shamanthss                 {blue}|{nc}")
    print(f" {blue}----------------------------------------------------------{nc}")

# Check and install dependencies
def install_dependencies():
    print(f"\n{green} (+) Checking System Updates and Installing Dependencies...{green}")
    subprocess.run(["sudo", "apt", "update", "-y"])
    subprocess.run(["sudo", "apt", "install", "git", "-y"])

# Install Go
def install_go():
    print("")
    print(f"\n{green} (+) Installing Go...")
    subprocess.run(["wget", "https://go.dev/dl/go1.21.6.linux-amd64.tar.gz"])
    subprocess.run(["sudo", "tar", "-C", "/usr/local", "-xzf", "go1.21.6.linux-amd64.tar.gz"])
    print(f"\n{green} (+) Download and Extraction Completed....")
    time.sleep(1)
    print("")
    print(f"{yellow} (x) Deleting {blue1}GO {yellow}installer file...")
    subprocess.run(["rm", "go1.21.6.linux-amd64.tar.gz"])
    
# Install Nuclei
def install_nuclei():
    print("")
    print(f"{green} (+) Installing Nuclei...")
    command = ["go", "install", "-v", "github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest"]
    subprocess.run(command)
    # Add nuclei to /local/bin/
    global global_user
    subprocess.run(["sudo", "cp", f"/home/{global_user}/go/bin/nuclei", "/usr/local/go/bin/"])

# Configure Nuclei with default templates
def configure_nuclei():
    print("")
    print(f"{green} (+) Checking for Nuclei updates...")
    command = ["nuclei", "-update"]
    subprocess.run(command)
    print("")
    print(f"{green} (+) Updating Nuclei...")
    subprocess.run(["nuclei", "-update-templates"])
    time.sleep(1)

# Main function
def main():
    about()
    #install_dependencies()
    #install_go()
    time.sleep(2)
    install_nuclei()
    configure_nuclei()
    time.sleep(2)
    print(f"")
    print(f"{green1} (+) Nuclei {green}installation and configuration completed successfully!{nc}")
    time.sleep(1)
    print(f"")
    print(f"{green1} (+) Run {blue}nuclei -v {green1}to verify installation....")
    print(f"")

main()
