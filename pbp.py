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

## Set classes

# Class to control IO og pins:
class pins:
    
    # Method to check status (of either one or both servers)
    def check(s):
        if s == 0:
            print("Checks the status of georgcenter")
            
            
        elif s == 1:
            print("Checks the status of voldby_mc")
    
    # Method to force a reset/reboot of a specific server
    def reset(s):
        if s == 0:
            print("resets georgcenter")
        elif s == 1:
            print("Resets voldby_mc")
    
    # Method to force a shutdown of a server
    def shutdown(s):
        if s == 0:
            print("Force a shut down of georgcenter")
        elif s == 1:
            print("Force a shut down of voldby_mc")
        
    # Method to turn on a specific server
    def turn_on(s):
        if s == 0:
            print("Turns on georgcenter")
        elif s == 1:
            print("Turns on voldby_mc")
        
# Class to control and confirm parsed input:
class parse_checker():

    # Class vars
    parser = argparse.ArgumentParser()
    parser.add_argument("server", help="chooses wich server to control. georg for georgcenter or vold for voldby_mc.")
    parser.add_argument("action", help="chooses wich action to trigger. (st)atus, (re)set, (sh)utdown og (tu)rnon.")
    args = parser.parse_args()
    srv = "null"
    
    # Method to check for correct input
    def get_server():
        
        print("1. arg is '{}'.".format(parse_checker.args.server))
        if parse_checker.args.server == "georg" or parse_checker.args.server == "vold":
            return parse_checker.args.server

    def get_action():
        
        # Method vars
        action = 5
        
        print("2. arg is '{}'.".format(parse_checker.args.action))
        if parse_checker.args.action == "status" or parse_checker.args.action == "st":
            action = 0
        elif parse_checker.args.action == "reset" or parse_checker.args.action == "re":
            action = 1
        elif parse_checker.args.action == "shutdown" or parse_checker.args.action == "sh":
            action = 2
        elif parse_checker.args.action == "turnon" or parse_checker.args.action == "tu":
            action = 3
                
        return action

    def confirm(s, a):
        print("Server: {}".format(s)+"\n"+"Action: {}".format(a)+"\n")
        check =  input("Is that correct? Y/N ")
    
        if check == "y" or check == "Y":
            return 1
        else:
            print("Try 'pbp.py -h' for more info")

    def get():
            
        srv = parse_checker.get_server()
        act = parse_checker.get_action()
            
        if srv != None and act < 5:
            if parse_checker.confirm(srv, act):
                if srv == "georg":
                    return 0, act
                elif srv == "vold":
                    return 1, act
            
        else:
            print("Wrong arguments. Try 'pbp.py -h'")

def main():
    args = parse_checker.get()
    
    if args[1] == 0:
        pins.check(args[0])
    elif args[1] == 1:
        pins.reset(args[0])
    elif args[1] == 2:
        pins.shutdown(args[0])
    elif args[1] == 3:
        pins.turn_on(args[0])    

if __name__ == "__main__":
    main()


#while True:
    #led.on()
    #sleep(1)
    #led.off()
    #sleep(1) 

