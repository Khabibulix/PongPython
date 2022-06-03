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
argcommand = argv[1]
commandlist = ["dev_gamelog","game_ball_add","game_ball_remove","game_reset","game_ball_retrace","game_pad_size"]

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# FUNCTIONS
#
def print_undefined(arg):
    print("Error : command \"" + arg + "\" does not exist.")

def print_wip(arg):
    print("Sorry : command \"" + arg + "\" is not implemented yet.")

def print_help():
    print("Available commands :")
    for i in commandlist :
        print(i)

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# MAIN
#
""" PRINT INPUT
print(argv)
print(argcount)
print("Command : " + argcommand)
"""

if argcount > 1:
    if argcommand == "" or argcommand == "help":
        print_help()
    elif argcommand == "dev_gamelog":
        print_wip(argcommand)
    elif argcommand == "game_ball_add":
        print_wip(argcommand)
    elif argcommand == "game_ball_remove":
        print_wip(argcommand)
    elif argcommand == "game_reset":
        print_wip(argcommand)
    elif argcommand == "game_ball_retrace":
        print_wip(argcommand)
    elif argcommand == "game_pad_size":
        print_wip(argcommand)
    else:
        print_undefined(argcommand)
    
else :
    pass