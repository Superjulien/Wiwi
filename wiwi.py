#!/usr/bin/python3

import subprocess
import argparse
import sys
import os

# WiWi
# by superjulien 
# > https://github.com/Superjulien
# > https://framagit.org/Superjulien
# V1.0

def restart_network_service():
    try:
        subprocess.run(["service", "NetworkManager", "restart"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("> Service NetworkManager Restart")
        print("")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting NetworkManager service: {e.stderr}")
        print("")

def get_wireless_interfaces():
    try:
        iw_command = ["iw", "dev"]
        iw_process = subprocess.Popen(iw_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        iw_output, iw_error = iw_process.communicate()
        if iw_process.returncode != 0:
            print(f"Error retrieving wireless interfaces: {iw_error}")
            sys.exit(1)
        interfaces = [line.split()[1] for line in iw_output.splitlines() if "Interface" in line]
        for index, interface in enumerate(interfaces):
            print(f"{index + 1}. {interface}")
        while True:
            selec = input("\nSelection Num Interface (e.g., 2, 1): ")
            try:
                selec = int(selec)
                if 1 <= selec <= len(interfaces):
                    break
                else:
                    print("Error: Please enter a valid number.")
            except ValueError:
                print("Error: Please enter a valid number.")
        selected_interface = interfaces[selec - 1]
        print("")
        print(selected_interface)
        print(f"  > Current interface: {get_wifi_interface_state(selected_interface)}")
        driver = get_wifi_driver(selected_interface)
        if driver:
            print(f"  > WiFi driver: {driver}")
        else:
            print("  > Unable to get the WiFi driver used.")
        return selected_interface
    except KeyboardInterrupt:
        sys.exit(0)

def select_wireless_mode(wireless_interface):
    try:
        while True:
            print("\n1. IBSS\n2. Managed\n3. AP\n4. Monitor\n5. Quit")
            selec = input("\nSelect type: ")
            try:
                selec = int(selec)
                if 1 <= selec <= 5:
                    break
                else:
                    print("Error: Please enter a valid number corresponding to an option.")
            except ValueError:
                print("Error: Please enter a valid number corresponding to an option.")
        if selec == 5:
            sys.exit(0)
        modes = {1: "ibss", 2: "managed", 3: "ap", 4: "monitor"}
        selected_mode = modes[selec]
        return selected_mode

    except KeyboardInterrupt:
        sys.exit(0)

def configure_wireless_interface(wireless_interface, selected_mode):
    try:
        all_interfaces_command = ["ip", "link", "show"]
        all_interfaces_output = subprocess.check_output(all_interfaces_command, text=True)
        all_interfaces = [line.split(":")[1].strip() for line in all_interfaces_output.splitlines() if ":" in line]
        if wireless_interface not in all_interfaces:
            print(f"Error: Interface '{wireless_interface}' does not exist.")
            sys.exit(1)
        subprocess.run(["ip", "link", "set", wireless_interface, "down"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        subprocess.run(["iw", "dev", wireless_interface, "set", "type", selected_mode], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        subprocess.run(["ip", "link", "set", wireless_interface, "up"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("\nSuccessful")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.cmd}")
        print(f"Error message: {e.stderr}")
        print("\nFailure")

def get_wifi_interface_state(wireless_interface):
    try:
        state_command = f"iw dev {wireless_interface} info | grep type | awk '{{print $2}}'"
        interface_mode = subprocess.check_output(state_command, shell=True, text=True).strip()
        return interface_mode
    except KeyboardInterrupt:
        sys.exit(0)

def get_wifi_driver(wireless_interface):
    try:
        command = f"ethtool -i {wireless_interface}"
        result = subprocess.check_output(command, shell=True, text=True)
        lines = result.split('\n')
        driver_line = [line for line in lines if 'driver:' in line][0]
        driver = driver_line.split('driver:')[1].strip()        
        return driver
    except subprocess.CalledProcessError as e:
        print(f"Error executing the ethtool command: {e.stderr}")
        return None

def print_ascii_logo():
    logo = """
 __      __.__        .__ 
/  \    /  \__|_  _  _|__|
\   \/\/   /  \ \/ \/ /  |
 \        /|  |\     /|  |
  \__/\  / |__| \/\_/ |__|
       \/      Version 1.0               
       
    """
    print(logo)

def main():
    if not sys.platform.startswith('linux'):
        print("This script is intended for use on Linux only.")
        sys.exit(1)
    if os.geteuid() != 0:
        print("This program must be run with 'sudo'.")
        sys.exit(1)
    print_ascii_logo()
    parser = argparse.ArgumentParser()
    parser.add_argument("-wt", "--wlantype", type=str, nargs=2, metavar=("interface", "mode"), help="Choose wireless interface and mode (e.g., wlan0 monitor)")
    parser.add_argument("-r", action='store_true', help="restart network service")
    parser.add_argument("-rq", action='store_true', help="restart network service & exit")
    args = parser.parse_args()
    if args.r:
        restart_network_service()
    if args.rq:
        restart_network_service()
        sys.exit(0)
    if args.wlantype:
        wireless_interface, selected_mode = args.wlantype
        configure_wireless_interface(wireless_interface, selected_mode)
        sys.exit(0)
    wireless_interface = get_wireless_interfaces()
    if not wireless_interface:
        return
    selected_mode = select_wireless_mode(wireless_interface)
    if not selected_mode:
        return
    configure_wireless_interface(wireless_interface, selected_mode)

if __name__ == "__main__":
    main()
