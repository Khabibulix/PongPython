##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#   DevConsole for cheats and testing
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#   Possible commands TODO :
#   ### Dev
#   # - dev_gamelog             #-// {Bool}             #-// Enable/Disable game event log print
#   ### Cheats
#   # - game_ball_add           #-// No param           #-// Add a new ball
#   # - game_ball_remove        #-// No param           #-// Remove the last ball
#   # - game_reset              #-// No param           #-// Reset the game
#   # - game_ball_retrace       #-// {Bool}             #-// Enable/Disable Ball raytrace
#   # - game_pad_size           #-// {Pad id} {Size}    #-// Change pad size
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#   Functionnalities TODO :
#   ### Isolated part
#   # - [X] devconsole.py existence
#   # - [ ] Read input
#   # - [ ] Treat the input and print result
#   # - [ ] User command log
#   ### Combined with PongPython game
#   # - [ ] In-game window
#   # - [ ] Window appearance based on a button press (maybe TAB key)
#   # - [ ] Typing box
#   # - [ ] Game event log
#   # - [ ] Scrollable log
#____________________________________#
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# CODE BEGIN
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# IMPORT
#
import sys
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# MACROS
#
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# GLOBAL
#
argv = sys.argv
argcount = len(argv)
if argcount > 1:
    argcommand = argv[1]
# commandlist = ["dev_gamelog","game_ball_add","game_ball_remove","game_reset","game_ball_retrace","game_pad_size"]
commandlist = []
commandlist.append(["dev_gamelog","{Bool}","Enable/Disable game event log print"])
commandlist.append(["game_ball_add","No param","Add a new ball"])
commandlist.append(["game_ball_remove","No param","Remove the last ball"])
commandlist.append(["game_reset","No param","Reset the game"])
commandlist.append(["game_ball_retrace","{Bool}","Enable/Disable Ball raytrace"])
commandlist.append(["game_pad_size","{Pad id} {Size}","Change pad size"])
log = []

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# FUNCTIONS
#
def print_undefined(arg):
    message = "Error : command \"" + arg + "\" does not exist."
    log.append(message)
    print(message)

def print_wip(arg):
    message = "Sorry : command \"" + arg + "\" is not implemented yet."
    log.append(message)
    print(message)

def print_help():
    print("Available commands :")
    for i in commandlist :
        message = i[0].ljust(25) + i[1].ljust(25) + i[2]
        log.append(message)
        print(message)

def console_input(arg):
    arg = arg.lower() # Don't care of the case
    if arg == "help":
        print_help()
    elif arg == "dev_gamelog":
        print_wip(arg)
    elif arg == "game_ball_add":
        print_wip(arg)
    elif arg == "game_ball_remove":
        print_wip(arg)
    elif arg == "game_reset":
        print_wip(arg)
    elif arg == "game_ball_retrace":
        print_wip(arg)
    elif arg == "game_pad_size":
        print_wip(arg)
    else:
        print_undefined(arg)

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# MAIN
#
""" PRINT INPUT
print(argv)
print(argcount)
print("Command : " + argcommand)
"""

if argcount > 1:
    console_input(argcommand)
while(1):
    usercommand = input("- ")
    log.append(usercommand)
    usercommand = list(usercommand.split(" ")) # Take the string list as a whole and split it into string sub-lists (= 2D array) for each words
    console_input(usercommand[0]) # Take the first word as parameter (= command)
