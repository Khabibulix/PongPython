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
#   # - [X] Read input
#   # - [X] Treat the input and print result
#   # - [X] User command log
#   ### Combined with PongPython game
#   # - [X] In-game window
#   # - [X] Window appearance based on a button press (maybe TAB key)
#   # - [X] Typing box
#   # - [/] In-game support of all the commands
#   # - [ ] Game event log
#   # - [CANCELLED] Scrollable log
#____________________________________#
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# CODE BEGIN
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# IMPORT
#

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# MACROS
#
SKIP = 0
DEV_GAMELOG = 1
GAME_BALL_ADD = 2
GAME_BALL_REMOVE = 3
GAME_RESET = 4
GAME_BALL_RAYTRACE = 5
GAME_BALL_SIZE = 6
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# GLOBAL
#
commandlist = []
commandlist.append(["dev_gamelog","{Bool}","Enable/Disable game event log print"])
commandlist.append(["game_ball_add","No param","Add a new ball"])
commandlist.append(["game_ball_remove","No param","Remove the last ball"])
commandlist.append(["game_reset","No param","Reset the game"])
commandlist.append(["game_ball_raytrace","{Bool}","Enable/Disable Ball raytrace"])
commandlist.append(["game_pad_size","{Pad id} {Size}","Change pad size"])
log = []

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# FUNCTIONS
#
### PRINT
def print_undefined(arg):
    """
    Tells that the command does not exist.
    :param arg: A string : The name of the concerned command.
    :return: Nothing.
    """
    message = "Error : command \"" + arg + "\" does not exist."
    log.append(message)
    print(message)

def print_wip(arg):
    """
    Tells that the command does exist but is not implemented.
    :param arg: A string : The name of the concerned command.
    :return: Nothing.
    """
    message = "Sorry : command \"" + arg + "\" is not implemented yet."
    log.append(message)
    print(message)

def print_help():
    """
    Prints the list of the available commands.
    :return: Nothing.
    """
    message = "Available commands :"
    log.append(message)
    print(message)
    for i in commandlist :
        message = i[0].ljust(25) + i[1].ljust(25) + i[2]
        log.append(message)
        print(message)


def print_game_ball_add():
    """
    Tells that a ball is added to the game.
    :return: Nothing.
    """
    message = "Adding one ball to the game."
    log.append(message)
    print(message)


### INPUT TREATMENT
def console_input(arg):
    """
    Decodes the command fed in.
    :param arg: A string : The name of the concerned command.
    :return: An int, if it is 0 it does nothing, else the value might be treated outside to call the associated function.
    """
    if arg == "" or arg[0] == " " : return SKIP # Do nothing if input is blank
    arg = arg.lower() # Don't care of the case
    if arg == "help":
        print_help()
        return SKIP
    elif arg == "dev_gamelog":
        print_wip(arg)
        return DEV_GAMELOG
    elif arg == "game_ball_add":
        print_game_ball_add()
        return GAME_BALL_ADD
    elif arg == "game_ball_remove":
        print_wip(arg)
        return GAME_BALL_REMOVE
    elif arg == "game_reset":
        print_wip(arg)
        return GAME_RESET
    elif arg == "game_ball_raytrace":
        print_wip(arg)
        return GAME_BALL_RAYTRACE
    elif arg == "game_pad_size":
        print_wip(arg)
        return GAME_BALL_SIZE
    else:
        print_undefined(arg)
        return SKIP

### LOG MANAGEMENT
def get_log():
    """
    Gives the log of all sended print to the caller.
    :return: A string list : The log.
    """
    return log

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# MAIN
#
# UNUSED
