#!/usr/bin/python3

import os
import subprocess
import re
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-wt", "--wlantype", type=str, help="wlan interface & new type // ex: wlan0 monitor")
parser.add_argument("-r",action='store_true', help="restart network service")
parser.add_argument("-rq",action='store_true', help="restart network service & exit")

args = parser.parse_args()
if args.r:
    os.system("service NetworkManager restart")
    print("Service NetworkManager Restart")
    print("")
if args.rq:
    os.system("service NetworkManager restart")
    print("Service NetworkManager Restart")
    quit()

try :
    print ("Interface :" )
    print ("")
    iw_name = "iw dev | grep Interface | cut -f2- | grep -n Interface | sed -e \"s/Interface//g\""
    liste = os.popen(iw_name).readlines()

    iw_name = "iw dev | grep Interface | cut -f2- | sed -e \"s/Interface//g\""
    liste2 = os.popen(iw_name).readlines()

    for index in range(len(liste)):
        liste[index] = re.sub('\\r*\\n*\\\\*', '', liste[index])
        print (liste[index])

    print ("")
    print ("Selection Num Interface (ex: 2 , 1) :")
    selec = int(input())
    print("")
    error = "Device not found"
    liste.insert(0, error)
    liste2.insert(0, error)

    if selec > len(liste) or selec == 0 :
        print(error)
    else :
        var = str(liste2[selec].strip())
        print("#############")
        print (var)
        iw_type = str("iw "+ var +" info | cut -f2- | grep type | sed -e \"s/Interface//g\"")
        iw_nam = str("ethtool -i "+ var +" | cut -f2- | grep driver | sed -e \"s/Interface//g\"")
        os.system(iw_type)
        os.system(iw_nam)
        print("#############")
        print("")

    liste=["1.IBSS","2.Managed","3.AP","4.Monitor"]

    for index in range(len(liste)):
        print (liste[index])

    print("")
    print("Selection type :")
    wla = var
    liste.insert(0, error)
    selec = int(input())

    if selec > len(liste) or selec == 0 :
        print(error)
    else :
        if selec == 1 :
            mod = "ibss"
        elif selec == 2 :
            mod = "managed"
        elif selec == 3 :
            mod = "ap"
        elif selec == 4 :
            mod = "monitor"
        else :
            print(error)

    act1 = "ip link set " + wla + " down"
    act2 = "iw dev " + wla + " set type " + mod
    act3 = "ip link set " + wla + " up"

    osc = os.system(act1)
    osc2 = os.system(act2)
    osc3 = os.system(act3)


    if osc == 0 and osc2 == 0 and osc3 == 0 :
        var = 1
    else :
        var = 0

    if var == 1 :
        print("")
        print("Successful")
    else :
        print("")
        print("Failure")
except KeyboardInterrupt :
    quit()
