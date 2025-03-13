import numpy as np

import time
import sys
from colorama import init, Fore, Style #
########################################
# Colorama Settings #
########################################
# Forces .exe to accept colorama       #
init()                                 #
# Increase Brightness of Text          #
print(Style.BRIGHT)  

# Heads   \n  Torso \n  Legs

# Define the frames of the animation
frames = [
    Fore.MAGENTA + " O" + Fore.CYAN + "                O \n" + Fore.MAGENTA + "/|\\" + Fore.CYAN + "              /|\\\n" + Fore.MAGENTA + "/ \\" + Fore.CYAN + "              / \\" + Style.RESET_ALL,
    Fore.MAGENTA + " O" + Fore.CYAN + "              O \n" + Fore.MAGENTA + "/|\\" + Fore.CYAN + "            /|\\\n" + Fore.MAGENTA + "/ \\" + Fore.CYAN + "            / \\" + Style.RESET_ALL,
    Fore.MAGENTA + " O" + Fore.CYAN + "            O \n" + Fore.MAGENTA + "/|\\" + Fore.CYAN + "          /|\\\n" + Fore.MAGENTA + "/ \\" + Fore.CYAN + "          / \\" + Style.RESET_ALL,
    Fore.MAGENTA + " O" + Fore.CYAN + "          O \n" + Fore.MAGENTA + "/|\\" + Fore.CYAN + "        /|\\\n" + Fore.MAGENTA + "/ \\" + Fore.CYAN + "        / \\" + Style.RESET_ALL,
    Fore.MAGENTA + " O" + Fore.CYAN + "        O \n" + Fore.MAGENTA + "/|\\" + Fore.CYAN + "      /|\\\n" + Fore.MAGENTA + "/ \\" + Fore.CYAN + "      / \\" + Style.RESET_ALL,
    Fore.MAGENTA + " O" + Fore.CYAN + "      O \n" + Fore.MAGENTA + "/|\\" + Fore.CYAN + "    /|\\\n" + Fore.MAGENTA + "/ \\" + Fore.CYAN + "    / \\" + Style.RESET_ALL,
    Fore.MAGENTA + " O" + Fore.CYAN + "    O \n" + Fore.MAGENTA + "/|\\" + Fore.CYAN + "  /|\\\n" + Fore.MAGENTA + "/ \\" + Fore.CYAN + "  / \\" + Style.RESET_ALL,
    Fore.MAGENTA + " O" + Fore.CYAN + "  O \n" + Fore.MAGENTA + "/|\\" + Fore.CYAN + "/|\\\n" + Fore.MAGENTA + "/ \\" + Fore.CYAN + "/ \\" + Style.RESET_ALL,
    Fore.MAGENTA + " O" + Fore.CYAN + "O *kiss*\n" + Fore.MAGENTA + "/|\\" + Fore.CYAN + "/|\\\n" + Fore.MAGENTA + "/ \\" + Fore.CYAN + "/ \\" + Style.RESET_ALL,
    Fore.MAGENTA + " O" + Fore.CYAN + "  O Happy Anniversary Darling <3 \n" + Fore.MAGENTA + "/|\\" + Fore.CYAN + "/|\\\n" + Fore.MAGENTA + "/ \\" + Fore.CYAN + "/ \\" + Style.RESET_ALL,
    Fore.MAGENTA + " O" + Fore.CYAN + "  O I love you so much!!! \n" + Fore.MAGENTA + "/|\\" + Fore.CYAN + "/|\\\n" + Fore.MAGENTA + "/ \\" + Fore.CYAN + "/ \\" + Style.RESET_ALL,
    
    
    Fore.RED +
    "                  ****                   ****\n"
    "               **********             **********\n"
    "            **************          **************\n"
    "        **********      ****      ****      **********\n"
    "    ***********          *************          ***********\n"
    " *************            ***********            *************\n"
    " *************                                   *************\n"
    " **************              Jess               **************\n"
    "  **************               &               **************\n"
    "    *************            Evan             **************\n"
    "       **************                      **************\n"
    "          **************                **************\n"
    "             **************          **************\n"
    "                **************    **************\n"
    "                   **************************\n"
    "                      ********************\n"
    "                         **************\n"
    "                            ********\n"
    "                               **\n" + Style.RESET_ALL
]

# Loop to create the animation
time.sleep(4)
Message = f"""
{"-"*50}
{"Happy Anniversary".center(50)}
{"You are an amazing human, kind, companionate,".center(50)}
{"a loving mother and a fantastic healer.".center(50)}
{"I am so grateful to have you in my life.".center(50)}

{"A rock to lean on".center(50)}
{"A hand to hold".center(50)}
{"A shoulder to cry on".center(50)}
{"A heart of Gold".center(50)}

{"Beauty through and through inside and out ".center(50)}
{"Like waves caressing the shore".center(50)}
{"Lions mane, rosey cheeks, and so much more".center(50)}
{"A woman that I simply adore".center(50)}


{"I love you more than words can express".center(50)}

{"-"*50}
"""
print(Fore.GREEN +Message)
time.sleep(15)
# Clear the screen
sys.stdout.write('\033c')

while True:
    for i, frame in enumerate(frames):
        # Clear the screen
        sys.stdout.write('\033c')
        # Print the frame and flush the output
        sys.stdout.write(frame + '\n')
        sys.stdout.flush()
        # Delay for a short period
        if i >= len(frames) - 3:
            time.sleep(4)  # Longer delay for the last 3 frames
        else:
            time.sleep(0.5)  # Shorter delay for the other frames
