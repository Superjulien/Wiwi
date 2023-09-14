# WiWi

[![Version](https://img.shields.io/badge/Version-1.0-blue.svg)](https://github.com/Superjulien/Wiwi) [![Python](https://img.shields.io/badge/Python_3-14354C?&logo=python&logoColor=white.svg)](https://www.python.org/)

WiWi is a Python command-line tool for managing and configuring wireless network interfaces on a Linux system. It provides a convenient way to change the operating mode of your wireless interface and restart the NetworkManager service.

## Features

- **Restart NetworkManager Service**: Quickly restart the NetworkManager service to resolve network connectivity issues.

- **Interface Selection**: View a list of available wireless interfaces and select the one you want to configure.

- **Wireless Mode Configuration**: Configure the selected wireless interface with different modes:
  - **IBSS (Ad-hoc)**: Create a peer-to-peer wireless network.
  - **Managed**: Connect to an existing wireless network.
  - **AP (Access Point)**: Turn your device into a wireless access point.
  - **Monitor**: Enable monitoring mode for wireless packet capture and analysis.

- **Interface Information**: Get detailed information about the current state and driver of the selected wireless interface.

## Prerequisites

- **Sudo:** Sudo access is required for changing interface modes and restarting the NetworkManager service.
- **Operating System:** Designed for Linux-based systems.
- **Python 3.x:** WiWi is built using Python 3.x, so make sure you have Python 3.x installed on your system.
- **Installed Dependencies:** WiWi requires the following dependencies to be installed on your system:
  - `ethtool`
  - `network-manager`

## Installation

Before using WiWi, make sure you have the following dependencies installed on your Linux system. Here is an example for Debian/Ubuntu:

```shell
sudo apt install && sudo apt upgrade -y
sudo apt install ethtool network-manager
```

Now you're ready to install and use WiWi:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/Superjulien/Wiwi.git
   cd Wiwi
   ```

2. Make the script executable:

   ```shell
   chmod +x wiwi.py
   ```

## Usage

### Interactive Mode

Run the script with root privileges to enter interactive mode:

```shell
sudo python3 wiwi.py
```

Follow the on-screen prompts to select a wireless interface and configure its mode.

### Command-Line Arguments

You can also use command-line arguments to perform specific actions:

```shell
Usage: wiwi.py [-h] [-wt interface mode] [-r] [-rq]

WiWi

Optional arguments:
  -h, --help                  Show this help message and exit.
  -wt interface mode          Choose wireless interface and mode (e.g., wlan0 monitor).
  -r                          Restart NetworkManager service.
  -rq                         Restart NetworkManager service and exit.
```

- To restart the NetworkManager service:

  ```shell
  sudo python3 wiwi.py -r
  ```
- To restart the service and exit:

  ```shell
  sudo python3 wiwi.py -rq
  ```
- To configure a specific wireless interface in monitor mode (replace `wlan0` and `monitor` with your desired interface and mode):

  ```shell
  sudo python3 wiwi.py -wt wlan0 monitor
  ```

## How It Works

WiWi is a Python script that leverages several Linux command-line tools and system utilities to manage wireless network interfaces. Here's a step-by-step breakdown of how WiWi works:

1. **Initialization**:
   - When you run WiWi, it performs initial checks to ensure that it is running on a Linux system and with superuser (root) privileges. If not, it exits with an appropriate error message.

2. **User Interface**:
   - Upon startup, WiWi displays an ASCII art logo to provide a visually appealing introduction.

3. **Command-Line Arguments**:
   - WiWi checks the command-line arguments provided by the user using the `argparse` library.
   - If the user specifies the `-r` or `-rq` flag, WiWi restarts the NetworkManager service accordingly.
   - If the user specifies the `-wt` flag followed by an interface name and mode, WiWi configures the wireless interface as instructed.
   - If no arguments are provided, WiWi enters interactive mode to guide the user through the process of selecting an interface and mode.

4. **NetworkManager Restart**:
   - When the user requests a NetworkManager restart using the `-r` or `-rq` flag, WiWi runs the `service NetworkManager restart` command using `subprocess`. If successful, it displays a success message; otherwise, it shows an error message.

5. **Listing and Selecting Interfaces**:
   - In interactive mode, WiWi lists available wireless interfaces using the `iw dev` command. It parses the output to extract interface names and presents them to the user for selection.
   - The user selects an interface by entering a corresponding number.

6. **Selecting Wireless Mode**:
   - After selecting an interface, the user is prompted to choose a wireless mode from the following options: IBSS, Managed, AP, Monitor, or Quit.
   - WiWi uses the user's choice to configure the wireless interface accordingly.

7. **Wireless Interface Configuration**:
   - WiWi uses the `ip` and `iw` commands through the `subprocess` module to configure the selected wireless interface.
   - It sets the interface down, changes its mode using the `iw dev` command, and brings it back up.
   - If any step in the configuration process fails, WiWi displays an error message.

8. **Interface Information**:
   - WiWi provides additional information about the selected wireless interface, such as its current mode and, if available, the driver in use.

9. **Completion and Exit**:
   - After completing the requested action (e.g., restarting NetworkManager or configuring a wireless interface), WiWi either exits or continues to interact with the user in interactive mode.

WiWi simplifies the management of wireless network interfaces by providing a user-friendly and script-driven interface to essential Linux networking commands. Whether you need to troubleshoot network issues, set up an access point, or analyze wireless traffic, WiWi is a versatile tool for Linux users.

## Sponsoring

This software is provided to you free of charge, with the hope that if you find it valuable, you'll consider making a donation to a charitable organization of your choice :

- SPA (Society for the Protection of Animals): The SPA is one of the oldest and most recognized organizations in France for the protection of domestic animals. It provides shelters, veterinary care, and works towards responsible adoption.

  [![SPA](https://img.shields.io/badge/Sponsoring-SPA-red.svg)](https://www.la-spa.fr/)

- French Popular Aid: This organization aims to fight against poverty and exclusion by providing food aid, clothing, and organizing recreational activities for disadvantaged individuals.

  [![SPF](https://img.shields.io/badge/Sponsoring-Secours%20Populaire%20Français-red.svg)](https://www.secourspopulaire.fr)

- Doctors Without Borders (MSF): MSF provides emergency medical assistance to populations in danger around the world, particularly in conflict zones and humanitarian crises.

  [![MSF](https://img.shields.io/badge/Sponsoring-Médecins%20Sans%20Frontières-red.svg)](https://www.msf.fr)

- Restaurants of the Heart : Restaurants of the Heart provides meals, emergency accommodation, and social services to the underprivileged.

  [![RDC](https://img.shields.io/badge/Sponsoring-Restaurants%20du%20Cœur-red.svg)](https://www.restosducoeur.org)

- French Red Cross: The Red Cross offers humanitarian aid, emergency relief, first aid training, as well as social and medical activities for vulnerable individuals.

   [![CRF](https://img.shields.io/badge/Sponsoring-Croix%20Rouge%20Française-red.svg)](https://www.croix-rouge.fr)

Every small gesture matters and contributes to making a real difference.

## Support

For support email : 

[![Gmail: superjulien](https://img.shields.io/badge/Gmail-Contact%20Me-purple.svg)](mailto:contact.superjulien@gmail.com) [![Tutanota: superjulien](https://img.shields.io/badge/Tutanota-Contact%20Me-green.svg)](mailto:contacts.superjulien@tutanota.com)
