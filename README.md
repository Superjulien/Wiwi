
# Wiwi

A simple interface selection for wifi. Install the driver wifi card before.

## Documentation

- [Python](https://www.python.org/doc/)
- [Ethtool](https://linux.die.net/man/8/ethtool)
- [Network-manager](https://developer-old.gnome.org/NetworkManager/stable/)

## Installation
Required : 
- python 3
- ethtool
- network-manager

### Linux Advanced Packaging Tool :
```
sudo apt install && sudo apt upgrade -y
sudo apt install ethtool network-manager 
git clone https://github.com/Superjulien/Wiwi.git 
```
    
## Usage

```
sudo python3 wiwi.py -h
usage: wiwi.py [-h] [-wt WLANTYPE] [-r] [-rq]

optional arguments:
  -h, --help            show this help message and exit
  -wt WLANTYPE, --wlantype WLANTYPE
                        wlan interface & new type // ex: wlan0 monitor
  -r                    restart network service
  -rq                   restart network service & exit
```
### Examples :
```
sudo python3 wiwi.py
Interface :

1: wlan0
2: wlan1

Selection Num Interface (ex: 2 , 1) :
2

#############
wlan1
type managed
driver: ath9k
#############

1.IBSS
2.Managed
3.AP
4.Monitor

Selection type :
4

Successful
```

## Support

For support, email [superjulien](mailto:contact.superjulien@gmail.com).  
