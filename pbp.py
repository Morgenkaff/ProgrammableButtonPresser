#!/usr/bin/python3
#from gpiozero import LED, Button
from time import sleep
import argparse

#georgcenter_power = LED(17)
#georgcenter_reset = LED(27)
#georgcenter_on = Button(16)

#voldbymc_power = LED(26)
#voldbymc_reset = LED(13)
#voldbymc_on = Button(12)

srv = "null"
action = 0

parser = argparse.ArgumentParser()
parser.add_argument("server", help="chooses wich server to control. georg for georgcenter or vold for voldby_mc.")
parser.add_argument("action", help="chooses wich action to trigger. (st)atus, (re)set, (sh)utdown og (tu)rnon.")
args = parser.parse_args()

print("1. arg is '{}'.".format(args.server))
if args.server == "georg" or args.server == "vold":
    srv = args.server
else:
    print("Wrong arguments. Try 'pbp.py -h'")
    
if srv != "null":

    print("2. arg is '{}'.".format(args.action))
    if args.action == "status" or args.action == "st":
        action = 1
    elif args.action == "reset" or args.action == "re":
        action = 2
    elif args.action == "shutdown" or args.action == "sh":
        action = 3
    elif args.action == "turnon" or args.action == "tu":
        action = 4
        
    print("Server: {}".format(args.server)+"\n"+"Action: {}".format(action)+"\n")
    check =  input("Is that correct? Y/N ")
    
    if check == "y" or check == "Y":
        print("code running...")
    
        if srv == "georg":
            #georg_code:
            if action == 1:
                #Print Georgcenter status
                print("Georgcenter status")
            elif action == 2:
                #Reset Georgcenter
                print("Georgcenter resets")
            elif action == 3:
                #Shutdown Georgcenter
                print("Georgcenter shuts down")
            elif action == 4:
                #Turn on Georgcenter
                print("Georgcenter turns on")
            
        elif srv == "vold":
            #vold_code:
            if action == 1:
                #Print Voldby_mc status
                print("Voldby_mc status")
            elif action == 2:
                #Reset Voldby_mc
                print("Voldby_mc resets")
            elif action == 3:
                #Shutdown Voldby_mc
                print("Voldby_mc shuts down")
            elif action == 4:
                #Turn on Voldby_mc
                print("Voldby_mc turns on")
        
        else:
            print("Somethings rotten in the state of Denmark..")
    
    else:
        print("Quitting..")



#while True:
    #led.on()
    #sleep(1)
    #led.off()
    #sleep(1) 

